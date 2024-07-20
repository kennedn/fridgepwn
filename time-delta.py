import RPi.GPIO as GPIO
from time import time, sleep
import atexit

@atexit.register
def reenable_cursor():
    print('\033[?25h', end="")

PIN = 25

def cb(channel):
    global t
    global avg_v
    global count
    global min_v
    global max_v
    t[0] = time()
    if t[1] == 0:
        t[1] = t[0]
        return
    delta = t[0] - t[1]
    if min_v == 0 or delta < min_v:
        min_v = delta

    if max_v == 0 or delta > max_v:
        max_v = delta

    count += 1
    avg_v = avg_v + (delta - avg_v) / count
    line = f"avg={avg_v:.3f}\tmin={min_v:.3f}\tmax={max_v:.3f}" 
    print(line, end="\r")
    with open("time-delta.out", "w") as f:
        f.write(line)
    t = t[::-1] # reverse array

t = [0,0]
avg_v = t[0]
min_v = 0
max_v = 0 
count = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(PIN, GPIO.RISING,bouncetime=1000)
GPIO.add_event_callback(PIN, cb)
print('\033[?25l', end="") # hide cursor
while True:
    sleep(1)
