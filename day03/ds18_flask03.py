## UPL 접속으로  /led/on, led/off하는 웹페이지 만들기
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

@app.route("/led/on")
def name():
	GPIO.output(led, False)
	return "<h1>LED ON</h1>"

@app.route("/led/off")
def age():
	GPIO.output(led, True)
	return "<h1>LED OFF</h1>" ## 고정된 값을 보여주는 정적 라우팅

if __name__ == "__main__": # 터미널에서 직접 실행시키면 실행파일이 main으로 바뀐다
	app.run(host="0.0.0.0", port="10111", debug=True) #실행을 위한 명련문으로 보면 된다
