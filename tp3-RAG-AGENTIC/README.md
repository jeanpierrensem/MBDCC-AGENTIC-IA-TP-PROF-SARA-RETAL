#  TP 3 - RAG Agentic   : Prof SARA RETAL

## Prerequis communs
pour la bonne exécution de l'agent RAG, il faut installer les paquets suivants en utilisant le gestionnaire uv. 

``bash
    uv add langchain_community
    uv add pypdf 
    uv add langchain_text_splitters
    uv add sentence-transformers
``

## fonctionnalité implémentées
### Partie 1
- Chargement et extraction de contenu d’un fichier PDF avec LangChain (PyPDFLoader)
- Segmentation de texte pour préparation au RAG avec LangChain
- Transformation des chunks en vecteurs sémantiques avec un modèle Hugging Face : Génération d’embeddings textuels
- Création d’une base vectorielle en mémoire pour stockage et recherche d’embeddings
- Indexation des documents dans la base vectorielle pour recherche sémantique
- Recherche sémantique dans une base vectorielle pour retrouver les informations pertinentes
- création d'un Agent RAG

### Partie 2
- Connexion à une base de données SQL (SQLite) avec LangChain
- Création d’un tool personnalisé pour interroger une base SQL avec un agent
- Création d’un agent LLM pour interroger une base SQL
- Interrogation d’un agent SQL via langage naturel et récupération des résultats