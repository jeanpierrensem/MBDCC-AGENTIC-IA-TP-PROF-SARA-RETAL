#PARTIE 2 : Agent LLM avec outil MCP de temps (time
#server) pour interrogation de l’heure en zone
#spécifique

#Configuration et initialisation d’un client MCP pour un serveur de temps avec gestion de timezone

import asyncio
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama

async def main():
    client = MultiServerMCPClient(
        {
            "time": {
            "transport": "stdio",
            "command": "uvx",
                "args": [
                "mcp-server-time",
                "--local-timezone=America/New_York"
                ]
            }
        }
    )

    # Récupération dynamique des tools :  get tools
    tools = await client.get_tools()

    #Création et exécution d’un agent LLM avec outils MCP pour la consultation du temps local

    # Initialiser le modèle Ollama
    model = ChatOllama(
    model="llama3.2", # ou mistral, gemma, etc.
    )
    agent = create_agent(
    model=model,
    tools=tools,
    )
    question = HumanMessage(content="What time is it in Japan")
    response = await agent.ainvoke(
    {"messages": [question]}

    )
    print(response['messages'][-1].content)

asyncio.run(main())