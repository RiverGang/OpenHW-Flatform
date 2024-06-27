import RPi.GPIO as GPIO
import time

# 0~9까�? 1byte hex�?
fndDatas = [0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xD8, 0x80, 0x90] # Anode
fndSegs = [5,6,13,19,26,16,20]
fndSels = [17,27, 22, 4]
count = 0

GPIO.setmode(GPIO.BCM)
for fndSeg in fndSegs:
   GPIO.setup(fndSeg,GPIO.OUT)
   GPIO.output(fndSeg, 1)

for fndSel in fndSels:
   GPIO.setup(fndSel, GPIO.OUT)
   GPIO.output(fndSel, 0)

def findOut(data,sel):
   for i in range(0,7):
      GPIO.output(fndSegs[i], fndDatas[data] & (0x01 << i))
      for j in range(0,4):
         if j==sel:
            GPIO.output(fndSels[j],1)
         else:
            GPIO.output(fndSels[j],0)
try:
   while True:
      count += 1
      if count == 9999:
         count = 0
      
      d1000 = count / 1000
      d100 = count % 1000 /100
      d10 = count % 100  /10
      d1 = count % 10
      d = [d1000,d100,d10,d1]
      for i in range(3,-1,-1):
         findOut(int(d[i]),i)
         time.sleep(0.005)

except KeyboardInterrupt:
   GPIO.cleanup()
