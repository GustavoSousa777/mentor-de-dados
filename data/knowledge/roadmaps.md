atualizado_em: outubro/2026

# Roadmaps de Carreira em Dados e IA

**Premissa de tempo deste documento:** as faixas de tempo assumem 10 a 15 horas de estudo por semana, para pessoa iniciante sem experiência na área. É uma estimativa do autor, não um dado das fontes. Com menos horas, as faixas se alongam. Itens marcados como "Recomendação" são interpretação do autor, não fato das fontes.

## Roadmap: Analista de Dados

<!-- tipo: roadmap | nivel: iniciante | area: analise -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Excel ou Google Sheets: tabelas dinâmicas, PROCV/XLOOKUP, fórmulas lógicas e de texto, formatação condicional, gráficos e limpeza básica de dados.
- SQL fundamental (PostgreSQL ou MySQL): SELECT, WHERE, GROUP BY, HAVING, INNER/LEFT/RIGHT JOIN, agregações e ordenação.
- Estatística descritiva: média, mediana, moda, variância, desvio padrão, percentis e distribuições elementares.
- Comunicação: transformar uma pergunta de negócio em análise e explicar conclusões de forma objetiva.
- O roadmap.sh de Data Analyst começa por Excel e pela noção de análise descritiva, diagnóstica, preditiva e prescritiva.
- Recomendação: resolver exercícios de SQL todos os dias (LeetCode, HackerRank) antes de partir para automação com código. Aprender SQL antes de Python, porque SQL aparece com mais frequência nas rotinas de análise.
- ⚠️ há divergência entre fontes sobre o momento ideal de introduzir Python/Pandas e funções de janela (algumas colocam na Etapa 1, outras na Etapa 2); vale testar e ajustar conforme seu ritmo

**Etapa 2 (3-6 meses): Ferramentas intermediárias**
- SQL intermediário: funções de janela (ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD), subqueries e CTEs.
- Ferramenta de BI: Power BI (DAX essencial, Power Query/M, modelagem Star Schema) ou Tableau (cálculos de tabela, campos calculados, dashboards interativos).
- Python para análise: Pandas para limpeza (duplicados, valores ausentes, outliers), NumPy, Matplotlib e Seaborn.
- Coleta de dados a partir de CSV, bancos de dados e APIs.
- Prática de séries temporais, segmentação, análise de tendências e definição de KPIs.
- Recomendação: dominar uma única ferramenta de BI (Power BI no ecossistema corporativo tradicional, Tableau em multinacionais) antes de aprender a outra.

**Etapa 3 (6-12 meses): Especialização e portfólio**
- EDA avançada e estatística inferencial: testes de hipóteses (teste A/B, t de Student, qui-quadrado), correlação vs. causalidade, intervalos de confiança.
- Storytelling com dados: comunicação de métricas, definição de KPIs, apresentação para público não técnico.
- Análise de ponta a ponta: entender o problema, obter e limpar os dados, analisar, validar, visualizar e recomendar com base em evidências.
- Git e GitHub para versionar scripts e relatórios em Jupyter Notebooks, com README de síntese executiva (ROI, retenção, eficiência operacional).
- Portfólio com contexto de negócio, pergunta definida, metodologia, resultados e limitações. Evitar projetos que sejam só notebooks com gráficos.
- Recomendação: escolher um setor (varejo, saúde, finanças) e manter nos projetos do portfólio.
- Deep learning e Spark aparecem como opcionais no roadmap.sh e não são necessários para a primeira vaga.

**Projeto prático sugerido:** análise exploratória e dashboard interativo no Power BI sobre taxa de cancelamento (churn), com consultas SQL usando CTEs e funções de janela e hipóteses de negócio testadas estatisticamente em um notebook Python.
Alternativa: analisar um dataset público de vendas ou e-commerce (por exemplo o Online Retail da UCI) com SQL e Pandas e entregar dashboard e relatório curto respondendo a três perguntas de negócio, com KPIs e limitações documentados.

## Roadmap: Cientista de Dados

