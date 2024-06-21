import RPi.GPIO as GPIO

led = 21

#GPIO를 BCM 모드로 설정
GPIO.setmode(GPIO.BCM)

GPIO.setup(led, GPIO.OUT) ## 21번 핀을 출력으로 사용 (입출력 설정)

try:
	while True:
		GPIO.output(led, False) ## VCC에 5V의 전압이 공급되고 있기에 R 단자에는 0V가 공급되어야 전류가 흐름

except KeyboardInterrupt: ## Ctrl + c 키보드 입력 시 프로그램 종료
	GPIO.cleanup() ## 프로그램 종료 시키며 핀 초기화
