from flask import Flask, render_template, request
from embedchain import App
import os

# Flask 애플리케이션 생성
app = Flask(__name__)


elon_bot = None  # 초기화된 객체를 저장하기 위한 변수

@app.route('/', methods=['GET', 'POST'])
def chat_with_elon():
    global elon_bot  # elon_bot 변수를 함수 내에서 수정하기 위해 global로 선언
    response = ""

    if request.method == 'POST':
        user_input = request.form['user_input']

        if elon_bot is None:  # elon_bot이 아직 초기화되지 않았을 때만 초기화
            # 가져온 API 키를 환경 변수로 설정
            api_key = request.form['api_key']  # API 키를 가져옴
            os.environ["OPENAI_API_KEY"] = api_key
            print("시작")
            elon_bot = App()

        response = elon_bot.query(user_input)

    return render_template('chat.html', response=response)

if __name__ == '__main__':
    app.run()
