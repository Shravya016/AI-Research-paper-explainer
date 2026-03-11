from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GROKAI_API_KEY')
from pypdf import PdfReader
reader=PdfReader("2603.09599v1.pdf")
from langchain.text_splitter import RecursiveCharacterTextSplitter
def extract_text_from_pdf(reader):
    # should open the pdf and retuurn the full text as a string
    text=""
    for page in reader.pages:
        text+=page.extract_text() or ""
    return text

text=extract_text_from_pdf(reader)
def split_text_into_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_text(text)
    return chunks
    
    # should recursively return the chunks of the text
chunks = split_text_into_chunks(text)

print(f"Total chunks: {len(chunks)}")
print("=" * 50)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk)
    print("=" * 50)