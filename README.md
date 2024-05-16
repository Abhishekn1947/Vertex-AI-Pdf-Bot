📄 Mr.DOC: Your PDF Q&A Assistant 🚀
🎉 Unlike ChatGPT or Gemini, Mr.DOC allows you to upload large PDF files (up to 200MB) and reads the entire document before answering your questions. This capability provides more accurate and comprehensive responses.

🌟 Project Overview
"Mr.DOC" is a Streamlit-based web application that leverages Google Cloud Vertex AI to deliver a powerful Q&A system for your PDF documents. By simply uploading a PDF and asking questions, the system can extract relevant answers using advanced machine learning models and efficient document retrieval methods.

🎯 Objectives
📝 Enable users to upload a PDF and ask questions about the document's content.
🔧 Implement customizable machine learning parameters to tailor the responses.
💻 Provide a clear and interactive user interface for document Q&A.

🚀 Getting Started

Prerequisites
🌐 Google Cloud Account: Access to Google Cloud Platform (GCP) with Vertex AI enabled and an API Key.
🐍 Python Environment: A Python environment with the necessary packages installed (Check requirements.txt).

Setup Instructions
1. Clone the Repository:

bash:
git clone <REPO_URL>
cd <REPO_NAME>

2. Install Dependencies:
Install the necessary Python packages using pip from the requirements.txt file in your environment. 

bash: 
pip install -r requirements.txt

3. Configure Google Cloud Credentials:
Obtain a JSON file containing your service account credentials from GCP.
Update the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to this JSON file:

bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/google/credentials.json"

Update the project_id and location variable within the code with your Google Cloud project ID.

4. Run the Application:
Start the Streamlit application by running:

bash

streamlit run app.py
Using the Application:
📂 Upload a PDF and ask questions using the provided input field.
🌐 Access the running application via your browser.

Upcoming updates: 
1) TO read any kind of a file.
2) consider images and tables as well and give answer in a structured table format as user requires 
