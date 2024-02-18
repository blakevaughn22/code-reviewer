import os
from openai import OpenAI
client = OpenAI()

with open("src/testcode.py") as f:
    data = f.read()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are about to recieve some python code, please explain what it does."},
    {"role": "user", "content": data}
  ]
)

print(response.choices[0].message.content)