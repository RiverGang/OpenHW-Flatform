import RPi.GPIO as GPIO
import time

Pins = [20,21,12,23,24,25,26]

GPIO.setmode(GPIO.BCM)
for pin in Pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, True)

seqs = [
 [0,0,0,0,0,0,1],
 [1,0,0,1,1,1,1],
 [0,0,1,0,0,1,0],
 [0,0,0,0,1,1,0],
 [1,0,0,1,1,0,0],
 [0,1,0,0,0,0,0],
 [0,0,0,1,1,1,1],
 [0,0,0,0,0,0,0],
 [0,0,0,0,1,0,0]]

try:
	while True:
		for seq in seqs:
			for num in range(0,7):
				GPIO.output(Pins[num], seq[num])
			time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
