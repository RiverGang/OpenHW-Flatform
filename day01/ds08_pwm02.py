# 키보드 입력에 따라 음계 울리기
import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [261, 294, 329, 349, 393, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

## 아날로그 출력을 위한 객체생성 (440Hz 출력)
Buzz = GPIO.PWM(piezoPin, 10)

try:
	while True:
		key = input()
		i = int(key)-1
		if 0 <= i < len(melody):
			Buzz.start(50)
			Buzz.ChangeFrequency(melody[int(key)-1])
			time.sleep(0.5)
		else:
			print("1~8을 입력하세요\n")

except KeyboardInterrupt:
	GPIO.cleanup()
