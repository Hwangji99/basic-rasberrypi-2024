# 피에조
import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [130, 147, 165, 175, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

# 아날로그 출력을 위한 객체 생성(440Hz로 출력)
Buzz = GPIO.PWM(piezoPin, 440)

try:
  while True:
    Buzz.start(50)    # duty cycle: 50 (50의 시간을 주며 동작)
    for i in range(0, len(melody)):
      BUzz.ChangeFrequency(melody[i])
      time.sleep(0.3)
    Buzz.stop()
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
