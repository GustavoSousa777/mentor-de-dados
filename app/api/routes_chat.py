import logging

from fastapi import APIRouter, HTTPException

from app.graph.build_graph import montar_grafo
from app.schemas.chat import PedidoChat, RespostaChat

logger = logging.getLogger(__name__)

router = APIRouter()
grafo = montar_grafo()


@router.get("/health")
def verificar_saude():
    return {"status": "ok"}


@router.post("/chat", response_model=RespostaChat)
def conversar(pedido: PedidoChat):
    configuracao = {"configurable": {"thread_id": pedido.id_conversa}}

    try:
        estado = grafo.invoke({"mensagem": pedido.mensagem}, configuracao)
    except Exception:
        logger.exception("Erro ao processar a mensagem")
        raise HTTPException(
            status_code=503,
            detail="O mentor não conseguiu responder agora. Tente novamente em instantes.",
        )

    return RespostaChat(resposta=estado["resposta"], intencao=estado["intencao"])
