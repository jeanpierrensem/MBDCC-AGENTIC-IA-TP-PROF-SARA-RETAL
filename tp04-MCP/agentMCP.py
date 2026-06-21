import asyncio # utilisation des E/S en mode asynchrone, non bloquant
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient # pour avoir accès au protocole
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from dotenv.ipython import load_dotenv

load_dotenv(override=True)

async def main():
    client = MultiServerMCPClient(
        {
        "local_server": {
            "transport": "stdio",
            "command": "python",
            "args": ["resources/mcp_local_server.py"],
            }
        }
   )
    #récuoération dynamique des tools
    tools = await client.get_tools()
    # récupération dynamique des resources
    resources = await client.get_resources()
    #récupération dynamique des prompts
    prompt = await client.get_prompt("local_server", "prompt")
    prompt = prompt[0].content


    # Agent LLM modulaire avec serveur MCP local (tools, resources et prompts dynamiques)

    # Initialiser le modèle Ollama
    model = ChatOllama(
    model="llama3.2", # ou mistral, gemma, etc.
    temperature=0
    )
    agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=prompt
    )
    config = {"configurable": {"thread_id": "1"}}
    response = await agent.ainvoke( {"messages": [HumanMessage(content="Tell me about the langchain-mcp-adapt-ers library")]},
                                   config=config
                                   )
    print(response)

asyncio.run(main())


