from sentence_transformers import SentenceTransformer,util
model=SentenceTransformer("all-MiniLM-L6-v2")
def create_embedding(text):
    return model.encode(text)
