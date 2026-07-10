def chunk_text(text):
    chunks=[]
    words=text.split()
    for i in range(0,len(text),450):
        chunk=" ".join(words[i:i+500])
        chunks.append(chunk)

    return chunks