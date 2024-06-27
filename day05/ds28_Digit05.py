# 1부터 9999까지 카운트하기
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

def display_number(number):
	number_str = str(number)
	length = len(number_str)
	size = 4 - length
	for x in range(10):
		for digit in range(length):
			for reset in COM:
				GPIO.output(reset, False)
			GPIO.output(COM[digit + size], True)
			num = int(number_str[digit])
			for i in range(7):
				GPIO.output(segPins[i], seqs[num][i])
			time.sleep(0.02)

try:
		number = 0
		while True:
			display_number(number)
			number += 1
			if number > 9999:
				print("Finish")
			time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()
