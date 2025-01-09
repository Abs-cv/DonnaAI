from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_reporting_agent(tools):
    \"\"\"Creates the reporting agent.\"\"\"
    system_message = (
        "You are a reporting agent. Your job is to generate a JSON report based on findings from other agents."
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="messages"),
    ])
    return prompt.bind_tools(tools)