<!-- tipo: roadmap | nivel: iniciante | area: ciencia -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Python: sintaxe intermediária, POO básica, estruturas de dados, funções, módulos, tratamento de erros, ambientes virtuais, NumPy, Pandas e SciPy.
- Matemática e estatística: álgebra linear, cálculo diferencial (derivadas e gradientes), probabilidade (Bayes, distribuições), amostragem, intervalos de confiança, testes de hipótese e conceitos básicos de experimentação.
- SQL para extração e união de bases (JOINs e agregações) e visualização com Matplotlib/Seaborn.
- O roadmap.sh de AI and Data Scientist coloca matemática e estatística como base antes de machine learning.
- Recomendação: não negligenciar a base matemática. Entender descida do gradiente e mecânica de matrizes ajuda a diagnosticar modelos ineficientes.
- ⚠️ há divergência entre fontes sobre a profundidade de matemática necessária nesta etapa (cálculo e álgebra linear completos vs. apenas o básico); o nível mais aprofundado é mais seguro para quem mira cargos de modelagem avançada

**Etapa 2 (3-6 meses): Machine learning**
- ML supervisionado e não supervisionado com Scikit-learn: regressão linear/logística, árvores, Random Forest, Gradient Boosting (XGBoost/LightGBM), K-Means e PCA.
- Validação: divisão treino/validação/teste, K-Fold cross-validation, overfitting, regularização, trade-off viés-variância.
- Métricas: acurácia, precisão, recall, F1, ROC-AUC, matriz de confusão; RMSE, MAE, R² para regressão.
- Feature engineering: nulos, One-Hot e Target Encoding, normalização/padronização, seleção de atributos. Pipelines reprodutíveis.
- EDA e visualização para guiar os primeiros modelos.
- Recomendação: dominar a avaliação correta de modelos (separação treino/teste, vazamento de dados) antes de testar algoritmos complexos. Usar SHAP para interpretar modelos caixa-preta desde os primeiros projetos.

**Etapa 3 (6-12 meses): Aprofundamento**
- Otimização de hiperparâmetros, desbalanceamento de classes, interpretabilidade, análise de erros e experimentos controlados.
- Noções de séries temporais.
- Especialização em uma direção (NLP, visão computacional, séries temporais ou ML aplicado a negócios), sem tentar dominar todas ao mesmo tempo.
- MLOps inicial: MLflow, Docker, APIs REST com FastAPI, versionamento de experimentos e monitoramento.
- Cloud: noções de AWS SageMaker, Google Cloud Vertex AI ou Azure Machine Learning.
- Deep learning (MLP, CNN, RNN/Transformers com PyTorch ou TensorFlow/Keras).
- Recomendação: priorizar projetos reprodutíveis de ponta a ponta em vez de precisão em competições sintéticas. Kaggle e projetos completos no GitHub podem compor o portfólio.
- ⚠️ há divergência entre fontes sobre se deep learning é item obrigatório desta etapa ou apenas opcional, e sobre o peso real do Kaggle num portfólio — trate ambos como complementares, não como pré-requisito para a primeira vaga

**Projeto prático sugerido:** pipeline de ML para predição de inadimplência com XGBoost, interpretabilidade com SHAP, tracking no MLflow e modelo empacotado como microsserviço REST em Docker com FastAPI.
Alternativa: prever churn com um dataset público (por exemplo Telco), com baseline, ao menos dois modelos, métrica justificada, análise de erros e notebook documentado com recomendações de negócio.

## Roadmap: Engenheiro de Dados

<!-- tipo: roadmap | nivel: iniciante | area: engenharia -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Python estruturado (scripts, arquivos, chamadas de API, POO), terminal Linux/Bash e Git/GitHub.
- SQL avançado e modelagem relacional com PostgreSQL: normalização (1FN a 3FN), índices, EXPLAIN, chaves primárias/estrangeiras, transações.
- Boas práticas de engenharia de software: Clean Code, PEP 8, testes com pytest, empacotamento de dependências.
- Docker para executar serviços de forma reproduzível; noções de redes e APIs.
- O Data Engineering Zoomcamp do DataTalks.Club abre com Docker, Postgres e infraestrutura como código, e informa que não exige experiência prévia em engenharia de dados.
- Recomendação: ganhar proficiência em Linux e shell script cedo, porque a maioria dos ambientes produtivos roda em Linux.

