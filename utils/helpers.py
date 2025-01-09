def extract_imports(code):
    \"\"\"Extracts import statements from the code.\"\"\"
    import re
    return re.findall(r'^import (.+)$', code, re.MULTILINE)
