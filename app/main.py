from fastapi import FastAPI,UploadFile,File
from app.pdf_utils import extract_text
from app.chunking import chunk_text
from app.embeddings import create_embeddings
from app.retrieval import retrieve_chunks
from app.LLM import build_prompt,generate_answer
from app.models import QuestionRequest
import os
t=[]
app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"Ai Doc Search API"
        }

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join("uploads", "current.pdf")

    with open(filepath, "wb") as f:
        f.write(await file.read())

    text = extract_text("uploads/current.pdf")
    chunks=chunk_text(text)

    global t 
    t = create_embeddings(chunks)
    
    return "PDF Processed",len(t)
    
@app.post("/ask")
async def ask(question:QuestionRequest):
    best=retrieve_chunks(question.question,t)
    answer=generate_answer(question.question,best)

    return {
        "answer":answer.output_text
    }
