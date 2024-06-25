from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time
import datetime

swPin = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN)

picam2 = Picamera2() ## Picamera2 클래스를 사용해 picam2 객체생성
camera_config = picam2.create_preview_configuration() ## picam2 객체를 이용해 미리보기 구성(configuration)생성
picam2.configure(camera_config)
picam2.start()

try:
	while True:
		if GPIO.input(swPin) == True:
				now = datetime.datetime.now()
				print(now)
				fileName = now.strftime('%Y-%m-%d %H:%M:%S')
				picam2.capture_file(fileName + '.jpg')

		time.sleep(0.2)

except KeyboardInterrupt:
	pass
