from flask import Flask, render_template, request
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
prompt.format(product="colorful socks")

import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)




app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        user_prompt = request.args.get('user_prompt')
        if user_prompt:
            prompt = PromptTemplate.from_template(user_prompt)
            return prompt
        else:
            return 'no user prompt inputted'
    else:
        return 'endpoint only accepts get request'

    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
