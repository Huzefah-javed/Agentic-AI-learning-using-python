from pypdf import PdfReader

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

for i in dataList[:3]:
    print(i)
