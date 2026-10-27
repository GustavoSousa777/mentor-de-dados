from pydantic import BaseModel, Field


class PedidoChat(BaseModel):
    mensagem: str = Field(min_length=1, max_length=1000)
    id_conversa: str = Field(min_length=1, max_length=100)


class RespostaChat(BaseModel):
    resposta: str
    intencao: str
