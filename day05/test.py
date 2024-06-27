import RPi.GPIO as GPIO

COM = [4, 5, 6, 13]

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(4, False)
GPIO.output(5, False)
GPIO.output(6, False)
GPIO.output(13, False)


GPIO.setup(16, GPIO.OUT)
GPIO.output(16, False)
GPIO.setup(aPin, GPIO.OUT)

try:
	while True:
		GPIO.output(22, True)
		GPIO.output(aPin, False)

except KeyboardInterrupt:
	GPIO.cleanup()
