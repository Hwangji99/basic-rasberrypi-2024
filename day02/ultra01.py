# Ultra
import RPi.GPIO as GPIO
import time

def measure():
  GPIO.output(trigPin, True)  # 10us 동안 high 레벨로 triger를 출력하여 초음파 발생 준
  time.sleep(0.00001)
  GPIO.output(trigPin, False)
  start = time.time()            # 현재시간 저장

  while GPIO.input(echoPin) == False:  # echo가 없으면
    start = time.time()                # 현재 시간을 start 변수에 저장하고
  while GPIO.input(echoPin) == True:   # echo가 있으면
    stop = time.time()                 # 현재 시간을 stop 변수에 저장
  elapsed = stop - start               # 걸린 시간을 구하고
  distance = (elapsed * 19000) / 2     # 초음파 속도를 이용해서 거리 계산

  return distance                       # 거리 반환

# 핀 설정
piezoPin = 13
trigPin = 27
echoPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

# 참조 파일 pwm01.py
# 다양한 소리를 내는게 아니기 때문에 melody랑 ChangeFrequency를 안쓴다

try:
  while True:
    distance = measure()
    print("Distance: %.2f cm" %distance)
    if distance < 50 and distance >= 40:    # 거리가 50cm 미만이 되면 
      Buzz.start(50)     # 부저가 울리기 시작한다
      Buzz.ChangeFrequency(220)
      time.sleep(0.3)
      Buzz.ChangeFrequency(360)
      time.sleep(0.3)
    elif distance < 40 and distance >= 30:
      Buzz.start(50)     # 부저가 울리기 시작한다
      Buzz.ChangeFrequency(380)
      time.sleep(0.3)
      Buzz.ChangeFrequency(440)
      time.sleep(0.3)
    elif distance < 30 and distance >= 20:
      Buzz.start(50)     # 부저가 울리기 시작한다
      Buzz.ChangeFrequency(460)
      time.sleep(0.3)
      Buzz.ChangeFrequency(500)
      time.sleep(0.3)
    elif distance < 20:
      Buzz.start(50)     # 부저가 울리기 시작한다
      Buzz.ChangeFrequency(530)
      time.sleep(0.3)
      Buzz.ChangeFrequency(600)
      time.sleep(0.3)
    else:
      Buzz.stop()        # 부저가 멈춘다
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
