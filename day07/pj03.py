import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import time

# LCD Number 모듈과 Dial 모듈이용
# Dial 모듈을 조작에 따라  LCD Number 모듈의 숫자가 변경되도록 
form_class = uic.loadUiType("./test.ui")[0]



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
			timestamp = time.time()
			lt = time.localtime(timestamp)
			timeNow = time.strftime("%H :%M", lt)
			self.lcdNumber.display(timeNow)

			global rpiTimeNow
			rpiTimeNow  = time.strftime("%H%M", lt) # 라즈베리 파이(콘솔)로 넘길 시간

			t = self.timeEdit.time() # timeEdit 시간 값 가져오기
			global userSetTime
			userSetTime = t.toString("HHmm")
			print(userSetTime)




# 전역 타이머 설정
def print_time():
	print(rpiTimeNow)


# GUI 실행
if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()

	console_timer = QTimer() ## GUI 창 실행과 콘솔출력이 동시에 되도록
	console_timer.timeout.connect(print_time)
	console_timer.start(1000)

	sys.exit(app.exec_())

	try:
		pass

	except KeyboardInterrupt:
		pass
