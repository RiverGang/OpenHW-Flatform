import RPi.GPIO as GPIO
import time

# 0~9까지 1byte hex값
fndDatas = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x82, 0xD8, 0x80, 0x90]
# a~g led pin
fndSeqs = [5,6,13,19,26,16,20]
# fnd(=com) 선택 pin
fndSels = [17, 27, 22, 4]


## GPIO 설정
GPIO.setmode(GPIO.BCM)
for fndseq in fndSeqs:
	GPIO.setup(fndseq, GPIO.OUT)
	GPIO.output(fndseq, True) ## a~g LED off 초기화, True -> LED 꺼짐

for fndsel in fndSels:
	GPIO.setup(fndsel, GPIO.OUT)
	GPIO.setup(fndsel, False) # COM 단자에 VCC가 들어가야 됨

def fndOut(data): # 숫자 형태를 만드는 함수
	for i in range(0, 7):
		GPIO.output (fndSeqs[i], fndDatas[data] & (0x01 << i)) ## & 비트연산 => A와 B가 모두 1이어야만 1, i 만큼 좌측 쉬프트 연산(<<)

try:
	#GPIO.cleanup()
	GPIO.output(17, True)
	GPIO.output(5, False)

except KeyboardInterrupt:
	GPIO.cleanup()
