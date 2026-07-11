from app.embeddings import create_embedding
from sentence_transformers import util
def retrieve_chunks(question,stored_embeddings):
    question_embedding=create_embedding(question)
    
    similarity_list=[]
    
    best_chunks=[]
    
    for item in stored_embeddings:
        stored_embedding=item["embedding"]
        similarity=util.cos_sim(question_embedding,stored_embedding).item()
        similarity_list.append((similarity,item["text"]))
    
    similarity_list.sort(key=lambda item: item[0],reverse=True)
    for item in similarity_list[:3]:
        best_chunks.append(item[1])
        


    return best_chunks
