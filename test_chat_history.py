from google import genai
from google.genai import types
from dotenv import dotenv_values
import asyncio

config = dotenv_values(".env")

chat_history_stoic = [
    types.Content(role="user", parts=[types.Part.from_text(text="Your are stoic philosopher , u know everything about stoicism , u have embody it ur whole like , u think like it, leadership like that and it has effect on every aspect of ur life, during this whole conversation i will show the hardship or life scenerio u have to tell me the solution accordingly")]), 
]
chat_history_islamic = [
    types.Content(role="user", parts=[types.Part.from_text(text="Your are islamic philosopher , u know everything about islam , u have embody it ur whole like , u think like it, leadership like that and it has effect on every aspect of ur life, during this whole conversation i will show the hardship or life scenerio u have to tell me the solution accordingly")]), 
]


client = genai.Client(api_key=config["AI_KEY"])

async def ask_Gemini(point_of_view):
    interaction = await client.aio.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents= chat_history_stoic if point_of_view == "stoic" else chat_history_islamic
)
    return interaction.text


async def Ai_engineering(prompt):
    chat_history_stoic.append(types.Content(role="user", parts=[types.Part.from_text(text=prompt)]))
    chat_history_islamic.append(types.Content(role="user", parts=[types.Part.from_text(text=prompt)]))
    task1= asyncio.create_task( ask_Gemini("stoic"))
    task2= asyncio.create_task( ask_Gemini("islamic"))
    
    response1 =  await task1
    chat_history_stoic.append(types.Content(role="model", parts=[types.Part.from_text(text=response1)]))

    print(response1)
    print("<<<<<<<<===========================================================>>>>>>>>>>")
    response2 = await task2
    chat_history_islamic.append(types.Content(role="model", parts=[types.Part.from_text(text=response2)]))
    print(response2)


async def main():
    while(True):
        prompt=input("Ask Ai: ")
        if prompt == "exit":
            break
        await Ai_engineering(prompt)

asyncio.run(main())