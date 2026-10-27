from app.graph.nodes import INTENCOES_COM_PERFIL, faltam_dados


def decidir_proximo_passo(estado):
    if estado["intencao"] in INTENCOES_COM_PERFIL and faltam_dados(estado):
        return "perguntar_perfil"
    return "recuperar_contexto"