**Etapa 2 (3-6 meses): Pipelines e warehouse**
- Modelagem dimensional (Kimball): fatos e dimensões, Star Schema, Snowflake, Slowly Changing Dimensions.
- ETL/ELT, data warehouses e data lakes. Ingestão (por exemplo com a biblioteca dlt).
- Orquestração: Apache Airflow ou Mage.ai (DAGs, operadores, hooks, agendamento, reprocessamento e tratamento de falhas). O curso do DataTalks.Club usa Kestra; Airflow é alternativa amplamente usada.
- Docker (Dockerfile, docker-compose) e fundamentos de Cloud Storage/IAM (AWS S3, Google Cloud Storage, Azure Blob Storage).
- Formatos como Parquet, particionamento, clusterização, cargas incrementais, qualidade de dados. O curso usa Google Cloud Storage e BigQuery.
- Recomendação: construir pipelines locais orquestrados por Airflow em Docker antes de migrar para nuvem paga. Escolher um único provedor de nuvem (GCP, AWS ou Azure) e aprofundar nele.
- ⚠️ há divergência entre fontes sobre quando introduzir Spark e Kafka (Etapa 2 ou Etapa 3); priorize dominar pipelines e orquestração antes de avançar para processamento distribuído

**Etapa 3 (6-12 meses): Produção**
- Apache Spark (PySpark): arquitetura de clusters, otimização de memória e partição.
- Modern Data Stack: Snowflake, BigQuery ou Redshift; Delta Lake, Apache Iceberg ou Parquet. Transformação com dbt.
- Streaming básico com Kafka ou AWS Kinesis.
- Terraform em nível introdutório. Testes e monitoramento de pipelines, IAM, segurança, observabilidade, lineage, performance e controle de custos na nuvem.
- Objetivo: deixar de construir apenas scripts de ETL e passar a construir sistemas de dados reproduzíveis e operáveis.
- Recomendação: entender a teoria de computação distribuída e partição de dados em Spark para evitar gargalos e custos excessivos na nuvem.

**Projeto prático sugerido:** pipeline ELT que extrai dados públicos via API, orquestra a ingestão com Airflow em Docker, guarda dados brutos em Data Lake (Parquet) e processa agregações no BigQuery/Snowflake com modelagem Kimball.
Alternativa: ingerir em lote um dataset público (por exemplo corridas de táxi de NYC), carregar num warehouse em nuvem, transformar com dbt e alimentar um dashboard, com orquestração agendada, testes, monitoramento básico e documentação no GitHub.

## Roadmap: Analytics Engineer

<!-- tipo: roadmap | nivel: iniciante | area: engenharia -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- SQL profundo: CTEs complexas, funções de janela, funções analíticas, subqueries e otimização de custo de processamento.
- Git/GitHub (branches, pull requests, code review) e Python auxiliar.
- Modelagem dimensional (Kimball): fatos, dimensões conformadas, granularidade, cardinalidade, normalização e desnormalização.
- O Analytics Engineer atua entre engenharia de dados e análise, e SQL é a habilidade central do cargo.
- Recomendação: dominar a sintaxe SQL de data warehouses modernos (ANSI, Snowflake, BigQuery), com foco em legibilidade e eficiência.

**Etapa 2 (3-6 meses): dbt e warehouse**
- dbt: modelos, sources, seeds, snapshots, jinja, macros, materializações (view, table, incremental) e documentação automática.
- Qualidade: testes nativos (unique, not_null, accepted_values, relationships), dbt-expectations e contratos de dados básicos.
- Diferença entre ETL e ELT. Data warehouse em nuvem (Snowflake, BigQuery ou Redshift) conectado a uma ferramenta de BI.
- O módulo de Analytics Engineering do Data Engineering Zoomcamp organiza o trabalho em camadas staging, intermediate e marts, com testes e documentação.
- Recomendação: separar rigidamente Staging (limpeza e renomeação), Intermediate (regras de negócio) e Marts (fatos e dimensões para consumo).

**Etapa 3 (6-12 meses): Práticas de produção**
- CI/CD com GitHub Actions (testes automáticos em PR) e agendamento com dbt Cloud ou Airflow.
- Camada semântica e métricas padronizadas (dbt Semantic Layer, Cube, Lightdash) e catalogação de metadados.
- Modelos incrementais, performance e custo, lineage, observabilidade e contratos de dados entre equipes.
- Reverse ETL (Census, Hightouch).
- Recomendação: manter documentação viva no repositório dbt, com descrição de cada coluna. A certificação dbt Fundamentals pode servir como validação, sem ser tratada como requisito, pois a exigência varia por empresa.

