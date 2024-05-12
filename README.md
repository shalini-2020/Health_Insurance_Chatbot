x`# Health Insurance Chatbot

### Introduction

The Health Insurance ChatBot is a Python application that allows to chat with multiple PDF documents. You can ask questions about the PDFs on health insurance policies and treatment. The application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate answers to queries. Please note that the app will only respond to questions related to the loaded PDFs.

### Prerequisites - Tech Stacks

Before using the Llama2 Medical Bot, make sure to have the following prerequisites installed on the system:

1. Python 3.8 or higher
2. Framework - Langchain
3. Frontend/webapp - Flask, HTML, CSS
4. LLM - meta llama 2
5. Vector DB - FAISS

### Installation

1. Replicate API Key: This is how we will apply the Llama2 model for our chatbot. Go to the Replicate website and sign up. Once you are signed up and logged in, navigate to this link to see your API Key:    https://replicate.com/account/api-tokens. Copy the key and save it for later.
   
2. Clone this repository to your local machine.

   ```bash
    git clone https://github.com/shalini-2020/Health_Insurance_Chatbot.git
    cd Health_Insurance_Chatbot
    ```
3. Create a Python virtual environment (optional but recommended):
    ```bash
    python -m venv insurance
    source .insurance/bin/activate  # On Windows, use: insurance\Scripts\activate
    ```
4. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```




