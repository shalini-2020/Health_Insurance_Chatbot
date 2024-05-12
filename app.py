from flask import Flask, render_template, jsonify, request
import settings
import data_injest as data_injest 
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Replicate
from prompt import *
import os

app = Flask(__name__)

embeddings = data_injest.hugging_face_embeddings()

docsearch = FAISS.load_local(settings.db_vector_path,embeddings,allow_dangerous_deserialization=True)

# Build custom prompts
PROMPT=PromptTemplate(template=ptemplate, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

# Initialize Replicate Llama2 Model
llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
    model_kwargs={"temperature": 0.75, "max_new_tokens": 4096}
)

# Build the conversation chain
healthbot=RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff", 
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def main():
    return render_template('home.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=healthbot({'query': input})
    print("Response : ", result["result"])
    return result["result"]

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 5000, debug= False)