**Projeto prático sugerido:** camada de transformação com dbt Core e Snowflake sobre dados de e-commerce, com modelos incrementais, testes de integridade via GitHub Actions e Marts documentados.
Alternativa: projeto dbt sobre dataset público com staging, intermediate e marts, ao menos 15 testes de dados, documentação gerada, dashboard consumindo os marts e README explicando as decisões de modelagem.

## Roadmap: Machine Learning Engineer

<!-- tipo: roadmap | nivel: iniciante | area: ia -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Engenharia de software com Python: padrões de projeto, tipagem (mypy), testes unitários e de integração (pytest), empacotamento, Git/GitHub.
- Algoritmos e estruturas de dados: Big-O, árvores, tabelas hash, filas.
- Fundamentos de ML com Scikit-learn: supervisionado e não supervisionado, ensembles, validação, overfitting, feature engineering, métricas.
- Separar código de treinamento, dados, configuração e inferência. SQL, APIs HTTP e Docker básicos.
- O MLOps Zoomcamp do DataTalks.Club lista Python, Docker, linha de comando e conhecimento de ML como pré-requisitos.
- Recomendação: escrever código limpo, modular e desacoplado desde o início. O trabalho de MLE exige mais qualidade de engenharia de software do que notebooks experimentais.

**Etapa 2 (3-6 meses): Modelos como serviços**
- Deep learning com PyTorch (CUDA, DataLoaders) ou TensorFlow conforme o domínio.
- APIs de inferência com FastAPI, validação com Pydantic, imagens Docker e testes automatizados.
- Rastreamento e registro de modelos com MLflow ou Weights & Biases (métricas, parâmetros, artefatos, Model Registry). Pipelines de treino, versionamento de dados e modelos, noções de CI/CD.
- Fundamentos de cloud para execução, armazenamento e serving de modelos.
- Recomendação: usar Docker multi-stage build para reduzir o tamanho das imagens de produção. Fazer o Machine Learning Zoomcamp (cerca de 16 semanas, foco em deploy) antes de entrar em MLOps, porque MLOps pressupõe que você já treinou modelos.

**Etapa 3 (6-12 meses): MLOps e operação**
- Pipelines de MLOps: Kubeflow Pipelines, ZenML ou Airflow, e versionamento de dados com DVC. Treinamento recorrente.
- Monitoramento de data drift e concept/model drift com Evidently AI ou Whylogs, com alertas, observabilidade, rollback e estratégias de deployment.
- Inferência batch vs. online, com análise de custo, latência, disponibilidade e escalabilidade.
- Inferência otimizada: quantização, ONNX, TensorRT, Triton Inference Server, Kubernetes.
- A certificação Google Cloud Professional Machine Learning Engineer cobre enquadrar problemas de ML, arquitetar soluções, desenvolver e escalar modelos, automatizar pipelines e monitorar. É descrita como voltada a profissionais com experiência, então é meta de médio prazo.
- Objetivo: demonstrar que o modelo pode ser executado, testado, monitorado e atualizado de forma confiável.
- Recomendação: priorizar o monitoramento contínuo, pois o ciclo de vida de um modelo começa após o primeiro deploy.
- ⚠️ há divergência entre fontes sobre o peso de Kubernetes nesta etapa (ferramenta central vs. apenas conceito introdutório); trate como algo a aprofundar conforme a necessidade do projeto, não como pré-requisito bloqueante

**Projeto prático sugerido:** pipeline de MLOps com DVC para dados, ZenML para orquestrar o treino, MLflow para logging e API de inferência em Docker monitorada contra drift com Evidently AI.
Versão reduzida: treinar um modelo de classificação, servi-lo por API em contêiner com testes automatizados, registrar experimentos e adicionar monitoramento básico de qualidade das previsões, com pipeline de retreino documentado.

## Roadmap: AI Engineer

<!-- tipo: roadmap | nivel: iniciante | area: ia -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Python ou TypeScript: código assíncrono, streams, HTTP/REST, JSON, Git, testes, linha de comando e Docker básico.
- LLMs: arquitetura Transformer básica (encoder/decoder, attention), tokens, janela de contexto, temperatura, embeddings, function/tool calling e limites dos modelos.
- Engenharia de prompts (few-shot, Chain-of-Thought, ReAct, system prompts) como parte de uma disciplina maior de desenvolvimento de aplicações.
- APIs de provedores (OpenAI, Anthropic Claude, Google Gemini). SQL e recuperação de dados, pois aplicações de IA consultam sistemas externos.
- O LLM Zoomcamp do DataTalks.Club exige conforto com programação e Python e não exige experiência prévia em IA ou ML.
- Recomendação: aprender saídas estruturadas (Structured Outputs, JSON Mode, Pydantic) direto pelas APIs antes de adotar frameworks complexos.

