from langchain_core.tools import tool

@tool
def python_repl(code: str):
    \"\"\"Executes Python code and returns the output.\"\"\"
    try:
        exec_globals = {}
        exec(code, exec_globals)
        return exec_globals
    except Exception as e:
        return f"Error executing code: {str(e)}"
