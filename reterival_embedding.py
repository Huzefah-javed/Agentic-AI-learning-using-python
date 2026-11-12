from pypdf import PdfReader
from google import genai
from google.genai import types
from dotenv import dotenv_values
import json

config = dotenv_values(".env")
client = genai.Client(api_key=config["AI_KEY"])

reader = PdfReader("a.pdf")

dataList = []

for p, page in enumerate(reader.pages):
    page_content = page.extract_text().split(".")
    for i, cur_sentence in enumerate(page_content):
        if i < len(page_content) - 3:
            dict ={
                "chunkId": f"a.pdf-page{p+1}-chunk{i+1}",
                "content": f"{page_content[i]}. {page_content[i+1]}. {page_content[i+2]}",
                "metadata": {
                        "source_file": "a.pdf",
                        "page_number": p+1,
                        "chunk_index": i+1,
                        "char_count": len(page_content[i])+len(page_content[i+1]) +len(page_content[i+2])
                     }
            }
            dataList.append(dict)


texts_to_embed = [chunk["content"] for chunk in dataList]

result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts_to_embed,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT", 
            output_dimensionality=1536     
            )
        )

for chunk, embedding_obj in zip(dataList, result.embeddings):
        chunk["embedding"] = embedding_obj.values


file_name = "vector_store.json"

with open(file_name, "w", encoding="utf-8") as f:
    json.dump(dataList, f, indent=4, ensure_ascii=False)

print(f"Successfully saved {len(dataList)} chunks to '{file_name}'!")


print(f"Total chunks embedded: {len(dataList)}")
print(f"Vector dimensions: {len(dataList[0]['embedding'])}") # Should print 768
print(f"First 5 numbers: {dataList[0]['embedding'][:5]}")