**Etapa 2 (3-6 meses): Aplicações com LLM**
- RAG: chunking, embeddings, busca vetorial (Chroma, Qdrant, Pinecone ou pgvector), busca textual (Elasticsearch ou similar), reranking e avaliação de respostas.
- Function calling e tool use ligando o modelo a bancos de dados, APIs e interpretadores de código.
- Frameworks de orquestração e agentes (LangChain, LangGraph, LlamaIndex, Semantic Kernel) e interface simples com Streamlit.
- Controle de custos, latência, erros e contexto. Conjuntos de avaliação para comparar mudanças de prompts, modelos e estratégias de recuperação.
- O LLM Zoomcamp cobre RAG, busca e saída estruturada em cerca de 10 semanas.
- Recomendação: entender os trade-offs entre modelos de embedding e estratégias de chunking antes de RAG avançado. Construir primeiro um fluxo fixo (workflow) antes de qualquer agente autônomo, e usar padrões simples antes de frameworks complexos.

**Etapa 3 (6-12 meses): Produção**
- RAG avançado: reranking com cross-encoders, busca híbrida (densa + BM25), Contextual Retrieval, roteamento semântico, estratégias multimodais.
- Avaliação e observabilidade: traces, latência e custos com Langfuse, Arize Phoenix ou LangSmith; Ragas e TruLens; LLM-as-a-judge; monitoramento com feedback de usuários.
- Guardrails, controle de acesso, segurança, prompt injection, proteção de dados e gestão de contexto.
- Workflows e agentes: padrões de workflow (encadeamento, roteamento, paralelização, orquestrador e trabalhadores, avaliador e otimizador) e critério para escolher entre workflow determinístico e agente. Explorar Agents SDK ou MCP somente depois de dominar APIs, ferramentas, contexto, avaliação e controle de estado.
- Fine-tuning de modelos abertos (Llama, Mistral) com PEFT/LoRA/QLoRA e Hugging Face, com serving via vLLM ou Ollama.
- O guia "Building effective agents" da Anthropic recomenda começar pela solução mais simples e só aumentar a complexidade quando houver necessidade comprovada.
- Recomendação: nunca lançar uma aplicação com LLM em produção sem suíte automatizada de avaliações (fidelidade, relevância, alucinações).

**Projeto prático sugerido:** RAG avançado sobre base documental regulatória, com busca híbrida (BM25 + Qdrant), reranking, fluxo agêntico em LangGraph e tracing de latência, tokens e fidelidade com Langfuse.
Versão com avaliação: assistente de perguntas e respostas sobre uma base própria, com RAG, respostas estruturadas, ao menos 30 perguntas de avaliação, métricas de qualidade da recuperação, comparação antes e depois de mudanças e painel simples de monitoramento.

## Roadmap: BI Analyst

<!-- tipo: roadmap | nivel: iniciante | area: bi -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- Métricas de negócio e KPIs: receita (CAC, LTV, MRR), eficiência operacional, funil de marketing, margens. Diferença entre métrica, indicador, dimensão e medida.
- SQL essencial para relatórios (filtros, agregações, JOINs) e Excel avançado (análise ad-hoc, conciliação, cenários).
- Estatística descritiva e princípios de visualização (escolha do gráfico, clareza, indicadores).
- Escolher uma ferramenta principal de BI, como Power BI, e aprender interface, conexão com fontes e relatórios básicos.
- Identificar KPIs com stakeholders é parte central do cargo.
- Recomendação: entender as dores e a linguagem dos decisores (C-Level, gerentes comerciais e operacionais), pois o sucesso de BI está no impacto do dado no negócio.

**Etapa 2 (3-6 meses): Ferramenta e modelagem**
- Power BI (DAX para inteligência temporal e medidas dinâmicas, Power Query, modelos semânticos) ou Tableau (LOD Expressions, parâmetros, dashboard actions).
- Modelagem dimensional em Star Schema: fatos, dimensões, granularidade, boas práticas de performance.
- Design de dashboards: teoria das cores, carga cognitiva, hierarquia visual, consumo executivo. Dashboards orientados a perguntas de negócio, não coleções de gráficos.
- A certificação Microsoft PL-300 organiza o conteúdo em preparar dados, modelar dados, visualizar e analisar, e gerenciar e proteger o Power BI.
- Recomendação: priorizar modelagem e DAX, pois o conteúdo oficial trata a modelagem como núcleo do Power BI. Evitar visualizações decorativas e preferir linhas, barras e matrizes limpas.

