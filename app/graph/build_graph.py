from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph

from app.graph.edges import decidir_proximo_passo
from app.graph.nodes import (
    classificar_intencao,
    extrair_perfil,
    perguntar_perfil,
    recuperar_contexto,
    responder,
)
from app.graph.state import EstadoMentor


def montar_grafo():
    grafo = StateGraph(EstadoMentor)

    grafo.add_node("classificar_intencao", classificar_intencao)
    grafo.add_node("extrair_perfil", extrair_perfil)
    grafo.add_node("perguntar_perfil", perguntar_perfil)
    grafo.add_node("recuperar_contexto", recuperar_contexto)
    grafo.add_node("responder", responder)

    grafo.add_edge(START, "classificar_intencao")
    grafo.add_edge("classificar_intencao", "extrair_perfil")
    grafo.add_conditional_edges(
        "extrair_perfil",
        decidir_proximo_passo,
        ["perguntar_perfil", "recuperar_contexto"],
    )
    grafo.add_edge("perguntar_perfil", END)
    grafo.add_edge("recuperar_contexto", "responder")
    grafo.add_edge("responder", END)

    return grafo.compile(checkpointer=MemorySaver())


def main():
    grafo = montar_grafo()
    configuracao = {"configurable": {"thread_id": "teste"}}

    while True:
        mensagem = input("\nVocê: ")
        if mensagem.strip().lower() == "sair":
            break

        estado = grafo.invoke({"mensagem": mensagem}, configuracao)
        print(f"\n[intenção: {estado['intencao']} | nível: {estado.get('nivel')} | orçamento: {estado.get('orcamento')}]")
        print(f"\nMentor: {estado['resposta']}")


if __name__ == "__main__":
    main()
