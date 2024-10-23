Medical PDF Query Assistant using FAISS and GPT-2

This project is a Medical PDF Query Assistant that extracts text from a PDF file, divides it into smaller chunks, generates embeddings for those chunks using a transformer model (all-MiniLM-L6-v2), stores the embeddings in a FAISS index, and allows users to query the PDF content. The bot uses the Hugging Face GPT-2 model to generate responses based on the most relevant context retrieved from the PDF.

Features
PDF Text Extraction: Extracts text from PDF documents using PyPDF2.
Text Chunking: Splits the extracted text into smaller, manageable chunks.
Embedding Generation: Uses SentenceTransformer to generate embeddings for each text chunk.
FAISS Indexing: Embeddings are stored in a FAISS index for efficient retrieval of relevant text chunks.
Query-Answering: Uses GPT-2 (via Hugging Face API) to generate a response based on the most relevant text chunks retrieved from the FAISS index.

Requirements
Hugging Face API key (to use GPT-2 for generating responses)

