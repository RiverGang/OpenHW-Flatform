# 충돌 방지 시스템
# 일정 거리 내로 물체가 탐지되면 부저 울리기 + LED 경고등 켜짐
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(triPin, True)
	time.sleep(0.00001) ## 거리를 측정할 초음파 펄스 0.0001초(10us) 동안 초음파발생 준비
	GPIO.output(triPin, False)
	start = time.time() # 현재 시간 저장

	while GPIO.input(echoPin) == False: # echo가 없으면 
		start = time.time() # 현재 시간을 start 변수에 저장

	while GPIO.input(echoPin) == True: # echo가 있으면 (반사되어 돌아오면)
		stop = time.time()	# 현재 시간을 stop 변수에 저장
	dlapsed = stop - start # 걸린 시간 구하기
	distance = (dlapsed * 19000) / 2 # 초음파 속도를 이용해 거리 계산

	return distance # 거리 반환

# 핀설정
triPin = 6
echoPin = 13
piezoPin = 24
red_LED =  20
blue_LED = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(triPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)
GPIO.setup(red_LED, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 250)
GPIO.output(red_LED, True)

try:
	while True:
		distance = measure()
		print("Distance: %.2f cm" %distance) ## 소숫점 둘째 자리까지 확인
		time.sleep(0.1)

		if 40 <= distance and distance < 50:
			GPIO.output(red_LED, False)
			Buzz.start(30)
			time.sleep(0.8)
			Buzz.stop()

		elif 30 < distance and distance <= 40:
			GPIO.output(red_LED, False)
			Buzz.start(30)
			time.sleep(0.5)
			Buzz.stop()

		elif 15 <distance and  distance <= 30:
			GPIO.output(red_LED, False)
			##Buzz.ChangeFrequency(600)
			Buzz.start(30)
			time.sleep(0.2)
			Buzz.stop()

		elif distance <= 15:
			GPIO.output(red_LED, False)
			Buzz.start(30)
			time.sleep(0.05)
			Buzz.stop()

		else:
			GPIO.output(red_LED, True)
			Buzz.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
