import json

from app.llm.client import gerar_resposta
from app.rag.retriever import buscar_chunks

INTENCOES = ["roadmap", "profissao", "curso", "certificacao", "faq"]
INTENCAO_PADRAO = "faq"
INTENCOES_COM_PERFIL = ["roadmap", "curso"]

NIVEIS = ["iniciante", "intermediario", "avancado"]
ORCAMENTOS = ["gratuito", "pago", "ambos"]
NIVEL_PADRAO = "iniciante"
ORCAMENTO_PADRAO = "ambos"
FILTRO_GRATUITO = {"gratuito": "true", "pago": "false"}

INSTRUCAO_CLASSIFICACAO = """Classifique a mensagem de um iniciante na área de dados em UMA das categorias abaixo.

roadmap: quer saber o caminho de estudos para uma profissão.
profissao: quer saber o que faz, quanto ganha ou como é uma profissão.
curso: quer indicação de cursos, gratuitos ou pagos.
certificacao: quer saber sobre certificações.
faq: dúvidas gerais sobre entrar na área, ou qualquer outro assunto.

Responda apenas com o nome da categoria, em minúsculas, sem mais nada."""

INSTRUCAO_PERFIL = """Extraia da mensagem o perfil de quem quer entrar na área de dados.

nivel: iniciante, intermediario ou avancado (sem acento).
area_interesse: a profissão ou área citada, em poucas palavras.
orcamento: gratuito, pago ou ambos.

Responda apenas com um JSON no formato {"nivel": ..., "area_interesse": ..., "orcamento": ...}.
Use null para o que a mensagem não informar. Não invente."""

INSTRUCAO_SISTEMA = """Você é o Mentor de Dados, um orientador de carreira para iniciantes na área de dados e inteligência artificial.

Responda sempre em português do Brasil, de forma clara e direta.
Use apenas as informações do contexto fornecido.
Se o contexto não tiver a informação pedida, diga que não tem essa informação na base.
Não invente cursos, links, preços ou salários.
Quando o contexto trouxer "[VERIFICAR ...]", avise que esse dado precisa ser conferido na fonte oficial.
Se houver o perfil da pessoa, adapte a resposta ao nível e ao orçamento dela."""


def normalizar_intencao(texto):
    intencao = texto.strip().lower()
    return intencao if intencao in INTENCOES else INTENCAO_PADRAO


def normalizar_opcao(valor, opcoes):
    if not isinstance(valor, str):
        return None
    valor = valor.strip().lower()
    return valor if valor in opcoes else None


def normalizar_texto(valor):
    if not isinstance(valor, str) or not valor.strip():
        return None
    return valor.strip()


def ler_json(texto):
    limpo = texto.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    try:
        dados = json.loads(limpo)
    except json.JSONDecodeError:
        return {}
    return dados if isinstance(dados, dict) else {}


def faltam_dados(estado):
    return not estado.get("nivel") or not estado.get("orcamento")


def montar_filtro(estado):
    intencao = estado.get("intencao", INTENCAO_PADRAO)
    filtro_tipo = {"tipo": intencao}
    orcamento = estado.get("orcamento")

    if intencao == "curso" and orcamento in FILTRO_GRATUITO:
        return {"$and": [filtro_tipo, {"gratuito": FILTRO_GRATUITO[orcamento]}]}

    return filtro_tipo


def montar_consulta(estado):
    area = estado.get("area_interesse")
    if area and estado.get("intencao") in INTENCOES_COM_PERFIL:
        return f"{estado['pergunta']} {area}"
    return estado["pergunta"]


def montar_contexto(chunks):
    textos = [texto for texto, _ in chunks]
    return "\n\n---\n\n".join(textos)


def montar_perfil(estado):
    partes = []
    if estado.get("nivel"):
        partes.append(f"nível {estado['nivel']}")
    if estado.get("area_interesse"):
        partes.append(f"área de interesse {estado['area_interesse']}")
    if estado.get("orcamento"):
        partes.append(f"orçamento {estado['orcamento']}")
    return ", ".join(partes)


def montar_conversa(historico):
    linhas = [f"{item['papel']}: {item['texto'][:500]}" for item in historico[-4:]]
    return "\n".join(linhas)


def registrar_historico(estado, resposta):
    historico = estado.get("historico", [])
    return historico + [
        {"papel": "usuario", "texto": estado["mensagem"]},
        {"papel": "mentor", "texto": resposta},
    ]


def classificar_intencao(estado):
    if estado.get("aguardando_perfil"):
        return {}

    resposta = gerar_resposta(INSTRUCAO_CLASSIFICACAO, estado["mensagem"])
    return {
        "intencao": normalizar_intencao(resposta),
        "pergunta": estado["mensagem"],
    }


def extrair_perfil(estado):
    aguardando = estado.get("aguardando_perfil", False)

    if estado["intencao"] not in INTENCOES_COM_PERFIL and not aguardando:
        return {}

    dados = ler_json(gerar_resposta(INSTRUCAO_PERFIL, estado["mensagem"]))
    nivel = normalizar_opcao(dados.get("nivel"), NIVEIS) or estado.get("nivel")
    orcamento = normalizar_opcao(dados.get("orcamento"), ORCAMENTOS) or estado.get("orcamento")
    area = normalizar_texto(dados.get("area_interesse")) or estado.get("area_interesse")

    if aguardando:
        nivel = nivel or NIVEL_PADRAO
        orcamento = orcamento or ORCAMENTO_PADRAO

    perfil = {"nivel": nivel, "orcamento": orcamento, "area_interesse": area}
    perfil = {chave: valor for chave, valor in perfil.items() if valor}
    perfil["aguardando_perfil"] = False
    return perfil


def perguntar_perfil(estado):
    perguntas = []
    if not estado.get("nivel"):
        perguntas.append("qual é o seu nível atual na área de dados (iniciante, intermediário ou avançado)")
    if not estado.get("orcamento"):
        perguntas.append("você prefere cursos gratuitos, pagos ou tanto faz")

    resposta = "Para te orientar melhor, " + " e ".join(perguntas) + "?"
    return {
        "resposta": resposta,
        "aguardando_perfil": True,
        "historico": registrar_historico(estado, resposta),
    }


def recuperar_contexto(estado):
    consulta = montar_consulta(estado)
    chunks = buscar_chunks(consulta, quantidade=5, filtro=montar_filtro(estado))

    if not chunks:
        chunks = buscar_chunks(consulta, quantidade=5)

    return {"chunks": chunks}


def responder(estado):
    partes = [f"Contexto:\n{montar_contexto(estado['chunks'])}"]

    perfil = montar_perfil(estado) if estado["intencao"] in INTENCOES_COM_PERFIL else ""
    if perfil:
        partes.append(f"Perfil da pessoa: {perfil}")

    conversa = montar_conversa(estado.get("historico", []))
    if conversa:
        partes.append(f"Conversa até agora:\n{conversa}")

    partes.append(f"Pergunta: {estado['pergunta']}")

    resposta = gerar_resposta(INSTRUCAO_SISTEMA, "\n\n".join(partes))
    return {
        "resposta": resposta,
        "historico": registrar_historico(estado, resposta),
    }
