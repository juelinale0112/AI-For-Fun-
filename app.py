
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

import os
app = Flask(__name__)


# Initialize the Generative AI Client
genai.configure(api_key = "..")  # Replace with your API key

def do_the_ai(the_prompt, the_question):
    model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest', system_instruction=the_prompt)
    resp = model.generate_content(the_question).text
    
    return resp

@app.route('/', methods=['GET', 'POST'])
def index():
    result_text = ""
    saved_text = ""  # Default value to store the text
    initial_text = "Enter your question here ..."
    saved_text = initial_text
    if request.method == 'POST':
        textbox1 = request.form.get('textbox1', '')
        textbox2 = request.form.get('textbox2', '')
        saved_text = textbox2

        # result_text = f"{textbox1} {textbox2}"  # Concatenate input from both textboxes
        result_text = do_the_ai(textbox1, textbox2)

    return render_template('index.html', result_text=result_text, saved_text=saved_text)

if __name__ == "__main__":
    app.run(debug=True)
