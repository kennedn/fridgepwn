import RPi.GPIO as GPIO
from time import sleep

OUT_LATCH = 17
OE = 27
DS = 22
CLK = 23

# Set pin low or high
def o(pin, value):
    if pin == OUT_LATCH:
        GPIO.setup(OUT_LATCH, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH if value else GPIO.LOW)

# Read OUT_LATCH pin
def i():
    GPIO.setup(OUT_LATCH, GPIO.IN)
    return GPIO.input(OUT_LATCH) == GPIO.HIGH

# Send word of data to shift registers
def w(word):
    for i in range(16):
        o(DS, ((word) >> i) & 1)
        o(CLK, 1) 
        o(CLK, 0) 
    o(OUT_LATCH, 1) 
    o(OUT_LATCH, 0) 

# Hold button down and run function to print which bit in the word enables it
def button_detect():
    for x in range(16): 
        w(0xFFFF - (1 << x))
        print(f'Match on pin {x}\n' if i() else '', end='')
        sleep(0.01)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(OUT_LATCH, GPIO.OUT)
GPIO.setup(OE, GPIO.OUT)
GPIO.setup(DS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)

