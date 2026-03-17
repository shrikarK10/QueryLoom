import time
import ollama
start_time = time.time()
response = ollama.chat(
    model="qwen:7b",
    messages=[{"role": "user", "content": "hi, how are you?"}]
)

end_time = time.time()
print(f"Response time: {end_time - start_time} seconds")

print(f"\nResponse: {response.message.content}")