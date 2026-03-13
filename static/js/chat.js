// 1. chat.html의 ID와 정확히 일치시킵니다.
const chatBox = document.getElementById('chatMessages'); 
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

// 2. '전송' 버튼에 클릭 이벤트 리스너를 추가합니다.
sendButton.addEventListener('click', sendMessage);

// 3. 엔터 키 이벤트 리스너 (이건 원래 잘 되어 있었습니다)
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// 메시지 전송 함수
async function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return;

    // 4. 'sender' 타입을 'user'로 지정하여 CSS가 적용되게 합니다.
    appendMessage('user', message);
    userInput.value = '';

    try {
        const res = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message }),
        });

        if (!res.ok) {
            throw new Error('서버 응답 오류');
        }

        const data = await res.json();
        // 5. 'sender' 타입을 'bot'으로 지정하여 CSS가 적용되게 합니다.
        appendMessage('bot', data.reply);

    } catch (error) {
        console.error('Error:', error);
        // 6. 오류 메시지도 봇이 말하는 것처럼 표시합니다.
        appendMessage('bot', '⚠️ 오류: 서버와 연결할 수 없습니다.');
    }
}

// 대화창에 메시지 추가 (chat.html의 CSS와 일치하도록 수정)
function appendMessage(senderType, text) {
    const messageElem = document.createElement('div');
    
    // 7. 'message' 클래스와 'user' 또는 'bot' 클래스를 추가합니다.
    //    이래야 chat.html의 <style> 태그가 인식합니다.
    messageElem.classList.add('message', senderType); 
    
    messageElem.innerText = text; // HTML 대신 순수 텍스트(innerText)로 설정 (보안에도 더 좋습니다)
    
    chatBox.appendChild(messageElem);
    chatBox.scrollTop = chatBox.scrollHeight; // 새 메시지가 보이도록 스크롤
}
