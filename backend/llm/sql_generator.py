import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
LOG_FILE = Path(__file__).resolve().parent / "generated_query_log.txt"

def generate_sql(question: str, schema: dict):
    prompt = f"""
You are an expert SQL generator.

STRICT RULES:
- Only return SQL query
- Do not explain anything
- Use only given schema

Schema:
{schema}

Question:
{question}

SQL:
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen:7b",
            "prompt": prompt,
            "stream": False
        }
    )

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"Prompt:\n{prompt}\n")
        log_file.write(f"Response:\n{response.json()['response'].strip()}\n")
        log_file.write("-" * 50 + "\n")
    
    return response.json()["response"].strip()