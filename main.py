#Check Requirements.txt and import the necessary packages. 
#PDF Vertex AI Bot, 
#Pros: Cheap to use. 
#cons: A little slow, can use a better model to improve answer generation and performance, I've used "gemini-pro". You can kick it up a notch if you wish. 
#Dm if you would like an Custom Industry Scalable version for your company with an even better fine-tuned model. 
import os
from datetime import datetime, timezone
import streamlit as st
from google.cloud import aiplatform, bigquery
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_vertexai import VertexAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from typing import List

# Setting environment variables for Google Cloud Platform
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "**Link to your json cred**" (Replace these) 
project_id = "**your project id**"
location = "GCP location"

# Initialize Google Vertex AI and BigQuery Client
aiplatform.init(project=project_id, location=location)
bq_client = bigquery.Client()


# Function to create dataset and table if not exists
def create_bigquery_dataset_table(dataset_id, table_id, schema):
    dataset_ref = bq_client.dataset(dataset_id)
    try:
        bq_client.get_dataset(dataset_ref)
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        bq_client.create_dataset(dataset, exists_ok=True)

    table_ref = dataset_ref.table(table_id)
    try:
        bq_client.get_table(table_ref)
    except Exception:
        table = bigquery.Table(table_ref, schema=schema)
        bq_client.create_table(table, exists_ok=True)


# Define the schema of the table
schema = [
    bigquery.SchemaField("question", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("answer", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("timestamp", "TIMESTAMP", mode="REQUIRED"),
]

# Create dataset and table
dataset_id = "questions_answers"
table_id = "conversations"
create_bigquery_dataset_table(dataset_id, table_id, schema)

# Mock implementation of an embeddings class
class MockEmbeddings:
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[0.1] * 768 for _ in texts]

    def embed_query(self, text: str) -> List[float]:
        return [0.1] * 768


embeddings = MockEmbeddings()

# Streamlit UI setup
st.set_page_config(page_title="Mr.DOC", page_icon="📄")
st.header("Ask Your PDF 📄")
pdf = st.file_uploader("Upload your PDF", type="pdf")

if pdf is not None:
    pdf_reader = PdfReader(pdf)
    text = "".join([page.extract_text() for page in pdf_reader.pages])
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200
    )
    chunks = text_splitter.split_text(text)

    try:
        chroma_index = Chroma.from_texts(chunks, embeddings)
        retriever = chroma_index.as_retriever()
    except Exception as e:
        st.error(f"Failed to create Chroma index: {e}")

    if "chroma_index" in locals():
        st.sidebar.header("Model Parameters")
        temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
        max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 150)
        top_p = st.sidebar.slider("Top P", 0.0, 1.0, 1.0)

        # Update LLM instantiation to use Gemini Pro
        llm = VertexAI(
            model_name="gemini-pro",
            temperature=temperature,
            max_output_tokens=max_tokens,
            top_p=top_p,
        )
        qa_chain = RetrievalQA.from_chain_type(
            llm, chain_type="stuff", retriever=retriever
        )

        if "history" not in st.session_state:
            st.session_state.history = []

        query = st.text_input("Ask a question about your PDF", key="query_input")
        if st.button("Ask", key="ask_button"):
            response = qa_chain({"query": query})  # Adjust invocation for Gemini
            # Ensure response is a string
            response_str = response["result"] if response else ""
            record = {
                "question": query,
                "answer": response_str,
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
            st.session_state.history.append(record)
            # Save to BigQuery
            table_ref = f"{project_id}.{dataset_id}.{table_id}"
            try:
                response = bq_client.insert_rows_json(table_ref, [record])
                if response:
                    st.error(f"Insert contained errors: {response}")
                else:
                    st.success("Record successfully added to BigQuery.")
            except Exception as e:
                st.error(f"Failed to insert record into BigQuery: {e}")

    st.write("Conversation History:")
    for exchange in reversed(st.session_state.history):
        st.text_area("Q:", value=exchange["question"], height=50, disabled=True)
        st.text_area("A:", value=exchange["answer"], height=100, disabled=True)
