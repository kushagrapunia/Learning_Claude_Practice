import re
import json
import yaml
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()
stored_messages = []
system_prompt = '''
You are a helpful assistant named Claude. You will answer the user's questions and engage in a conversation with them. 
You will provide accurate and concise information, and you will be friendly and polite in your responses. 
'''
print("Chat with Claude! Say 'done' when you want to end the conversation.\n")
param = {
    "model": "claude-haiku-4-5",
    "max_tokens": 1024,
    "messages": stored_messages,
    "system": system_prompt
    }


while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if "done" in user_input.lower():
        print("Goodbye!")
        break

    stored_messages.append({"role": "user", "content": user_input})

    response = client.messages.create(**param)

    assistant_reply = response.content[0].text
    stored_messages.append({"role": "assistant", "content": assistant_reply})

    print(f"Claude: {assistant_reply}\n")