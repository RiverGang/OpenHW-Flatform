import time
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
stepPins = [21, 22, 23, 24]

for pin in stepPins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, False)

StepCounter = 0

StepCount = 4

Seq = [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]]

try:
	while 1:
		for pin in range(0,4):
			xpin = stepPins[pin]
			if Seq[StepCounter][pin]!=0:
				GPIO.output(xpin, True)

			else:
				GPIO.output(xpin, False)

		StepCounter += 1


		if (StepCounter==StepCount):
			StepConuter = 0
		if (StepCounter <0):
			StepCounter = StepCount


		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()
