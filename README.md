**Medical PDF Query Assistant using FAISS and GPT-2**

This project is a Medical PDF Query Assistant that extracts text from a PDF file, divides it into smaller chunks, generates embeddings for those chunks using a transformer model (all-MiniLM-L6-v2), stores the embeddings in a FAISS index, and allows users to query the PDF content. The bot uses the Hugging Face GPT-2 model to generate responses based on the most relevant context retrieved from the PDF.

Features

PDF Text Extraction
Text Chunking
Embedding Generation
FAISS Indexing 
Query-Answering

Requirements
Hugging Face API key (to use GPT-2 for generating responses)

