import RPi.GPIO as GPIO
import time

Pins = [20, 21, 12, 23, 24, 25, 26] # a,b,c,d,e,f,g

GPIO.setmode(GPIO.BCM)

for pin in Pins:
	GPIO.setup(pin, GPIO.OUT) ## 핀 설정
	GPIO.output(pin, True)

seqs =
[[0,0,0,0,0,0,1], # 0
 [1,0,0,1,1,1,1], # 1
 [0,0,1,0,0,1,0], # 2
 [0,0,0,0,1,1,0], # 3
 [1,0,0,1,1,0,0], # 4
 [0,1,0,0,1,0,0], # 5
 [0,1,0,0,0,0,0], # 6
 [0,0,0,1,1,1,1], # 7
 [0,0,0,0,0,0,0], # 8
 [0,0,0,0,1,0,0]] # 9
## 0이 LED on
try:
	while True:
		 for  seq in seqs:
		 	for num in range(0,7):
		 		GPIO.output(Pins[num],seq[num])
		 	time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

