from typing import TypedDict


class EstadoMentor(TypedDict, total=False):
    mensagem: str
    pergunta: str
    historico: list
    nivel: str
    area_interesse: str
    orcamento: str
    aguardando_perfil: bool
    intencao: str
    chunks: list
    resposta: str