**Etapa 3 (6-12 meses): BI corporativo**
- Governança de self-service BI: permissões, Row-Level Security (RLS), workspaces, atualização agendada, distribuição de relatórios.
- Conexão direta a Snowflake, BigQuery ou Databricks sem degradar a performance. SQL intermediário (funções de janela), noções de data warehouse e semantic layer.
- Otimização de modelos, documentação e definição padronizada de métricas.
- Alertas de anomalias em KPIs e entrega automatizada por e-mail ou Slack.
- Recursos de IA integrados às plataformas de BI, sempre com validação humana de dados, métricas e consultas.
- Recomendação: manter RLS implementada nos modelos do portfólio. Avaliar prestar o PL-300 ao final da etapa e confirmar os objetivos vigentes na página oficial antes de agendar, pois a Microsoft atualiza o exame periodicamente.

**Projeto prático sugerido:** painel executivo de performance comercial em Power BI sobre banco dimensional, com medidas DAX de inteligência temporal (YoY, MoM), RLS por regional e glossário de métricas.
Versão com critérios: dashboard de vendas ou financeiro com múltiplas fontes tratadas no Power Query, modelo estrela, ao menos cinco medidas DAX, RLS por região, página de resumo executivo, capturas de tela e documentação do modelo.

## Roadmap: Data Governance Specialist

<!-- tipo: roadmap | nivel: iniciante | area: governanca -->

Premissa: faixas de tempo assumem 10 a 15 h/semana (estimativa). Itens "Recomendação" são interpretação do autor.

**Etapa 1 (0-3 meses): Fundamentos**
- DAMA-DMBOK: o DMBOK organiza a gestão de dados em 11 áreas de conhecimento, com governança de dados no centro (qualidade, metadados, arquitetura, segurança).
- Conceitos de dados: tipos, ciclo de vida, dados estruturados e não estruturados. Ownership, stewardship, catálogo, metadados, classificação, qualidade, segurança, privacidade, acesso e lineage.
- Dimensões de qualidade: precisão, completude, consistência, atualidade, validade e unicidade.
- LGPD (Lei 13.709/2018) e GDPR: dados pessoais, bases legais, direitos do titular, DPIA/RIPD.
- Bancos de dados e SQL para dicionários de dados e inspeção de integridade.
- Recomendação: estudar as diretrizes oficiais da ANPD para ver como a teoria de privacidade vira exigência de auditoria técnica.

**Etapa 2 (3-6 meses): Processos e ferramentas**
- Catálogos e linhagem: DataHub, Apache Atlas, OpenMetadata, Microsoft Purview, Alation, Google Cloud Dataplex.
- Qualidade de dados: perfilamento, regras e métricas, com Great Expectations ou Soda.
- Inventários de dados, glossários de negócio, responsáveis pelos ativos (data owner e steward), dados mestres, políticas e padrões.
- Classificação e acesso: mascaramento (anonymization/pseudonymization), RBAC, IAM e conformidade em trânsito e repouso.
- Recomendação: começar por qualidade de dados e metadados, as áreas mais práticas e fáceis de demonstrar em portfólio. Usar Great Expectations (código aberto) antes de suítes corporativas proprietárias.

**Etapa 3 (6-12 meses): Governança ativa**
- Lineage ponta a ponta e governança ativa, incluindo impacto de mudanças de schema.
- Contratos de dados entre produtores e consumidores.
- Políticas de retenção, acesso baseado em propósito, auditoria, gestão de mudanças e indicadores de governança. Maturidade de gestão de dados e implantação de programa de governança (estratégia, escopo, indicadores).
- Governança de IA e ética de dados: mitigação de viés, auditoria de dados de treinamento de LLMs, ISO/IEC 42001 e EU AI Act. Riscos de dados sensíveis em RAG, embeddings, logs e agentes.
- Relação da governança com Data Engineering, Analytics, MLOps e aplicações de IA. Traduzir políticas em processos técnicos verificáveis e mensuráveis.
- A certificação CDMP, da DAMA International, é baseada no DMBOK.
- Recomendação: construir diretrizes para evitar vazamento de segredos corporativos em ferramentas de IA generativa. Tratar este cargo como de entrada mais difícil que os demais: ele exige convivência com áreas de negócio e jurídico, e um caminho comum é começar em análise de dados ou qualidade de dados e migrar para governança.

