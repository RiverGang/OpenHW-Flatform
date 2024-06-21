#pir

## 적외선 인체감지 센서를 이용해 인체가 인식되면 "Detected" 문자열 출력
import RPi.GPIO as GPIO
import time

pirPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)

try:
	while True:
		if GPIO.input(pirPin) == True: ## 입력핀이 True면 인체 감지
			print("Detected")
			time.sleep(0.5)

except KeyboardInterrupt:
	GPIO.cleanup()
