# 입력한 숫자 띄우기
import RPi.GPIO as GPIO
import time

segPins = [20,21,12,23,24,25,26]
COM = [4, 5, 6, 13]
GPIO.setmode(GPIO.BCM)

for pin in segPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

for com in COM:
	GPIO.setup(com, GPIO.OUT)

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
	number = 0
	while True:
		number += 1
		NUMBER = str(number)
		if(number > 9999):
			break
		if number <10:
			for num in range(0, 4):
				for reset in COM:
					GPIO.output(reset, False)
				GPIO.output(COM[3], True)
			for i in range(1, 7):
				GPIO.output(segPins[i], seqs[i][i])
			time.sleep(0.001)
		else:
			List = []
			for i in str(NUMBER): ## 자릿수별 숫자 배열 담기
				List.append(i)
			numList = list(map(int, List)) ## 형변환
			len = len(str(numList)) ## 배열길이
			size = 4-len ## 좌측 정렬을 위한 변수 size
			for num in range(0, len):
				for reset in COM:
					GPIO.output(reset, False) ## COM이 바뀔 때 마다 초기화
				GPIO.output(COM[num+size], True) ## COM에 신호인가
				for i in range(0, 7):
					GPIO.output(segPins[i], seqs[numList[num]][i]) ## 해당하는 숫자 표기
				time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()
