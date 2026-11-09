from google import genai
from google.genai import types
from dotenv import dotenv_values
from pydantic import BaseModel, Field
from typing import Annotated
import asyncio
import logging

logging.basicConfig(filename="chatbot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("google").setLevel(logging.WARNING)

config = dotenv_values(".env")

chat_history_stoic = [
    types.Content(role="user", parts=[types.Part.from_text(text="Your are stoic philosopher , u know everything about stoicism , u have embody it ur whole like , u think like it, leadership like that and it has effect on every aspect of ur life, during this whole conversation i will show the hardship or life scenerio u have to tell me the solution accordingly")]), 
]
chat_history_islamic = [
    types.Content(role="user", parts=[types.Part.from_text(text="Your are islamic philosopher , u know everything about islam , u have embody it ur whole like , u think like it, leadership like that and it has effect on every aspect of ur life, during this whole conversation i will show the hardship or life scenerio u have to tell me the solution accordingly")]), 
]


class TopicAnalysis(BaseModel):
    title: Annotated[str ,Field(description="The core title of the topic")]
    key_takeaways: Annotated[list[str] , Field(description="Exactly 3 bullet points summarizing the concept")]
    difficulty_score: Annotated[int, Field(description="A score from 1 to 10 rating the complexity")]


client = genai.Client(api_key=config["AI_KEY"])

async def ask_Gemini(point_of_view):
    token_check = client.models.count_tokens(
        model="gemini-3.5-flash-lite",
        contents=chat_history_stoic if point_of_view == "stoic" else chat_history_islamic,
    )

    logging.info(f"Input::::your token for {point_of_view} is {token_check.total_tokens}")
    interaction=""
    try:
        interaction = await client.aio.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents= chat_history_stoic if point_of_view == "stoic" else chat_history_islamic,
        config={
            "response_mime_type": "application/json",
            "response_schema": TopicAnalysis,
        },
     )
    except Exception as e:
        print(f"API call failed: {e}")
    finally:
        logging.info(f"Output::::::token consumption {point_of_view} {interaction.usage_metadata.total_token_count}")
    return interaction.parsed


async def Ai_engineering(prompt):
    chat_history_stoic.append(types.Content(role="user", parts=[types.Part.from_text(text=prompt)]))
    chat_history_islamic.append(types.Content(role="user", parts=[types.Part.from_text(text=prompt)]))
    task1= asyncio.create_task( ask_Gemini("stoic"))
    task2= asyncio.create_task( ask_Gemini("islamic"))
    
    response1 =  await task1
    text1=""
    for res in response1.model_dump()["key_takeaways"]:
        text1+=res
    chat_history_stoic.append(types.Content(role="model", parts=[types.Part.from_text(text=text1)]))
    print(text1)    

    print("<<<<<<<<===========================================================>>>>>>>>>>")
    response2 = await task2
    text2=""
    for res in response2.model_dump()["key_takeaways"]:
        text2+=res
    chat_history_islamic.append(types.Content(role="model", parts=[types.Part.from_text(text=text2)]))
    print(text2)    
    


async def main():
    while(True):
        prompt=input("Ask Ai: ")
        if prompt == "exit":
            break
        await Ai_engineering(prompt)

asyncio.run(main())