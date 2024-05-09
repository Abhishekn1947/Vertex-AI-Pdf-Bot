# Vertex-AI-Pdf-Bot

This project, named "Mr.DOC," is a Streamlit-based web application that integrates Google Cloud Vertex AI to provide a powerful Q&A system for your PDF documents. By simply uploading a PDF and posing questions, the system can extract relevant answers using advanced machine learning models and efficient document retrieval methods.

Mr.DOC: Your PDF Q&A Assistant
Project Overview
This project, named "Mr.DOC," is a Streamlit-based web application that integrates Google Cloud Vertex AI to provide a powerful Q&A system for your PDF documents. By simply uploading a PDF and posing questions, the system can extract relevant answers using advanced machine learning models and efficient document retrieval methods.

Objectives
* Build an application that allows users to upload a PDF and ask questions about the document's content.
* Implement customizable machine learning parameters to tailor the responses.
* Provide a clear and interactive user interface for document Q&A.

-> Getting Started

-> Prerequisites

* Google Cloud Account: Access to Google Cloud Platform (GCP) with Vertex AI enabled, API Key. 
* Python Environment: A Python environment with the necessary packages installed. (Check Requirements.txt) 

-> Setup Instructions
* Clone the Repository:
* Clone the project's GitHub repository to your local machine.

Code for your reference: 

bash
(Copy code)
git clone <REPO_URL>
cd <REPO_NAME>

-> Install Dependencies:
* Install the necessary Python packages using pip, check the requirements.txt (IMPORTANT)

bash
(Copy code)
pip install -r requirements.txt

Configure Google Cloud Credentials:
Obtain a JSON file containing your service account credentials from GCP.
Update the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to this JSON file.

Example:
bash
(Copy code)
export GOOGLE_APPLICATION_CREDENTIALS="path/to/google/credentials.json"

* Update the project_id variable within the code with your Google Cloud project ID.

-> Run the Application:
-> Start the Streamlit application by running:

bash
(Copy code)
streamlit run (File Name).py

-> Using the Application:
* Access the running application via your browser.
* Upload a PDF and ask questions using the provided input field.
 
Conclusion
Mr.DOC provides a streamlined, interactive way to gain insights from PDF documents using the power of Vertex AI. Adjust the parameters to refine responses, and explore new ways to enhance this project to meet your specific needs.

#I Appreciate Contributions/ Please feel free to use my code and collab as necessary and do give a follow. Thanks 
#Further more, I've also built an Chatbot using Open Source Packages, Completely free. But it requires significant processing power (Reach out if you would like to collab on that). 

License
This project is licensed under the MIT License.
