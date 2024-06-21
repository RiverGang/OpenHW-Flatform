import RPi.GPIO as GPIO
import time

red_led = 21
blue_led = 20
green_led = 16

button = 6
i = 0

#GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

## 1초마다 RGB 색상이 변경되도록
try:
	while True:
		if GPIO.input(button) == True:
			i += 1
			if i > 2:
				i = 0

			if i == 0:
					GPIO.output(red_led, False)
					GPIO.output(blue_led, True)
					GPIO.output(blue_led, True)
					print("RED")

			elif i == 1:
					GPIO.output(red_led, True)
					GPIO.output(blue_led, False)
					GPIO.output(green_led, True)
					print("Blue")

			elif i == 2:
					GPIO.output(red_led, True)
					GPIO.output(blue_led, True)
					GPIO.output(green_led, False)
					print("GREEN")

			time.sleep(0.5)

except KeyboardInterrupt: ## Ctrl + c 키보드 입력 시 프로그램 종료
	GPIO.output(red_led, True)
	GPIO.output(blue_led, True)
	GPIO.output(green_led, True)

	GPIO.cleanup() ## 프로그램 종료 시키며 핀 초기화
