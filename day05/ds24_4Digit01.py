# Button 클릭 마다 세그먼트 LED 숫자 변경

import RPi.GPIO as GPIO
import time

Pins = [20,21,12,23,24,25,26]
Button = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button, GPIO.IN)
for pin in Pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

seqs = [
 [0,0,0,0,0,0,1], # 0
 [1,0,0,1,1,1,1], # 1
 [0,0,1,0,0,1,0], # 2
 [0,0,0,0,1,1,0], # 3
 [1,0,0,1,1,0,0], # 4
 [0,1,0,0,1,0,0], # 5
 [0,1,0,0,0,0,0], # 6
 [0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,0], # 8
 [0,0,0,0,1,0,0]]  #9

count = 0

try:
	while True:
		if(count > 9):
			count = 0
		if(GPIO.input(Button) == True):
			print("LED: ",count)
			time.sleep(0.5)
			for num in range(0,7):
				GPIO.output(Pins[num], seqs[count][num])
			count += 1

except KeyboardInterrupt:
	GPIO.cleanup()
