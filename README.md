# Mentor de Dados

Um mentor de carreira para quem quer entrar na área de dados. A pessoa conta em que nível está (iniciante, intermediário...) e se prefere conteúdo gratuito, pago ou tanto faz, e o mentor responde com roadmaps, cursos e certificações que fazem sentido para esse perfil.

O projeto está **em desenvolvimento**. Este README mostra o que já funciona, o que falta e como pretendo deixar tudo no final, para que quem abrir o repositório agora entenda em que ponto ele está.

## Por que fiz isso

Quem começa em dados costuma se perder entre dezenas de trilhas, cursos e certificações, quase sempre com conselhos genéricos. Quis fazer algo mais direto: um assistente que não responde só com o que o modelo "sabe", mas busca em uma base de conhecimento que eu mesmo montei e curei, e que faz as perguntas certas antes de recomendar qualquer coisa.

Também é um projeto de portfólio. A ideia é praticar o ciclo completo de uma aplicação com LLM: base de conhecimento, busca vetorial, fluxo de conversa, API, testes, CI, avaliação e deploy.

## Como funciona

Em vez de um RAG que busca e responde a qualquer mensagem, usei um fluxo guiado:

1. A mensagem chega pela API com um `id_conversa`.
2. Um nó classifica a intenção (por exemplo, pedir um roadmap, perguntar sobre uma profissão, tirar uma dúvida do FAQ).
3. Se faltar informação, como o nível ou a preferência entre gratuito e pago, o mentor pergunta antes de responder.
4. Com o perfil completo, o sistema busca no ChromaDB os trechos mais parecidos com o pedido.
5. O Gemini gera a resposta usando só esse contexto.

O estado de cada conversa (a "ficha" do mentor) fica separado por `id_conversa`, então duas conversas diferentes não se misturam.

## Stack

| Parte | Tecnologia |
|---|---|
| Geração de respostas | Gemini |
| Banco vetorial | ChromaDB |
| Embeddings | `paraphrase-multilingual-MiniLM-L12-v2` (sentence-transformers), com troca para a API do Gemini em avaliação |
| Fluxo da conversa | LangGraph |
| API | FastAPI |
| Testes | pytest |
| CI | GitHub Actions |
| Frontend (planejado) | React + Vite |
| Deploy (planejado) | Docker |

## Base de conhecimento

São seis arquivos Markdown em `data/knowledge/`, divididos em 93 chunks pelo script de ingestão:

- `profissoes.md`
- `roadmaps.md`
- `cursos_gratuitos.md`
- `cursos_pagos.md`
- `certificacoes.md`
- `faq.md`

## Estrutura do projeto

Esta é a estrutura que pretendo ter na versão final. O que ainda não existe está listado na seção de status.

