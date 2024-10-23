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


Here's the complete installation section for your GitHub README, formatted as requested:

markdown
Copy code
## Installation

Follow these steps to set up the project on your local machine:

### Clone the repository

```bash
git clone https://github.com/yourusername/pdf-query-bot.git
cd pdf-query-bot
Create a virtual environment


bash
Copy code
python -m venv venv
Activate the virtual environment:

On macOS and Linux:

bash
Copy code
source venv/bin/activate
On Windows:

bash
Copy code
venv\Scripts\activate
Install the dependencies
Once the virtual environment is activated, install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables
Create a .env file in the root directory of the project.

Add your Hugging Face API key to the .env file:

makefile
Copy code
HUGGING_FACE_API_KEY=your_hugging_face_api_key





