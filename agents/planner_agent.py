from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

def create_planner_agent(tools):
    """Creates the planner agent with a defined prompt."""
    system_message = (
        "You are a planner agent. Your job is to create a detailed pipeline for analyzing datasets."
        " Include pseudo code and specify dependencies among tasks."
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="messages"),
    ])
    return prompt.bind_tools(tools)
