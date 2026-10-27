from app.graph import nodes


def test_normalizar_intencao_aceita_intencao_valida():
    assert nodes.normalizar_intencao("  Roadmap \n") == "roadmap"


def test_normalizar_intencao_usa_padrao_quando_invalida():
    assert nodes.normalizar_intencao("não sei") == nodes.INTENCAO_PADRAO


def test_ler_json_com_cerca_de_codigo():
    assert nodes.ler_json('```json\n{"nivel": "iniciante"}\n```') == {"nivel": "iniciante"}


def test_ler_json_invalido_devolve_vazio():
    assert nodes.ler_json("isto não é json") == {}
    assert nodes.ler_json("[1, 2]") == {}


def test_faltam_dados():
    assert nodes.faltam_dados({})
    assert nodes.faltam_dados({"nivel": "iniciante"})
    assert not nodes.faltam_dados({"nivel": "iniciante", "orcamento": "ambos"})


def test_filtro_usa_o_tipo_da_intencao():
    assert nodes.montar_filtro({"intencao": "faq"}) == {"tipo": "faq"}


def test_filtro_de_curso_gratuito():
    filtro = nodes.montar_filtro({"intencao": "curso", "orcamento": "gratuito"})
    assert filtro == {"$and": [{"tipo": "curso"}, {"gratuito": "true"}]}


def test_filtro_de_curso_pago():
    filtro = nodes.montar_filtro({"intencao": "curso", "orcamento": "pago"})
    assert filtro == {"$and": [{"tipo": "curso"}, {"gratuito": "false"}]}


def test_filtro_de_curso_ambos_so_usa_o_tipo():
    assert nodes.montar_filtro({"intencao": "curso", "orcamento": "ambos"}) == {"tipo": "curso"}


def test_consulta_inclui_a_area_so_para_roadmap_e_curso():
    estado = {"pergunta": "Qual o roadmap?", "area_interesse": "engenharia de IA"}

    assert nodes.montar_consulta({**estado, "intencao": "roadmap"}) == "Qual o roadmap? engenharia de IA"
    assert nodes.montar_consulta({**estado, "intencao": "profissao"}) == "Qual o roadmap?"


def test_classificar_intencao_guarda_a_pergunta(falsos):
    resultado = nodes.classificar_intencao({"mensagem": "Qual o roadmap?"})

    assert resultado == {"intencao": "roadmap", "pergunta": "Qual o roadmap?"}


def test_classificar_intencao_nao_reclassifica_enquanto_aguarda_perfil(falsos):
    resultado = nodes.classificar_intencao({"mensagem": "sou iniciante", "aguardando_perfil": True})

    assert resultado == {}
    assert falsos["chamadas"] == []


def test_extrair_perfil_ignora_intencoes_sem_perfil(falsos):
    resultado = nodes.extrair_perfil({"intencao": "profissao", "mensagem": "Quanto ganha?"})

    assert resultado == {}
    assert falsos["chamadas"] == []


def test_extrair_perfil_le_os_campos(falsos):
    estado = {"intencao": "roadmap", "mensagem": "sou iniciante, quero gratuito e engenharia de IA"}

    assert nodes.extrair_perfil(estado) == {
        "nivel": "iniciante",
        "orcamento": "gratuito",
        "area_interesse": "engenharia de IA",
        "aguardando_perfil": False,
    }


def test_extrair_perfil_assume_padroes_depois_de_perguntar(falsos):
    estado = {"intencao": "roadmap", "aguardando_perfil": True, "mensagem": "não sei"}

    assert nodes.extrair_perfil(estado) == {
        "nivel": nodes.NIVEL_PADRAO,
        "orcamento": nodes.ORCAMENTO_PADRAO,
        "aguardando_perfil": False,
    }


def test_extrair_perfil_mantem_o_que_ja_era_conhecido(falsos):
    estado = {"intencao": "curso", "nivel": "avancado", "mensagem": "quero gratuito"}

    resultado = nodes.extrair_perfil(estado)

    assert resultado["nivel"] == "avancado"
    assert resultado["orcamento"] == "gratuito"


def test_perguntar_perfil_pergunta_so_o_que_falta():
    estado = {"mensagem": "Qual o roadmap?"}

    pergunta_completa = nodes.perguntar_perfil(estado)["resposta"]
    pergunta_orcamento = nodes.perguntar_perfil({**estado, "nivel": "iniciante"})["resposta"]

    assert "nível" in pergunta_completa and "gratuitos" in pergunta_completa
    assert "nível" not in pergunta_orcamento and "gratuitos" in pergunta_orcamento


def test_perguntar_perfil_marca_que_aguarda_e_registra_historico():
    resultado = nodes.perguntar_perfil({"mensagem": "Qual o roadmap?"})

    assert resultado["aguardando_perfil"] is True
    assert [item["papel"] for item in resultado["historico"]] == ["usuario", "mentor"]


def test_recuperar_contexto_repete_a_busca_sem_filtro_quando_vazio(monkeypatch):
    buscas = []

    def buscar_falso(pergunta, quantidade=10, filtro=None):
        buscas.append(filtro)
        return [] if filtro else [("chunk", {})]

    monkeypatch.setattr(nodes, "buscar_chunks", buscar_falso)

    resultado = nodes.recuperar_contexto({"pergunta": "Qual o roadmap?", "intencao": "roadmap"})

    assert buscas == [{"tipo": "roadmap"}, None]
    assert resultado == {"chunks": [("chunk", {})]}


def test_responder_inclui_perfil_para_roadmap(falsos):
    estado = {
        "mensagem": "sou iniciante",
        "pergunta": "Qual o roadmap?",
        "intencao": "roadmap",
        "nivel": "iniciante",
        "chunks": [("chunk de teste", {})],
    }

    resultado = nodes.responder(estado)

    assert "Perfil da pessoa: nível iniciante" in resultado["resposta"]
    assert "Pergunta: Qual o roadmap?" in resultado["resposta"]
    assert "chunk de teste" in resultado["resposta"]
    assert len(resultado["historico"]) == 2


def test_responder_nao_inclui_perfil_para_profissao(falsos):
    estado = {
        "mensagem": "Quanto ganha?",
        "pergunta": "Quanto ganha?",
        "intencao": "profissao",
        "nivel": "iniciante",
        "chunks": [("chunk de teste", {})],
    }

    assert "Perfil da pessoa" not in nodes.responder(estado)["resposta"]
