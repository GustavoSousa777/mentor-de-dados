import re
from pathlib import Path
 
import chromadb
from sentence_transformers import SentenceTransformer
 
PASTA_CONHECIMENTO = Path("data/knowledge")
PASTA_BANCO_VETORIAL = "chroma_db"
NOME_COLECAO = "mentor_de_dados"
MODELO_EMBEDDING = "paraphrase-multilingual-MiniLM-L12-v2"
 
PADRAO_METADADOS = re.compile(r"<!--\s*(.*?)\s*-->")
PADRAO_SECAO = re.compile(r"^## (.+)$", re.MULTILINE)
 
 
def ler_metadados(texto_metadados):
    metadados = {}
    for campo in texto_metadados.split("|"):
        chave, valor = campo.split(":", 1)
        metadados[chave.strip()] = valor.strip()
    return metadados
 
 
def dividir_em_secoes(conteudo):
    titulos = list(PADRAO_SECAO.finditer(conteudo))
    secoes = []
 
    for indice, titulo in enumerate(titulos):
        inicio = titulo.end()
        fim = titulos[indice + 1].start() if indice + 1 < len(titulos) else len(conteudo)
        corpo = conteudo[inicio:fim].strip()
 
        busca_metadados = PADRAO_METADADOS.search(corpo)
        metadados = ler_metadados(busca_metadados.group(1)) if busca_metadados else {}
        corpo_sem_metadados = PADRAO_METADADOS.sub("", corpo).strip()
        nome = titulo.group(1).strip()
        texto = f"{nome}\n{corpo_sem_metadados}"
        metadados["titulo"] = nome
 
        secoes.append({"texto": texto, "metadados": metadados})
 
    return secoes
 
 
def carregar_secoes(arquivo):
    conteudo = arquivo.read_text(encoding="utf-8")
    secoes = dividir_em_secoes(conteudo)
 
    for secao in secoes:
        secao["metadados"]["arquivo"] = arquivo.stem
 
    return secoes
 
 
def carregar_todas_as_secoes():
    secoes = []
    for arquivo in sorted(PASTA_CONHECIMENTO.glob("*.md")):
        secoes += carregar_secoes(arquivo)
    return secoes
 
 
def recriar_colecao(cliente):
    colecoes_existentes = [colecao.name for colecao in cliente.list_collections()]
    if NOME_COLECAO in colecoes_existentes:
        cliente.delete_collection(NOME_COLECAO)
    return cliente.create_collection(NOME_COLECAO)
 
 
def salvar_secoes_no_banco(secoes):
    cliente = chromadb.PersistentClient(path=PASTA_BANCO_VETORIAL)
    colecao = recriar_colecao(cliente)
 
    modelo = SentenceTransformer(MODELO_EMBEDDING)
    textos = [secao["texto"] for secao in secoes]
    embeddings = modelo.encode(textos).tolist()
 
    colecao.add(
        ids=[f"chunk_{i}" for i in range(len(secoes))],
        documents=textos,
        embeddings=embeddings,
        metadatas=[secao["metadados"] for secao in secoes],
    )
 
 
def main():
    secoes = carregar_todas_as_secoes()
    print(f"{len(secoes)} chunks encontrados em {PASTA_CONHECIMENTO}")
 
    salvar_secoes_no_banco(secoes)
    print(f"Chunks salvos em '{PASTA_BANCO_VETORIAL}' na coleção '{NOME_COLECAO}'")
 
 
if __name__ == "__main__":
    main()
 





















