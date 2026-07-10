from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
def create_embedding(text):
    return model.encode(text)

def create_embeddings(chunks):
    embeddings=[]
    for chunk in chunks:
        embedding=create_embedding(chunk)
        embeddings.append({
            "text":chunk,
            "embedding":embedding
        })
    return embeddings
