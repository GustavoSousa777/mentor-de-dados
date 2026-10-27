from functools import lru_cache

PASTA_BANCO_VETORIAL = "chroma_db"
NOME_COLECAO = "mentor_de_dados"
MODELO_EMBEDDING = "paraphrase-multilingual-MiniLM-L12-v2"


@lru_cache(maxsize=1)
def carregar_colecao():
    import chromadb

    cliente = chromadb.PersistentClient(path=PASTA_BANCO_VETORIAL)
    return cliente.get_collection(NOME_COLECAO)


@lru_cache(maxsize=1)
def carregar_modelo():
    from sentence_transformers import SentenceTransformer

    return SentenceTransformer(MODELO_EMBEDDING)


def buscar_chunks(pergunta, quantidade=10, filtro=None):
    colecao = carregar_colecao()
    modelo = carregar_modelo()

    vetor_pergunta = modelo.encode([pergunta]).tolist()

    resultado = colecao.query(
        query_embeddings=vetor_pergunta,
        n_results=quantidade,
        where=filtro,
    )

    textos = resultado["documents"][0]
    metadados = resultado["metadatas"][0]

    return list(zip(textos, metadados))


def main():
    pergunta = input("Pergunta: ")
    chunks_encontrados = buscar_chunks(pergunta, filtro={"tipo": "roadmap"})

    for texto, metadados in chunks_encontrados:
        print("\n---")
        print(metadados)
        print(texto[:300])


if __name__ == "__main__":
    main()
