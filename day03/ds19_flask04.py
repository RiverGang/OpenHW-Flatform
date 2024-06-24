## 라우팅 구문(=주소창)안에서의 변수 <> 사용
import RPi.GPIO as GPIO
from flask import Flask
led = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, True)

app = Flask(__name__)

@app.route("/")
def hello():
	return "LED Control Web page"

@app.route("/led/<state>") # 주소창 내 변수 state -> <>으로 감싸기
def fun(state): # 변수 state를 사용하는 함수
	if state == "on":
		GPIO.output(led, False)
		return "<h1>LED ON</h1>"
	elif state == "off":
		GPIO.output(led, True)
		return "<h1>LED OFF</h1>" ## 고정된 값을 보여주는 정적 라우팅
	elif state == "clear":
		GPIO.cleanup()
if __name__ == "__main__": # 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다
	app.run(host="0.0.0.0", port="10111", debug=True) #실행을 위한 명련문으로 보면 된다
