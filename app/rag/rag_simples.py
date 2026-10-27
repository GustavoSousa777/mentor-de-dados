from app.llm.client import gerar_resposta
from app.rag.retriever import buscar_chunks

INSTRUCAO_SISTEMA = """Você é o Mentor de Dados, um orientador de carreira para iniciantes na área de dados e inteligência artificial.

Responda sempre em português do Brasil, de forma clara e direta.
Use apenas as informações do contexto fornecido.
Se o contexto não tiver a informação pedida, diga que não tem essa informação na base.
Não invente cursos, links, preços ou salários.
Quando o contexto trouxer "[VERIFICAR ...]", avise que esse dado precisa ser conferido na fonte oficial."""


def montar_contexto(chunks):
    textos = [texto for texto, _ in chunks]
    return "\n\n---\n\n".join(textos)


def responder(pergunta, filtro=None):
    chunks = buscar_chunks(pergunta, quantidade=5, filtro=filtro)
    contexto = montar_contexto(chunks)
    mensagem = f"Contexto:\n{contexto}\n\nPergunta: {pergunta}"
    return gerar_resposta(INSTRUCAO_SISTEMA, mensagem)


def main():
    pergunta = input("Pergunta: ")
    print(responder(pergunta, filtro={"tipo": "roadmap"}))


if __name__ == "__main__":
    main()
