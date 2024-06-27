import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("./test02.ui")[0]

#windowClass
class WindowClass (QMainWindow, form_class):
	def __init__(self): # 생성자,  첫번째 인자 self
		super().__init__() # 부모클래스 생성자 (QWidges)
		self.setupUi(self)

		# 이벤트 함수 등록
		self.btn_1.clicked.connect(self.btn1Function)
		self.btn_2.clicked.connect(self.btn2Function)


	# 이벤트 함수 정의
	def btn1Function(self):
		print("LED ON Button Click")
	def btn2Function(self):
		print("LED OFF Button Click")
	def slot1(self): ## Qt Designer에서 이벤트를 등록해두면 생성자에 이벤트 연결을 하지 않고, 함수만 생성하면 됨
		print("exit")

if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
