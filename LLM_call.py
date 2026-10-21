
from google import genai
from dotenv import dotenv_values

config = dotenv_values(".env")


# print(config["AI_KEY"])

client = genai.Client(api_key=config["AI_KEY"])

interaction = client.interactions.create(
    model="gemini-2.5-flash",
    input="My name is Muhammad huzefa javed and i see myself higher i made standered for my self , inspire by the histories great warriors and leaders and empirer , stoicisim is my favourite phylosiphy , my inspiraton includes, david giggins , Muhammad Ali , mike tyson and khabib from today eras , but from past like alexendar the great , hanibaal barca , marcus arelies for his philophy , slahudin and knight and warrior , honorable mentoin like khalid ibn waleed , and every one who lead with purpose , ambition by example , who face his fears and stand tall againsat them , "
)

print(interaction.output_text)
