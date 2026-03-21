import time
import ollama
start_time = time.time()
response = ollama.chat(
    model="qwen2.5:7b-instruct-q4_K_M",
    messages=[{"role": "user", "content": "What is transformer architecture?"}],
)

end_time = time.time()
print(f"Response time: {end_time - start_time} seconds")

print(f"\nResponse: {response.message.content}")