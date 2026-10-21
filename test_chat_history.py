from google import genai
from google.genai import types
from dotenv import dotenv_values

config = dotenv_values(".env")

chat_history = [
    types.Content(role="user", parts=[types.Part.from_text(text="My code word is Alpha-9.")]),
    types.Content(role="model", parts=[types.Part.from_text(text="Understood, your code word is Alpha-9.")]),
    types.Content(role="user", parts=[types.Part.from_text(text="What is my code word?")])
]


client = genai.Client(api_key=config["AI_KEY"])

interaction = client.models.generate_content(
    model="gemini-2.5-flash",
   contents=chat_history
)

print(interaction.text)
