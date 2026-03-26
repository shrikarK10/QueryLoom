import time
import ollama
from backend.utils.config import MODEL_NAME
start_time = time.time()
response = ollama.chat(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "What is full form of WIFI?"}],
)

end_time = time.time()
print(f"Response time: {end_time - start_time} seconds")

print(f"\nResponse: {response.message.content}")