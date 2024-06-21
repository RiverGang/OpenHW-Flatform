import RPi.GPIO as GPIO
import time

red_led = 21
blue_led = 20
green_led = 16

#GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

## 1초마다 RGB 색상이 변경되도록
try:
	while True:
		key = input("LED on -> O | LED Off -> X\n")

		if (key == "o" or key == "O"):
			GPIO.output(red_led, False)
			GPIO.output(blue_led, False)
			GPIO.output(blue_led, False)
		elif (key == "x" or key == "X"):
			GPIO.output(red_led, True)
			GPIO.output(blue_led, True)
			GPIO.output(green_led, True)
		else:
			print("올바른 키를 입력하세요\n")

except KeyboardInterrupt: ## Ctrl + c 키보드 입력 시 프로그램 종료
	GPIO.cleanup() ## 프로그램 종료 시키며 핀 초기화
