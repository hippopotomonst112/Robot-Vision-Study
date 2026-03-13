from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer # Trainer 두 종류 모두 가져오기

app = Flask(__name__)

# 1. 챗봇 객체 생성 (이름은 NANA로 설정)
chatbot = ChatBot(
    'NANA', 
    logic_adapters=['chatterbot.logic.BestMatch']
)

# 2. 말뭉치 학습 (수천 가지 대화를 배우는 과정)
# 이 과정은 처음에 시간이 좀 걸릴 수 있습니다.
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
corpus_trainer.train("chatterbot.corpus.korean") 

# 3. 사용자 정의 학습 (내가 원하는 특정 대화 가르치기)
trainer = ListTrainer(chatbot)
trainer.train([
    "안녕",
    "안녕하세요! 만나서 반가워요 😊",
    "이름이 뭐야?",
    "저는 NANA예요.",
    "기분 어때?",
    "오늘은 기분이 좋아요! 당신은요?",
    "고마워",
    "천만에요! 도움이 되었다니 기뻐요."
])

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot.get_response(user_input)
    return jsonify({'reply': str(response)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


