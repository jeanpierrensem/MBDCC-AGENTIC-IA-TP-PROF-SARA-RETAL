#  MBDCC SEMESTRE 2 - AGENTIC IA  : Prof SARA RETAL

Ce repositry centralise les TP du cours  **IA Agentic** dispensé par le professeur **SARA RETAL**.



| Dossier | Sujet |
|---|---|
| [tp1-Ingenierie-prompts](./venv/tp1-Ingenierie-prompts) | Ingenierie des prompts (tokenisation, Ollama, Groq, OpenAI, JSON, images) |
| [tp2-Agents-Langchain](./tp2-Agents-Langchain) | Agents avec LangChain (agent chef personnel, memoire, web search) |
| [tp3-RAG-AGENTIC](./Lab3-RAG) | RAG sur PDF (HuggingFace embeddings) + agent SQL (Chinook DB) |
| [tp4-MCP](./Lab4-MCP) | Model Context Protocol : stdio, serveur de temps, HTTP streaming |
| [tp5-LangGraph-Studio](./Lab5-LangGraph_Studio) | LangGraph Studio (visualisation/debug d'agents) + systeme Multi-Agents hierarchique |
| [tp6-Contexte-Etat](./Lab6-Contexte_et_Etat) | Contexte par invocation (`ReaderProfile`) et etat persiste (`LibraryState`) |
| [tp7-Human-In-The-Loup](./Lab7-Human_In_The_Loop) | Agent HITL : interrupt(), approve / reject / edit |
| [tp8-Workflow-avec-LangGraph](./Lab8-Workflow_avec_LangGraph) | Workflows LangGraph : graphe simple, reducers, etat message, branchements conditionnels, boucles |
| [tp9-Agent-avec-LangGraph](./Lab9-Agent_avec_LangGraph) | Agent LangGraph : tools, agent comme noeud, HITL fonctionnel (`@entrypoint`/`@task`), historique et fork |
| [tp-chef-personnel](./TP-Chef_personnel) | Agent chef cuisinier : RAG + memoire + recherche web + system prompt |

## Prerequis communs

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/) — gestionnaire de paquets
- [Ollama](https://ollama.com/) avec le modele `llama3.2:3b`

```bash
ollama pull llama3.2:3b
```

## Execution

Chaque lab est autonome avec son propre environnement virtuel :

```bash
cd Lab6-Contexte_et_Etat
uv sync
uv run --active python agent_context.py
uv run --active python agent_state.py
```

## Remarques

- Les fichiers `.env` ne doivent pas etre pushes sur GitHub (voir `.env.example` dans chaque lab).
- Certains labs demandent des cles API optionnelles (`TAVILY_API_KEY`, `LANGSMITH_API_KEY`).
