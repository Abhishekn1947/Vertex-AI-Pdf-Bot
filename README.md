📄 Mr.DOC: Your PDF Q&A Assistant (POWER TO THE USER)
🎉 Unlike ChatGPT or Gemini, Mr.DOC allows you to upload large PDF files (up to 200MB) and reads the entire document before answering your questions. Mainly keeps your data local and uses your Systems processing power to run the program. 

Best of all, Its free to use. Dm me on www.aboutabhi.com if you would like a custom LLM. 

-> This capability provides more accurate and comprehensive responses.
-> The main merit of this project is that it allows the user to store the data locally, and allows the user to store the data on their own big query if they want to. Hence ensuring data privacy and not giving the AI companies access to your data. 
-> I'm basically using their brain, but not storing the data on that brain. just using it. 

![diagram (2)](https://github.com/user-attachments/assets/8abb5e29-e154-41ed-a950-c9ec3b255427)

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

![image](https://github.com/Abhishekn1947/PDF_BOT/assets/134388969/d18dd665-391e-4c26-8c42-6f6dca611a98)

![image](https://github.com/Abhishekn1947/PDF_BOT/assets/134388969/0804d070-5dc4-4bc3-b506-7a9fb84533ff)

![image](https://github.com/Abhishekn1947/PDF_BOT/assets/134388969/55fec803-4c29-4449-b45b-583690266dde)

![image](https://github.com/Abhishekn1947/PDF_BOT/assets/134388969/a61cffea-ede7-4962-91bc-cf208b0690db)

Upcoming updates: 
1) TO read any kind of a file.
2) consider images and tables as well and give answer in a structured table format as user requires 
