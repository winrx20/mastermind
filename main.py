import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://gateway.ngrok.ai",
    api_key=os.environ["AI_GATEWAY_API_KEY"],
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)