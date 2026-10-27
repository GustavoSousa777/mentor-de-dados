import json

import pytest

from app.graph import nodes


@pytest.fixture
def falsos(monkeypatch):
    registro = {"buscas": [], "chamadas": []}

    def gerar_falso(instrucao, mensagem):
        registro["chamadas"].append(instrucao)
        texto = mensagem.lower()

        if instrucao == nodes.INSTRUCAO_CLASSIFICACAO:
            if "roadmap" in texto:
                return "roadmap"
            if "curso" in texto:
                return "curso"
            if "ganha" in texto:
                return "profissao"
            return "faq"

        if instrucao == nodes.INSTRUCAO_PERFIL:
            orcamento = None
            if "gratuito" in texto:
                orcamento = "gratuito"
            elif "tanto faz" in texto:
                orcamento = "ambos"

            return json.dumps(
                {
                    "nivel": "iniciante" if "iniciante" in texto else None,
                    "area_interesse": "engenharia de IA" if "engenharia de ia" in texto else None,
                    "orcamento": orcamento,
                }
            )

        return f"RESPOSTA: {mensagem}"

    def buscar_falso(pergunta, quantidade=10, filtro=None):
        registro["buscas"].append({"pergunta": pergunta, "filtro": filtro})
        return [("chunk de teste", {})]

    monkeypatch.setattr(nodes, "gerar_resposta", gerar_falso)
    monkeypatch.setattr(nodes, "buscar_chunks", buscar_falso)
    return registro
