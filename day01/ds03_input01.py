import RPi.GPIO as GPIO
import time

swicth = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(swicth, GPIO.IN)

try:
	while True:
		if GPIO.input(swicth) == True:
			print("Pushed")
			time.sleep(0.3)

except KeyboardInterrupt:
	GPIO.cleanup()
