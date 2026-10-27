from fastapi.testclient import TestClient

from app.api import routes_chat
from app.main import app

cliente = TestClient(app)


def test_health():
    resposta = cliente.get("/health")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_chat_pergunta_o_perfil_antes_de_responder(falsos):
    resposta = cliente.post("/chat", json={"mensagem": "Qual o roadmap?", "id_conversa": "api-1"})

    assert resposta.status_code == 200
    assert resposta.json()["intencao"] == "roadmap"
    assert "nível" in resposta.json()["resposta"]


def test_chat_mantem_a_conversa_pelo_id(falsos):
    cliente.post("/chat", json={"mensagem": "Qual o roadmap?", "id_conversa": "api-2"})

    resposta = cliente.post(
        "/chat",
        json={"mensagem": "sou iniciante, quero gratuito, engenharia de IA", "id_conversa": "api-2"},
    )

    assert resposta.status_code == 200
    assert resposta.json()["resposta"].startswith("RESPOSTA:")


def test_chat_recusa_mensagem_vazia():
    resposta = cliente.post("/chat", json={"mensagem": "", "id_conversa": "api-3"})

    assert resposta.status_code == 422


def test_chat_recusa_pedido_sem_id_da_conversa():
    resposta = cliente.post("/chat", json={"mensagem": "Oi"})

    assert resposta.status_code == 422


def test_chat_devolve_503_quando_o_grafo_falha(monkeypatch):
    class GrafoQuebrado:
        def invoke(self, *args, **kwargs):
            raise RuntimeError("falha simulada")

    monkeypatch.setattr(routes_chat, "grafo", GrafoQuebrado())

    resposta = cliente.post("/chat", json={"mensagem": "Oi", "id_conversa": "api-4"})

    assert resposta.status_code == 503
    assert "tente novamente" in resposta.json()["detail"].lower()
