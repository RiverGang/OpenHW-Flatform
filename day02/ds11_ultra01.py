#Ultra
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

GPIO.setmode(GPIO.BCM)
GPIO.setup(triPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
	while True:
		distance = measure()
		print("Distance: %.2f cm" %distance) ## 소숫점 둘째 자리까지 확인
		time.sleep(5)

except KeyboardInterrupt:
	GPIO.cleanup()
