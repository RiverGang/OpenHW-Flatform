import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time
import RPi.GPIO as GPIO

form_class = uic.loadUiType("./test.ui")[0]

ledR= 21

rpiTimeNow = ""
userSetTime = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledR, GPIO.OUT)
GPIO.output(ledR, True) # 초기설정 LED 끄기

#windowClass
class WindowClass (QMainWindow, form_class):
	def __init__(self): # 생성자,  첫번째 인자 self
		super().__init__() # 부모클래스 생성자 (QWidges)
		self.setupUi(self)

		# QTimer 설정
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_time)
		self.timer.start(1000) # 1초마다 갱신

		self.update_time() #초기 시간 설정

	def update_time(self):
			global rpiTimeNow, userSetTime

			timestamp = time.time()
			lt = time.localtime(timestamp)
			timeNow = time.strftime("%H :%M", lt)
			self.lcdNumber.display(timeNow)

			rpiTimeNow  = time.strftime("%H%M", lt) # 라즈베리 파이(콘솔)로 넘길 시간

			if userSetTime is not None and userSetTime == rpiTimeNow:
				LED_blink()
				userSetTime = None

	def BtnsaveFnc(self):
			t = self.timeEdit.time() # timeEdit 시간  가져오기

			global userSetTime
			userSetTime = t.toString("HHmm")
			print(userSetTime)


# 전역 타이머 설정
def print_time():
	#print(rpiTimeNow)
	pass

def LED_blink():
	for i in range(10):
		GPIO.output(ledR, False)
		time.sleep(1)
		GPIO.output(ledR, True)
		time.sleep(1)
	GPIO.output(ledR, True)

# GUI 실행
if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	

	console_timer = QTimer() ## GUI 창 실행과 콘솔출력이 동시에 되도록
	console_timer.timeout.connect(print_time)
	console_timer.start(1000)

	sys.exit(app.exec_())
