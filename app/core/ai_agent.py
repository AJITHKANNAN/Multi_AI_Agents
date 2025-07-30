from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
import langgraph
from langgraph.prebuilt import create_react_agent
 #type:ignore
from langchain_core.messages.ai import AIMessage #used to find which msgs written from user and AI

from app.config.settings import settings

def get_response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []  # max_results = top 2 results fetched

    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state = {"messages" : query} # used for conversation history that is a list of messages

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]
    # used to fetch only message from AI
    # (message,AIMessage) --> this means only get message feom AIMessage 

    return ai_messages[-1] # latest reply