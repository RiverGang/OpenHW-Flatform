# OpenHW-Flatform
IoT 개발자 오픈하드웨어 플랫폼 학습

## day01

- 물리적인 핀 번호(5)와 프로그래밍적 핀 번호(GPIO3)는 다름
- Python GPIO 함수
    
    ```python
    # GPIO 설정함수
    
    ## 모드 설정
    GPIO.setmode(GPIO.BOARD) ## wPI 모드
    GPIO.setmode(GPIO.BCM) ## BCM 모드 프로그래밍적 핀 번호(초록글자) 모드로 설정
    
    ## 입출력 형태 지정
    GPIO.setup(channel, GPIO.mode)
    ## channel: 핀번호
    ## mode: 입출력 설정 (IN/OUT)
    
    GPIO.cleanup() ## 핀 초기화
    
    # GPIO 출력함수
    GPIO.output(channel, state)
    ## channel: 핀번호
    ## state: HIGL/LOW or 1/0 or True/False
    
    # GPIO 입력함수
    GPIO.input(channel)
    ## channel: 핀번호
    
    # 시간 지연함수
    time.sleep(secs)
    ```
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/e1e49949-7674-4cfb-90f5-017aceee7918/964ee39b-140d-4381-a838-f520572027a7/Untitled.png)
    
- 핀은 레지스터와 연결되어 있고,  HIGH(= Vcc, 5V) or LOW(= Gnd, 0V)의 비트 값 저장
- 전기 공급 → 전류 흐름 → 동작

- 하드웨어 설계 기본 법칙
    - 옴의 법칙(V=IR)
        - 전류(I): 전하의 흐름
        - 전압(V)
        - 저항
    - 키르히호프의 법칙
        - 전압 법칙
        - 전류 법칙
    - 플로팅 상태

    - 스위치
        - 풀업저항 (저항이 VCC 쪽에 연결)
            - 스위치를 누르지 않으면 VCC 값(= 1)이 그대로 레지스터(=입력)에 들어감
        - 풀다운 저항 (저항이 GND 쪽에 연결)
            - 스위치 off: 입력 핀에 0V(=0) (VCC의 전압이 인가되지 않음)
            - 스위치 on : VCC에서 공급되는 전압이 전항에 막혀 입력 핀에 전류가 흘러들어감 (5V)

- 스위치 클릭 마다 LED 색 변경
- 키보드 입력 값(1~8)마다 정음계 (도~시) 부저 소리 출력

## 2일차
- 파이썬 가상환경 생성
    - env 라는 폴더에 가상환경 생성
        - python -m venv env
    - 가상환경 접속
        - source ./env/bin/activate 
    - 가상환경 종료
        - deactivate

    - 가상환경에 라즈베리파이 설치
        - sudo pip install RPi.GPIO
    
    - 라즈베리파이 핀의 전류 상태 확인
    - sudo git clone https://github.com/WiringPi/WiringPi
    - cd WiringPi 에서 sudo ./build
    - gpio readall
    - Name(Pin), V(핀 상황)

- 적외선 센서 인체행동 감지 시 LED ON
- 초음파 거리측정 센서
    - 목적지에 도달하고 다시 되돌아오는 왕복 => % 2
- 충돌 방지 시스템 일정 거리만큼 다가오면 (가깝게 다가 올 수록) 부저 소리 빠르게 울리기

## 3일차
- 릴레이(Relay) 모듈: 라즈베리/아두이노에서 제공하는 전력만으로 구동할 수 없는 외부기기를 컨트롤하고 싶을 때 외부 전원을 릴레이와 연결하여 조건이 만족할 때 아두이노에서 신호를 보내 컨트롤