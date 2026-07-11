from google import genai
from dotenv import load_dotenv
from os import getenv

load_dotenv()
api_key=getenv("GEMINI_API")
if api_key is None:
    raise ValueError("API MISSING")

client=genai.Client(api_key=api_key)

def build_prompt(question,best_chunks):
    context="\n\n".join(best_chunks)
    prompt=f"""
    You are a helpful assistant that answers questions using the provided context.

    Instructions:
    - Use only the information in the context.
    - If the answer is not present in the context, say that the information is not available.
    - Do not make up facts.

    Context:
    {context}
    
    Question:
    {question}

    Answer: 
    """
    return prompt

def generate_answer (prompt):
    interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
    
)
    return interaction