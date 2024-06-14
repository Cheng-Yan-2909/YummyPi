from RPi import GPIO
import sys

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
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def all():
    red()
    blue()
    green()
    white()


def red():
    GPIO.setup(RED_LED, GPIO.OUT)
    GPIO.output(RED_LED, state)


def blue():
    GPIO.setup(BLUE_LED, GPIO.OUT)
    GPIO.output(BLUE_LED, state)


def green():
    GPIO.setup(GREEN_LED, GPIO.OUT)
    GPIO.output(GREEN_LED, state)


def white():
    GPIO.setup(WHITE_LED, GPIO.OUT)
    GPIO.output(WHITE_LED, state)


globals()[light_color_func]()

