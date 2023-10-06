from flask import Flask, render_template, request
from embedchain import App
import os

# Flask 애플리케이션 생성
app = Flask(__name__)

# OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "sdkfdicm"

# Embedchain App 객체 생성
elon_bot = App()

@app.route('/', methods=['GET', 'POST'])
def chat_with_elon():
    response = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        response = elon_bot.query(user_input)

    return render_template('chat.html', response=response)

if __name__ == '__main__':
    app.run()
