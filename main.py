import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('HUGGING_FACE_API_KEY')

if not API_KEY:
    raise ValueError("HUGGING_FACE_API_KEY not found in environment. Please set it in the .env file.")

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

# Chunk the text
def chunk_text(text, chunk_size=100):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

#Embed the text chunks
def embed_text_chunks(text_chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_chunks)
    return embeddings

#start Faiss index and store embeddings
def store_embeddings_in_faiss(embeddings):
    try:
        d = embeddings.shape[1] 
        index = faiss.IndexFlatIP(d)  #(cosine similarity) search
        index.add(embeddings)
        print(f"Embeddings stored in Faiss index with dimension {d}")
        return index
    except Exception as e:
        print(f"Error storing embeddings in Faiss index: {e}")
        return None

# Generate response from query
def generate_response(query, index, text_chunks):
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([query])[0]
        print(f"Query Embedding: {query_embedding}\n")

        D, I = index.search(query_embedding.reshape(1, -1), 5)  # Search top 5
        print(f"Results: {I}\n")

        retrieved_texts = [text_chunks[i] for i in I[0]]
        context = ' '.join(retrieved_texts)
        print(f"Context: {context[:500]}...\n") 

        # making context for the Hugging Face API
        payload = {
            'inputs': f"{context}\n\n{query}",
            'max_length': 256
        }
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        response = requests.post('https://api-inference.huggingface.co/models/gpt2', headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            return result[0]['generated_text']
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return "An error occurred while generating the response."

    except Exception as e:
        print(f"Error generating response: {e}")
        return "An error occurred while querying or generating the response."

if __name__ == "__main__":
    pdf_path = 'sampleMedicalDataPDF.pdf'
    
    text = extract_text_from_pdf(pdf_path)
    if not text:
        print("No text extracted from PDF.")
    else:
        print(f"Extracted Text: {text[:100]}")  #print the first 100 characters
    
    text_chunks = chunk_text(text)
    print(f"First 3 Text Chunks: {text_chunks[:3]}")  
    
    embeddings = embed_text_chunks(text_chunks)
    print(f"First 3 Embeddings: {embeddings[:3]}")  
    
    index = store_embeddings_in_faiss(embeddings)
    
    if index is not None:
        query = "What are the effects of heart failure?"
        response = generate_response(query, index, text_chunks)
        print(f"Response: {response}")
