from app.graph import nodes
from app.graph.build_graph import montar_grafo


def conversar(grafo, mensagem, conversa="teste"):
    configuracao = {"configurable": {"thread_id": conversa}}
    return grafo.invoke({"mensagem": mensagem}, configuracao)


def test_roadmap_sem_perfil_pergunta_antes_de_buscar(falsos):
    estado = conversar(montar_grafo(), "Qual o roadmap?")

    assert estado["aguardando_perfil"] is True
    assert "nível" in estado["resposta"]
    assert falsos["buscas"] == []


def test_depois_da_resposta_busca_com_a_pergunta_original(falsos):
    grafo = montar_grafo()
    conversar(grafo, "Qual o roadmap?")

    estado = conversar(grafo, "sou iniciante, quero gratuito, engenharia de IA")

    assert estado["intencao"] == "roadmap"
    assert estado["nivel"] == "iniciante"
    assert estado["aguardando_perfil"] is False
    assert falsos["buscas"] == [
        {"pergunta": "Qual o roadmap? engenharia de IA", "filtro": {"tipo": "roadmap"}}
    ]
    assert estado["resposta"].startswith("RESPOSTA:")


def test_perfil_completo_na_primeira_mensagem_nao_pergunta(falsos):
    estado = conversar(montar_grafo(), "Quero um roadmap, sou iniciante e prefiro gratuito")

    assert estado["resposta"].startswith("RESPOSTA:")
    assert len(falsos["buscas"]) == 1


def test_profissao_responde_direto_sem_extrair_perfil(falsos):
    estado = conversar(montar_grafo(), "Quanto ganha um engenheiro de IA?")

    assert estado["intencao"] == "profissao"
    assert falsos["buscas"][0]["filtro"] == {"tipo": "profissao"}
    assert nodes.INSTRUCAO_PERFIL not in falsos["chamadas"]


def test_curso_gratuito_filtra_por_orcamento(falsos):
    conversar(montar_grafo(), "Quero um curso gratuito, sou iniciante")

    assert falsos["buscas"][0]["filtro"] == {"$and": [{"tipo": "curso"}, {"gratuito": "true"}]}


def test_nao_pergunta_o_perfil_duas_vezes(falsos):
    grafo = montar_grafo()
    conversar(grafo, "Quero um curso")
    conversar(grafo, "tanto faz")

    estado = conversar(grafo, "Quero um roadmap")

    assert estado["resposta"].startswith("RESPOSTA:")


def test_conversas_diferentes_nao_misturam_o_perfil(falsos):
    grafo = montar_grafo()
    conversar(grafo, "Quero um roadmap, sou iniciante e prefiro gratuito", conversa="a")

    estado = conversar(grafo, "Qual o roadmap?", conversa="b")

    assert estado["aguardando_perfil"] is True
