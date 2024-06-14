from RPi import GPIO
import sys
import time

state = True
light_color_func = "all"
if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    if "=" in arg:
        light_color_func, arg = arg.split("=")
    state = arg == "true" or arg == "yes" or arg == "on"

RED_LED = 17
BLUE_LED = 27
GREEN_LED = 22
WHITE_LED = 23

#
# initialize the device
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def all(state):
    for i in range(0, 20):
        red(state)
        time.sleep(0.1)
        blue( state)
        time.sleep(0.1)
        green(state)
        time.sleep(0.1)
        white(state)
        time.sleep(0.1)
        state = not state
        white(state)
        time.sleep(0.1)
        green(state)
        time.sleep(0.1)
        blue(state)
        time.sleep(0.1)
        red(state)
        time.sleep(0.1)
        state = not state

def red(status):
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(RED_LED, status)


def blue(status):
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.output(BLUE_LED, status)


def green(status):
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.output(GREEN_LED, status)


def white(status):
    GPIO.setup(WHITE_LED, GPIO.OUT)
    GPIO.output(WHITE_LED, status)


globals()[light_color_func](state)

