import os

from flask import Flask,render_template, request, jsonify
import google.generativeai as genai


import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')
CODE_CHAT_MODEL = os.getenv('CODE_CHAT_MODEL')

app = Flask(__name__)


config = {
    "max_output_tokens": 2048,
    "temperature": 0.9,
    "top_p": 1
}

genai.configure(api_key= os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel(os.getenv('MODEL'))
chat = model.start_chat()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    response = chat.send_message(userText, generation_config=config) # for the gemini AI model
    return response.text

if __name__ == "__main__":
    app.run()