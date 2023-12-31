from flask import Flask, request
import os
import time
import json
from RPi import GPIO
from xml.etree import ElementTree
import inspect

app = Flask(__name__)

STATUS_ON = ["on", "switch on", "enable", "power on", "activate", "turn on", "kai"]
STATUS_OFF = ["off", "switch off", "deactivate", "power off", "disable", "turn off", "guan"]


def get_speach(text):
    try:
        xml_doc = ElementTree.fromstring(text)
        if xml_doc.tag == 'speak':
            return {'type': 'SSML', 'ssml': text}
    except:
        pass

    return {'type': 'PlainText', 'text': text}

def speach(text, card_title=None, card_content=None):
    response_wrapper = {
        'version': '1.0',
        'response': {
            "shouldEndSession": True,
            "outputSpeech": get_speach(text),
            "card": {
                'type': 'Simple',
                'title': card_title,
                'content': card_content
            }
        },
        'sessionAttributes': {
            "dev": "Cheng Yan"
        }
    }

    print("=================================", flush=True)
    print(f"response: {response_wrapper}", flush=True)
    print("=================================", flush=True)
    return json.dumps(response_wrapper)


def process_alexa_request(request_data):
    print(json.dumps(request_data), flush=True)
    print("============================================", flush=True)
    fan_pin = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)

    text = "Unknown Operation"
    s = "unknown"

    if "request" in request_data:
        if "intent" in request_data["request"]:
            intent = request_data["request"]["intent"]
            if intent["name"] == "FanIntent":
                val = intent["slots"]["status"]["value"]
                if val in STATUS_ON:
                    GPIO.output(fan_pin, GPIO.HIGH)
                    text = "Fan is now on"
                    s = "on"
                elif val in STATUS_OFF:
                    GPIO.output(fan_pin, GPIO.LOW)
                    text = "Fan is now off"
                    s = "off"
                else:
                    print("unknown state")
                    text = "Not sure what to do"

        return speach(text, "Fan Status", f"Fan is currently {s}")


@app.route("/", methods=['POST', 'GET'])
def default_route():

    try:
        return process_alexa_request(request.get_json())
    except:
        pass

    return """
    Welcome Unknown dude
    """


if __name__ == '__main__':
   port = 8000
   app.run(host='127.0.0.1', port=port)






