def router(state):
    \"\"\"Determines the next step in the workflow.\"\"\"
    messages = state["messages"]
    last_message = messages[-1]
    if "FINAL ANSWER" in last_message.content:
        return "__end__"
    return "continue"
