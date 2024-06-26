# COM 입력 단자 별 숫자 다르게 띄우기
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
 [1,0,0,1,1,1,1],
 [0,0,1,0,0,1,0],
 [0,0,0,0,1,1,0],
 [1,0,0,1,1,0,0],
]

try:
	while True:
			for com, seq in zip(COM, seqs):
				for reset in COM:
					GPIO.output(reset,  False)
				GPIO.output(com, True)
				for i in range(0, 7):
					GPIO.output(segPins[i], seq[i])
				time.sleep(0.001)

except KeyboardInterrupt:
	GPIO.cleanup()
