from flask import Flask, request
import os
import time
import json
import RPi.GPIO as GPIO


app = Flask(__name__)

STATUSON = ["on", "switch on", "enable", "power on", "activate", "turn on", "kai"] 
STATUSOFF = ["off", "switch off", "deactivate", "power off", "disable", "turn off", "guan"]


@app.route("/", methods=['POST', 'GET'])
def default_route():
    request_data = request.get_json()
    print( json.dumps(request_data), flush=True )
    print("============================================", flush=True)
    fan_pin = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin,GPIO.OUT)

    if "intent" in request_data["request"]:
        intent = request_data["request"]["intent"]
        if intent["name"] == "FanIntent":
            val = intent["slots"]["status"]["value"]
            if val in STATUSON:
                GPIO.output(fan_pin,GPIO.HIGH)
                print("Fan is on")
            elif val in STATUSOFF:
                GPIO.output(fan_pin,GPIO.LOW)
                print("Fan is off")
            else:
                print("unknown state")
   

    return "hello", 200




if __name__ == '__main__':
   port = 80
   app.run(host='127.0.0.1', port=80)












