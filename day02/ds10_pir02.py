#pir

## 적외선 인체감지 센서를 이용해 인체가 인식되면 "Detected" 문자열 출력
import RPi.GPIO as GPIO
import time

pirPin = 24
ledPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, True) ## LED 끄기 초기화

try:
	while True:
		if GPIO.input(pirPin) == True: ## 입력핀이 True면 인체 감지
			GPIO.output(ledPin, False)
			print("Human")
			time.sleep(5)

		else:
			GPIO.output(ledPin, True)
		
except KeyboardInterrupt:
	GPIO.cleanup()
