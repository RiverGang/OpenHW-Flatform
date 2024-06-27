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

if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
