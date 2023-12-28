from RPi import GPIO
import sys
import time

all_out = [ 23, 24, 17, 27 ]
state = True
port = 23

if len(sys.argv) > 1:
    arg = sys.argv[1].lower()
    state = arg == "true" or arg == "yes" or arg == "on"


if len(sys.argv) > 2:
    arg = int(sys.argv[2])
    print(f"port arg is '{arg}'")
    if arg in all_out:
        port = arg
    else:
        print(f"... '{arg}' not in {all_out}")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for w in all_out:
    GPIO.setup(w, GPIO.OUT)
    GPIO.output(w, False)

print(f"port: {port} is set to {state}")
GPIO.output(port, state)

