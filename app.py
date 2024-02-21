from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Generative AI API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

app = Flask(__name__)

# Function to load the gemini pro model
def get_gemini_response(questions):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(questions)
    return response.parts[0].text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['GET', 'POST'])  # Allow GET and POST requests
def ask():
    if request.method == 'POST':
        user_question = request.form['question']
        response = get_gemini_response(user_question)
        return response
    else:
        # If the request method is GET, redirect or render a page
        return render_template('index.html')  # Example: Render a form for asking questions

if __name__ == '__main__':
    app.run(debug=True)
