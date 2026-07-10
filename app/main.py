from fastapi import FastAPI,UploadFile,File
from app.pdf_utils import extract_text
from app.chunking import chunk_text
from app.embeddings import create_embedding
from sentence_transformers import util
import os

app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"Ai Doc Search API"
        }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join("uploads", file.filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    return {
        "message": "Upload successful",
        "filename": file.filename
    }       

@app.get("/test")
def test():
    text = extract_text("uploads/thinkpython2.pdf")
    chunks=chunk_text(text)
    
    return { 
        "num_chunks":len(chunks),
        "first_chunk":chunks[0]
    }

@app.get("/embedding-test")
def embedding_test():

    sentence1 = "A cat is sleeping on the sofa."
    sentence2 = "A kitten is resting on the couch."
    sentence3 = "Python dictionaries store key value pairs."

    e1 = create_embedding(sentence1)
    e2 = create_embedding(sentence2)
    e3 = create_embedding(sentence3)

    cvk=util.cos_sim(e1,e2).item()
    cvp=util.cos_sim(e1,e3).item()

    return {
        "cvk":cvk,
        "cvp":cvp
    }

    