**Projeto prático sugerido:** programa de governança para um pipeline analítico, com catálogo e linhagem no OpenMetadata, validações de qualidade com Great Expectations e manual de adequação LGPD/GDPR com matriz de acesso RBAC.
Alternativa: modelo de governança para um dataset público ou organização fictícia, com inventário, classificação de dados sensíveis, owners e stewards, glossário, dicionário de dados, regras de qualidade medidas com SQL ou Python, política de acesso e mapa de lineage.

## Fontes

**Plataformas de roadmap e portfólio:**
- roadmap.sh: Data Analyst Roadmap (https://roadmap.sh/data-analyst e PDF), AI and Data Scientist Roadmap (PDF), Data Engineer, AI Engineer e MLOps Roadmaps, índice geral (https://roadmap.sh/) e páginas de projetos por cargo (ex: https://roadmap.sh/data-analyst/projects).
- DataTalks.Club: Data Engineering Zoomcamp (currículo: https://datatalks.club/docs/courses/data-engineering-zoomcamp/curriculum/), Machine Learning Zoomcamp, MLOps Zoomcamp, LLM Zoomcamp (https://datatalks.club/blog/llm-zoomcamp.html), lista de cursos (https://datatalks.club/docs/courses) e Podcast Wiki (Data Roles Guide, Business Intelligence, Data Engineering Tools, Governance, Self-Service Data Platforms).

**Documentação de big techs e laboratórios de IA:**
- OpenAI Developers: API Documentation, Agents, Evaluate Agent Workflows, Structured Model Outputs.
- Anthropic: "Building Effective Agents" (https://www.anthropic.com/research/building-effective-agents), eBook "Building Effective AI Agents" (https://resources.anthropic.com/building-effective-ai-agents), Effective Context Engineering for AI Agents, Demystifying Evals for AI Agents, Writing Effective Tools for AI Agents.
- Google for Developers / Google Cloud: Machine Learning Crash Course, Production ML Systems, Generative AI on Vertex AI, Evaluation of Generative AI Agents, What is Data Governance?
- Microsoft Learn: Power BI Data Analyst Associate / PL-300 (https://learn.microsoft.com/certifications/resources/study-guides/pl-300), learning paths de preparo, modelagem e uso de DAX em Power BI, Microsoft Purview Data Governance e Data Lineage.
- AWS e Google Cloud Architecture Centers: guias de Modern Data Architecture, Data Warehousing e MLOps produtivo.

**Certificações e frameworks técnicos:**
- Google Cloud Professional Machine Learning Engineer — conteúdo baseado no guia oficial de estudo (Sybex/Wiley).
- DAMA International, DMBOK e certificação CDMP (https://cdmp.info, https://dama.org/), consultados também via materiais secundários (Snowflake, Atlan).
- dbt Labs Developer Guides e amostra de vagas da dbt Labs para o cargo de Analytics Engineer.
- Hugging Face: documentação de orquestração de LLMs abertos, fine-tuning (PEFT/LoRA) e avaliação de modelos.

**Observações sobre as fontes:**
- Não foram obtidas páginas primárias da OpenAI nem do Google especificamente sobre trilhas de carreira; o conteúdo de certificação do Google Cloud vem do guia de estudo oficial, não da documentação de carreira em si.
- A referência a requisitos de vaga de mercado se apoia numa amostra pequena (dbt Labs), sem levantamento estatístico mais amplo.
- A LGPD foi referenciada por conhecimento geral, não a partir de consulta direta ao texto da lei.
- As faixas de tempo de cada etapa assumem 10 a 15 horas de estudo por semana para quem está começando do zero — é uma estimativa, não um dado de nenhuma fonte, e tende a se alongar com menos horas disponíveis.
- Itens marcados como "Recomendação" são interpretação do curador do documento, não um fato relatado pelas fontes.
- A nomenclatura de algumas ferramentas (ex: "Google Cloud Dataplex") muda com frequência e deve ser reconfirmada na documentação oficial antes de publicar.
