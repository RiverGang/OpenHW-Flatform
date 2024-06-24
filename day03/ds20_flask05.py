# request 모듈 사용
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get():
	value1 = request.args.get("이름", "user") # 이름 => Key, user => Value 
	value2 = request.args.get("주소", "부산")
	return value1 + ":" + value2
# get 방식으로 데이터 가져오기

## 주소창 /?이름=홍길동&주소=서울
## ? -> 물음표를 기준으로 클라이언트가 서버에게 데이터 전달
## 키=Value&키=Value 형태

if __name__ == "__main__": 
	app.run(host="0.0.0.0", port="10111", debug=True) 
