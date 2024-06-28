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

    - 스위치 (**플로팅현상때문에 반드시 풀업or풀다운 형태로 연결**)
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
        - python -m venv (--system-site-packages)env
        - 괄호: 운영체제가 가진 라이브러리를 포함하는 옵션
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

    ![릴레이모듈](https://raw.githubusercontent.com/RiverGang/OpenHW-Flatform/main/images/img01.png)
    - 5VDC -> 5V 직류구동
    - 10A 250VAC -> 10A 250V 교류 연결 가능

    - NC: Nomal Close (접점이 닫혀져있음)
    - NO: Nomal Open (접점이 열려있음)
    - COM: 공통단자

    - VCC(+),GND(-),IN(Singnal) -> 릴레이(전자석)을 구동하기 위한 전력 단자 및 신호 단자
    
    ![전자석원리](https://raw.githubusercontent.com/RiverGang/OpenHW-Flatform/main/images/img02.png)
    - 코일에 전류가 흐르면 자성이 생겨 (=전자석) NO의 접점이 닫히고, NC의 접점이 열리게 된다

    - 릴레이에 전류가 흐를 때 어떤 부품을 동작 or 전류 인가 => NO연결
    - 평상시 부품에 전류를 계속 인가하고 릴레이에 전류가 흐를 때 차단 => NO 연결

- 스텝모터 모듈 / 모터 드라이버
    - 스텝모터가 돌아가는 반복문 알고리즘 작성

- Flask 활용 웹서버 가동
    ```python
    app.run(host="0.0.0.0", port="10111", debug=True)
    ## host: 외부 아이피에서 접속하도록 설정
    ## port: 포트번호 지정 (생략가능)
    ## debug=True: 수정된 코드를 실시간으로 서버에 반영
    ```

    - (ds19)웹을 통해 LED on/off 제어하기
    - get 형태로 파라미터(인자값) 받기
    
    ```python
    (flask.)request.args.get('text')
    # text라는 Key의 Value 값 가져오기
    # URL:port/?text=boom!! 형태의 주소를 입력하면
    # boom!!이 가져와짐
    ```

## 4일차
- RPi 스위치로 카메라모듈 동작 및 이미지 파일로 저장
    ```python
    from picamera2 import Picamera2
    # picamera2 라이브러리의 Picamera2 클래스
    ```
- 7-세그먼트 모듈 사용

    ![7-세그먼트](https://raw.githubusercontent.com/RiverGang/OpenHW-Flatform/main/images/img03.png)

    - 공통 양극(Common Anode)방식: 공통 단자(COM1,2,3,4)에 (+)신호, 데이터 신호(a~g, dp) (-)마이너스 => LED ON
    <->
    - 공통 음극(Common Cathod)방식: 공통 단자 (-), 데이터 신호 (+)
    
    - 0~9까지 1초마다 숫자 점등하기
    - 버튼을 클릭할 때마다 0~9 카운트하기
 
 ## 5일차
 - 4 Digit 7-세그먼트 모듈
    - 각 COM 단자가 차례로 하나씩 빠르게 ON/OFF되면 그 잔상이 동시에 표기된 것처럼 보이게 됨
    - COM 입력 단자 별 저항연결
        - (ds26) 1234 동시에 표시
        - (ds27) 키보드 입력 값을 화면에 표시하기
        - (ds28) 1~9999까지 숫자 카운트

## 6일차
- PyQt5 설치 (pip install PyQt5)
- vncserver 바탕화면에 PyQt5 설치
    - vncserver-virtual (putty에서 vnc서버 열기)
    - sudo apt install qttools5-dev-tools

- Qt Designer
    - GUI 레이아웃 구성
    - PyQt5 라이브러리 이용 -> 이벤트와 함수 설정
        - Qt Designer에서 Edit Signal/Slots을 이용해 이벤트와 함수 연결 시 Python에서 클래스 생성자 내에 이벤트핸들러 연결하지 않아도 됨, 함수만 정의

## 7일차
- Qt Designer 이용한 GUI RPi제어 개인 토이 프로젝트
    -  GUI 제어 알람시계
        - 기능
            - GUI
            1. 현재 시간 확인
            2. 알람 시간 설정
            3. 벨소리 선택
            4. LED 색상 선택
            5. 알람 반복 횟수 선택

            - RPi
            1. 현재 시간 출력
            2. LED 불빛 출력
            3. 부저 소리 출력
        
        - 사용 모듈
            - LED
            - 부저
            - 4Digit 7-segments

    - 수정사항
        - [] 아이콘변경
        - [] 알람 설정 정보 하단 창에 띄우기 
        - [] 알람 저장 시, 설정들 초기화하기
        - [] 스위치 이용, 알람 끄기
        - [] 화면 꾸미기
            - 참고 링크
            - https://life-of-panda.tistory.com/72
            