```
mentor-de-dados/
├── .github/workflows/ci.yml
├── app/
│   ├── main.py
│   ├── api/routes_chat.py
│   ├── schemas/chat.py
│   ├── graph/
│   │   ├── state.py
│   │   ├── nodes.py
│   │   ├── edges.py
│   │   └── build_graph.py
│   ├── llm/client.py
│   └── rag/
│       ├── ingest.py
│       └── retriever.py
├── data/knowledge/
├── eval/
├── frontend/
├── notebooks/
├── tests/
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

Cada camada só conhece a de baixo: a API chama o grafo, o grafo chama o `rag` e o `llm`, e nenhuma delas fala direto com o frontend. O arquivo `rag_simples.py`, que usei só para validar a busca com o Gemini, vai sair ou virar teste quando o grafo estiver completo.

## Status

### Já feito

- [x] Base de conhecimento com os seis arquivos e 93 chunks
- [x] Ingestão (`ingest.py`): lê os `.md`, gera os vetores e salva no ChromaDB
- [x] Busca (`retriever.py`): recupera os chunks mais parecidos, com o modelo de embedding carregado uma única vez (`lru_cache`)
- [x] Cliente do Gemini (`client.py`)
- [x] Estado da conversa (`state.py`)
- [x] Nós, arestas e montagem do grafo no LangGraph
- [x] API com `POST /chat` e `GET /health`
- [x] 34 testes passando com pytest
- [x] Workflow de CI no GitHub Actions

### Em andamento

- [ ] Teste manual do `/chat` com o Gemini real pela página `/docs`
- [ ] Decisão sobre o embedding (ver abaixo)

### Falta fazer

- [ ] **Avaliação da busca (passo 16):** cerca de 20 perguntas, cada uma com o chunk que deveria ser recuperado, e uma métrica de recuperação
- [ ] **Comparar os embeddings:** medir o modelo local como baseline, trocar para o do Gemini, recriar o banco e medir de novo
- [ ] **Dockerfile:** rodar `python -m app.rag.ingest` durante o build para a imagem já levar o `chroma_db/` pronto
- [ ] **Deploy**, depois de medir o consumo real de memória
- [ ] **Frontend** em React + Vite (passo 15)
- [ ] `requirements.txt`, `.env.example` e este README com os resultados finais

## Decisão em aberto: embedding local ou API do Gemini

O `sentence-transformers` traz o PyTorch junto, e minha estimativa é que a aplicação passe de 512 MB de RAM, o que complica hospedagem em planos pequenos. Ainda não medi, então é uma hipótese. Isso me levou a considerar trocar para o `gemini-embedding-001`.

Prós da troca:

- A imagem Docker fica bem menor e cabe em planos mais baratos.
- O app já depende do Gemini para gerar respostas, então não nasce uma dependência nova.
- O modelo local provavelmente corta textos longos, e a API aceita entradas maiores.

Cuidados:

- Cada pergunta passa a gastar uma chamada de embedding, e a cota gratuita é limitada.
- Textos da base e perguntas usam tipos de tarefa diferentes na API (`RETRIEVAL_DOCUMENT` e `RETRIEVAL_QUERY`).
- Trocar de modelo muda a ordem dos resultados, então é preciso recriar o banco e refazer a avaliação.
- `ingest.py` e `retriever.py` precisam sempre usar o mesmo modelo.

Não vou decidir no palpite. Pretendo rodar a mesma avaliação nos dois modelos, comparar a recuperação e só então escolher. Quando terminar, vou registrar os números aqui.

## Como rodar

Todos os comandos partem da raiz do projeto.

```bash
git clone <url-do-repositorio>
cd mentor-de-dados

python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com a chave do Gemini:

```
GEMINI_API_KEY=sua_chave_aqui
```

Gere o banco vetorial e suba a API:

```bash
python -m app.rag.ingest
uvicorn app.main:app --reload
```

A documentação interativa fica em `http://127.0.0.1:8000/docs`. Exemplo de requisição:

```json
{"mensagem": "Qual o roadmap?", "id_conversa": "teste1"}
```

Como ainda não sei o nível da pessoa, o mentor deve perguntar o nível e a preferência entre cursos gratuitos, pagos ou tanto faz. Depois de uma resposta como "sou iniciante, quero gratuito, engenharia de IA", ele devolve o roadmap correspondente.

Para rodar os testes:

```bash
pytest
```

> O `requirements.txt` ainda não existe. Até eu criá-lo, as dependências principais são `fastapi`, `uvicorn`, `langgraph`, `chromadb`, `sentence-transformers`, `python-dotenv`, o SDK do Gemini e `pytest`.

## Como quero deixar o projeto no final

- Aplicação publicada, com uma demo que qualquer pessoa consiga abrir
- Frontend simples de chat em React
- Imagem Docker que já sobe com o banco vetorial pronto
- Avaliação da busca documentada, com os números do modelo local e do Gemini lado a lado
- Testes e CI rodando a cada push
- README com a decisão de embedding explicada e os resultados medidos, não só estimados

## Limitações conhecidas

- A base de conhecimento é pequena (93 chunks) e escrita por mim, então não cobre todas as áreas de dados.
- Cursos e certificações mudam de preço e de disponibilidade. As informações da base precisam de revisão periódica.
- O mentor só deve recomendar o que está na base. Perguntas fora dela podem ter respostas fracas.

## Licença

A definir.
