from langchain_core.tools import tool

@tool
def ensure_json_format(content: str):
    \"\"\"Validates and formats content as JSON.\"\"\"
    import json
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {str(e)}"
