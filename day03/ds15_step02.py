## ds14 모터 돌리기 반복문으로 구현

import RPi.GPIO as GPIO
import time

steps = [21, 22, 23, 24]
GPIO.setmode(GPIO.BCM)
i = 3
for stepPin in steps:
	GPIO.setup(stepPin, GPIO.OUT) ## 핀 설정
	GPIO.output(stepPin, 0) ## 초기 값 설정

seqs = [[0,0,0,1], [0,0,1,1], [0,0,1,0], [0,1,1,0], [0,1,0,0], [1,1,0,0], [1,0,0,0], [1,0,0,1]]

try:
	while 1:
		for seq in seqs: ## 2차원 배열 -> seq = [0,0,0,1] 일차원 배열
			for num in range(0,4): ## 모터 핀 0번부터 3번까지
				GPIO.output(steps[num], seq[num])
			time.sleep(0.1) ## seq 마다 딜레이 주기

except KeyboardInterrupt:
	GPIO.cleanup()
