import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time
import RPi.GPIO as GPIO

form_class = uic.loadUiType("./DigitalAlarm.ui")[0]

ledPin= {"Red":18, "Blue":23, "Green":24} # LED GPIO핀 딕셔너리 형태
piezoPin = 12
switch = 21

## 전역변수 선언
rpiTimeNow = ""
userSetTime = None
userSetLED = None
userSetRepeat = None
userSetSound = None

# GPIO 세팅

GPIO.setmode(GPIO.BCM)
# LED setting
for value in ledPin.values(): # 딕셔너리의 값(Value) 반복문 
	GPIO.setup(value, GPIO.OUT)
	GPIO.output(value, True) # 초기설정 LED 끄기

# Piezo setting
GPIO.setup(piezoPin, GPIO.OUT)
Buzz = GPIO.PWM(piezoPin, 10)
melody = [261, 294, 329, 349, 393, 440, 493, 523]
Sound = {
"Star": [melody[0],melody[0],melody[4],melody[4],melody[5],melody[5],melody[4]
				 ,melody[3],melody[3],melody[2],melody[2],melody[1],melody[1],melody[0]],
"Butterfly": [melody[4],melody[2],melody[2],melody[3],melody[1],melody[1],melody[0]
				 ,melody[1],melody[2],melody[3],melody[4],melody[4],melody[4]]
}

# LCD 7-segments setting
fndDatas = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xD8, 0x80, 0x90]
fndSegs = [5,6,13,19,26,16,20]
fndSels = [17, 27, 22, 4]

for fndSeg in fndSegs:
	GPIO.setup(fndSeg, GPIO.OUT)
	GPIO.output(fndSeg, 1)

for fndSel in fndSels:
	GPIO.setup(fndSel, GPIO.OUT)
	GPIO.output(fndSel, 0)

# Button setting
GPIO.setup(switch, GPIO.IN)

#windowClass
class WindowClass (QMainWindow, form_class):
	def __init__(self): # 생성자,  첫번째 인자 self
		super().__init__() # 부모클래스 생성자 (QWidges)
		self.setupUi(self)

		# QTimer 설정 실시간 시간 업데이트
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_time)
		self.timer.start(1000) # 1초마다 갱신

		self.update_time() #초기 시간 설정

	def update_time(self):
			global rpiTimeNow, userSetTime

			timestamp = time.time() ## 현재 시간 가져오기
			lt = time.localtime(timestamp)
			timeNow = time.strftime("%H:%M", lt) ## 문자형태 변환
			self.lcdNumber.display(timeNow)

			rpiTimeNow  = time.strftime("%H%M", lt) # 라즈베리 파이(콘솔)로 넘길 시간

			if userSetTime is not None and userSetTime == rpiTimeNow:
				LED_blink() ## 알람실행

	def BtnsaveFnc(self):
			t = self.timeEdit.time() # timeEdit 시간  가져오기

			## 사용자가 설정한 정보 전역 변수에 담기
			global userSetTime, userSetLED, userSetRepeat, userSetSound
			userSetTime = t.toString("HHmm")
			userSetLED = ledPin[self.CboLED.currentText()]
			userSetRepeat = int(self.CboRepeat.currentText())
			userSetSound = self.CboSound.currentText()

			## 하단 알람설정 정보창 업데이트
			self.LblTime.setText("Time : " + userSetTime)
			self.LblColor.setText("Color : " + self.CboLED.currentText())
			self.LblRepeat.setText("Repeat : " + self.CboRepeat.currentText())
			self.LblSound.setText("Sound : " + self.CboSound.currentText())
			print(userSetTime)

	## 하단 설정 정보창 Reset
	def BtnResetFnc(self):
		global userSetTime, userSetLED, userSetRepeat, userSetSound
		userSetTime = userSetLED = userSetRepeat = userSetSound = None
		self.LblTime.setText("Time : ")
		self.LblColor.setText("Color : ")
		self.LblRepeat.setText("Repeat : ")
		self.LblSound.setText("Sound : ")

## 7-segment 숫자 표기
def findOut(data, sel):
	for i in range(0,7):
		GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
		for j in range(0,4):
			if j==sel:
				GPIO.output(fndSels[j], 1)
			else:
				GPIO.output(fndSels[j], 0)

# 전역 타이머 설정
def print_time():
	global rpiTimeNow
	while True:
		List = []
		for i in rpiTimeNow:
			List.append(i)
		timeList = list(map(int, List))

		for i in range(3, -1, -1):
			findOut(timeList[i],i)
			time.sleep(0.005)

# 알람 울림 함수
def LED_blink():
	GPIO.output(userSetLED, False)
	for i in range(userSetRepeat):
		if GPIO.input(switch) == True: # switch 버튼 누르면 알람 종료
			break
		if userSetSound == "Warning":
			Buzz.start(30)
			time.sleep(1)
			Buzz.stop()
			time.sleep(1)
		else:
			for i in Sound[userSetSound]:
				Buzz.start(30)
				Buzz.ChangeFrequency(i)
				time.sleep(0.5)
				Buzz.stop()
				time.sleep(0.1)
	GPIO.output(userSetLED, True)
	Buzz.stop()

# GUI 실행
if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()

	console_thread = threading.Thread(target=print_time) ## RPi 보드에서 표기 될 7-segments 화면 쓰레드 처리
	console_thread.daemon = True # 메인 스레드 종료시 함께 종료
	console_thread.start()
	sys.exit(app.exec_())
	try:
		pass
	except KeyboardInterrupt:
		GPIO.cleanup()
