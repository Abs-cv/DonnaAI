import os
from dotenv import load_dotenv

def load_env_variables():
    \"\"\"Loads environment variables from a .env file.\"\"\"
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("OPENAI_API_KEY is not set in the environment.")
