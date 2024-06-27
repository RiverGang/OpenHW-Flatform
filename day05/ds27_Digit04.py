# 입력한 숫자 띄우기
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
segPins = [5,6,13,19,26,16,20]
COM = [17,27,22,4]

for pin in segPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

for com in COM:
	GPIO.setup(com, GPIO.OUT)
	GPIO.output(com, False)

seqs = [
 [0,0,0,0,0,0,1],  # 0
 [1,0,0,1,1,1,1], # 1
 [0,0,1,0,0,1,0], # 2
 [0,0,0,0,1,1,0], # 3
 [1,0,0,1,1,0,0], # 4
 [0,1,0,0,1,0,0], # 5
 [0,1,0,0,0,0,0], # 6
 [0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,0], # 8
 [0,0,0,0,1,0,0]  # 9
]

try:
		NUMBER = input("숫자를 입력하세요(0~9999) >> ")
		List = []
		for i in str(NUMBER): ## 자릿수별 숫자 배열 담기
			List.append(i)
		numList = list(map(int, List)) ## 형변환
		len = len(str(NUMBER)) ## 숫자길이
		size = 4-len ## 좌측 정렬을 위한 변수 size

		while True:
			for num in range(0, len):
				for reset in COM:
					GPIO.output(reset,  False) ## COM이 바뀔 때 마다 초기화
				GPIO.output(COM[num+size], True) ## COM에 신호인가
				for i in range(0, 7): 
					GPIO.output(segPins[i], seqs[numList[num]][i]) ## 해당하는 숫자 표기
				time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()


