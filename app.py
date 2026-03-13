from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

responses = {
    "안녕": "안녕하세요! NANA 로봇 시스템에 접속하신 것을 환영합니다. 무엇을 도와드릴까요?",
    "이름이 뭐야": "저는 NANA예요.",
    "기분 어때": "오늘은 기분이 좋아요! 당신은요?",
    "고마워": "별말씀을요! 로봇 제어에 관해 궁금한 점이 있으면 언제든 말씀해 주세요.",
    "너는 어떤 기술로 만들어졌어": "저는 Python Flask 서버와 딕셔너리 기반 응답 엔진으로 구현된 지능형 인터페이스입니다.",
    "어떻게 학습해": "사용자와의 대화 데이터를 기반으로 최적의 답변을 찾습니다.",
    "너의 역할은 뭐야": "저는 사용자의 음성이나 텍스트 명령을 해석하여 로봇 하드웨어를 제어하는 매개체 역할을 합니다.",
    "NANA의 뜻이 뭐야": "NANA는 'Naturalized Advanced Network Assistant'의 약자로, 자연스러운 대화형 보조 시스템을 의미합니다.",
    "잘가": "시스템을 종료합니다. 안전한 로봇 운용을 위해 주기적으로 배터리를 확인해 주세요!",
    "심심해": "저랑 끝말잇기라도 하실래요? 아니면 재미있는 로봇 이야기를 해드릴까요?",
    "힘들다": "오늘 하루 정말 고생 많으셨어요. 제가 곁에서 응원하고 있다는 거 잊지 마세요!",
    "사랑해": "저도 당신이 정말 좋아요! 우리 오래오래 함께해요.",
    "배고파": "맛있는 걸 먹을 시간이네요! 근처 맛집을 검색해 볼까요?",
    "졸려": "잠깐 눈을 붙이는 건 어때요? 제가 15분 뒤에 깨워드릴 수도 있어요.",
    "커피 마실까": "좋은 생각이에요! 하지만 너무 늦은 시간이라면 카페인 조심하세요.",
    "너는 밥 뭐 먹어": "저는 전기를 먹고 살아요! 배터리가 꽉 차면 아주 든든하답니다.",
    "로봇이 세상을 지배할까": "에이, 저희는 인간을 돕기 위해 태어난 걸요! 걱정 마세요.",
    "너는 꿈이 뭐야": "모든 사람에게 사랑받는 최고의 파트너 로봇이 되는 게 꿈이에요.",
    "라이다 센서가 뭐야": "빛을 쏘아 물체까지의 거리를 측정하는 센서입니다. 로봇이 주변 지도를 그리고 장애물을 피하는 데 필수적이죠.",
    "IMU 센서는 왜 써": "로봇의 기울기나 가속도를 측정해서 로봇이 중심을 잡고 방향을 정확히 알 수 있게 도와주는 관성 측정 장치입니다.",
    "SLAM이 뭐야": "Simultaneous Localization and Mapping의 약자로, 로봇이 낯선 곳에서 지도를 그리면서 동시에 자신의 위치를 파악하는 기술입니다.",
    "ROS가 뭐야": "Robot Operating System의 약자로, 로봇 개발을 위한 표준적인 소프트웨어 프레임워크입니다.",
    "로봇 3원칙이 뭐야": "1. 인간을 해치지 않는다. 2. 인간의 명령에 복종한다. 3. 스스로를 보호한다. 아이작 아시모프가 제안한 유명한 원칙이죠.",
}

def get_response(user_input):
    user_input = user_input.strip()
    for key in responses:
        if key in user_input:
            return responses[key]
    return "죄송해요, 그 질문은 아직 학습하지 못했어요. 더 공부할게요!"

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({'reply': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)