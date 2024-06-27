import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# LCD Number 모듈과 Dial 모듈이용
# Dial 모듈을 조작에 따라  LCD Number 모듈의 숫자가 변경되도록 
form_class = uic.loadUiType("./test03.ui")[0]

#windowClass
class WindowClass (QMainWindow, form_class):
	def __init__(self): # 생성자,  첫번째 인자 self
		super().__init__() # 부모클래스 생성자 (QWidges)
		self.setupUi(self)

		# 이벤트 함수 등록
	def lcd_slot(self, value):
		self.lcdNumber.display(value)

if __name__ =="__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	myWindow.show()
	app.exec_()
