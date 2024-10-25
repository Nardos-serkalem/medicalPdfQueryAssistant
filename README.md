# Medical PDF Text Extraction and Query Response System

This project extracts text from a PDF document, processes it into chunks, generates embeddings using a pre-trained model, and stores these embeddings in a FAISS index for efficient retrieval. The system allows users to query information related to the extracted text and receive generated responses using the Hugging Face API.

## Features

- Extracts text from PDF files.
- Splits extracted text into manageable chunks.
- Generates embeddings for each text chunk using Sentence Transformers.
- Stores embeddings in a FAISS index for fast similarity searches.
- Queries the stored embeddings and generates a response based on the retrieved context using the Hugging Face API.

## Requirements
- Libraries:
  - `PyPDF2`
  - `sentence-transformers`
  - `faiss-cpu` 
  - `requests`
  - `python-dotenv`
 




