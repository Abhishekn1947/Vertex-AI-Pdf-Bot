import os
from google.cloud import aiplatform
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_vertexai import VertexAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
import streamlit as st
from typing import List

# Correctly setting environment variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path to your GCP Cred.json"
project_id = "GCP ID"

# Initialize Vertex AI
aiplatform.init(project=project_id, location="your GCP Zone")


# Mock Embeddings Class Implementation
class MockEmbeddings:
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[0.1] * 768 for _ in texts]

    def embed_query(self, text: str) -> List[float]:
        return [0.1] * 768


# Instantiate the embeddings object
embeddings = MockEmbeddings()

# Streamlit UI setup
st.set_page_config(page_title="Mr.DOC", page_icon="📄")
st.header("Ask Your PDF 📄")

# Upload PDF
pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf is not None:
    # Extract text from the uploaded PDF
    pdf_reader = PdfReader(pdf)
    text = "".join([page.extract_text() for page in pdf_reader.pages])
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    try:
        # Create Chroma Index
        chroma_index = Chroma.from_texts(chunks, embeddings)
        retriever = chroma_index.as_retriever()
    except Exception as e:
        st.error(f"Failed to create Chroma index: {e}")

    # Proceed only if the Chroma index was created successfully
    if 'chroma_index' in locals():
        st.sidebar.header("Model Parameters")
        # Hyperparameters UI
        temperature = st.sidebar.slider("Temperature (Randomness control)", 0.0, 1.0, 0.7,
                                        help="Controls the randomness of the responses. Lower values make responses more deterministic.")
        max_tokens = st.sidebar.slider("Max Tokens (Response length)", 50, 500, 150,
                                       help="Sets the maximum number of tokens in the response. Adjust to increase or decrease response length.")
        top_p = st.sidebar.slider("Top P (Token selection probability)", 0.0, 1.0, 1.0,
                                  help="Controls the likelihood of token selection. Lower values focus on more likely tokens, reducing randomness.")

        # Initialize the Vertex AI model for QA
        llm = VertexAI(model="text-bison@001")
        qa_chain = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=retriever)

        # Conversation history
        if 'history' not in st.session_state:
            st.session_state.history = []

        # Query input and response
        query = st.text_input("Ask a question about your PDF")
        if st.button("Ask"):
            response = qa_chain.invoke(query, temperature=temperature, max_tokens=max_tokens, top_p=top_p)
            st.session_state.history.append({"question": query, "answer": response})

            for index, exchange in enumerate(st.session_state.history):
                st.text_area("Q:", value=exchange["question"], height=50, disabled=True, key=f"question_{index}")
                st.text_area("A:", value=exchange["answer"], height=100, disabled=True, key=f"answer_{index}")
