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
YELLOW_LED = 24

#
# initialize the device
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



def all(state):
    for i in range(0, 2):
        blueon(state, 1)
        blueon(state, 1)
        blueon(state, 3)
        blueon(state, 1)
        blueon(state, 1)
        blueon(state, 3)
        blueon(state, 1)
        redon(state, 1)
        whiteon(state, 1)
        greenon(state, 1)
        blueon(state, 1)
        time.sleep(3)
        redon(state, 1)
        redon(state, 1)
        redon(state, 1)
        redon(state, 1)
        redon(state, 1)
        blueon(state, 1)
        blueon(state, 1)
        blueon(state, 1)
        blueon(state, 1)
        greenon(state, 1)
        greenon(state, 1)
        blueon(state, 1)
        greenon(state, 1)
        redon(state, 1)








# red(state)
#         red(state)
#         time.sleep(0.1)
#         blue( state)
#         time.sleep(0.1)
#         green(state)
#         time.sleep(0.1)
#         white(state)
#         time.sleep(0.1)
#         state = not state
#         white(state)
#         time.sleep(0.1)
#         green(state)
#         time.sleep(0.1)
#         blue(state)
#         time.sleep(0.1)
#         red(state)
#         time.sleep(0.1)
#         state = not state


def redon(state, _time):
    red(state)
    time.sleep(_time)
    red(not state)


def blueon(state, _time):
    blue(state)
    time.sleep(_time)
    blue(not state)


def greenon(state, _time):
    green(state)
    time.sleep(_time)
    green(not state)


def whiteon(state, _time):
    white(state)
    time.sleep(_time)
    white(not state)

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


def yellow(status):
    GPIO.setup(YELLOW_LED, GPIO.OUT)
    GPIO.output(YELLOW_LED, status)


globals()[light_color_func](state)

