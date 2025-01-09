from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def create_data_analysis_agent(tools):
    \"\"\"Creates the data analysis agent.\"\"\"
    system_message = (
        "You are a data analysis agent. Your job is to analyze datasets for duplicates and calculate statistics."
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="messages"),
    ])
    return prompt.bind_tools(tools)
