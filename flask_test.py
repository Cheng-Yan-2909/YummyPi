from flask import Flask, request
import os
import time
import json
from RPi import GPIO
from xml.etree import ElementTree
import inspect

true = True
false = False


app = Flask(__name__)

STATUS_ON = ["on", "switch on", "enable", "power on", "activate", "turn on", "kai"]
STATUS_OFF = ["off", "switch off", "deactivate", "power off", "disable", "turn off", "guan"]
user_id_file = "/tmp/user_id"

def get_speach(text):
    try:
        xml_doc = ElementTree.fromstring(text)
        if xml_doc.tag == 'speak':
            return {'type': 'SSML', 'ssml': text}
    except:
        pass

    return {'type': 'PlainText', 'text': text}

def speach(text, card_title=None, card_content=None, endSession=True):
    print("=========== speach response ==============", flush=True)
    print(text, flush=True)
    print("==========================================", flush=True)

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
    print(f"response: {json.dumps(response_wrapper, indent=4)}", flush=True)
    print("=================================", flush=True)
    return json.dumps(response_wrapper)


def fan_intent(val):
    fan_pin = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT)

    if val in STATUS_ON:
        GPIO.output(fan_pin, GPIO.HIGH)
        text = "Fan is now on"
        s = "on"
    elif val in STATUS_OFF:
        GPIO.output(fan_pin, GPIO.LOW)
        text = "Fan is now off"
        s = "off"
    else:
        text = f"Unknown FanIntent value {val}"

    return speach(text, "Fan Status", f"Fan is currently {s}")


def device_intent(val):
    pass


def get_user_id(request_data):
    user_id = None
    if "session" in request_data:
        try:
            user_id = request_data["session"]["user"]["userId"]
            print(f"[DEBUG] user id from session: {user_id}")
        except:
            user_id = None

    if user_id is None and "context" in request_data:
        try:
            user_id = request_data["context"]["System"]["user"]["userId"]
            print(f"[DEBUG] user id from context: {user_id}")
        except:
            user_id = None

    return user_id

def save_user_id(request_data):
    user_id = get_user_id(request_data)
    print(f"[debug] saving user id: {user_id}")
    if user_id is not None:
        with open(user_id_file, "w") as w:
            w.write(user_id)
            w.close()


def check_user_id(request_data):
    user_id = None
    if os.path.exists(user_id_file):
        with open(user_id_file) as r:
            user_id = r.read()
            r.close()

        print(f"[DEBUG] saved user id: {user_id}")

        if user_id == get_user_id(request_data):
            return True

        return false

def process_alexa_request(request_data):
    print("============== Request Data ================", flush=True)
    print(json.dumps(request_data, indent=4), flush=True)
    print("============================================", flush=True)


    text = "Unknown Operation"
    s = "unknown"

    if "request" in request_data:
        if "intent" in request_data["request"]:
            intent = request_data["request"]["intent"]
            val = intent["slots"]["status"]["value"]
            if val == "FanIntent":
                return fan_intent(val)

            elif val == "DeviceIntent":
                return device_intent(val)

            else:
                text = f"Not sure what to do with intent {intent['name']}"
                return speach(text, "Fan Status", f"Fan is currently {s}")

        elif "type" in request_data["request"]:
            t = request_data["request"]["type"]
            if "LaunchRequest" == request_data["request"]["type"]:
                save_user_id(request_data)

            if not check_user_id(request_data):
                return "Bad Request", 400

            print(f"================= request type: {t} ====================", flush=True)
            return speach(f"Daniel Toy is {t}", "Fan Status", "Fan initialized", False)

        else:
            print("==================== unknown request ==================", flush=True)

    else:
        print("================= no 'request' found ====================", flush=True)

    return "Bad Request", 400


def home_page():
    return """
        Welcome Unknown dude
    """, 200

@app.route("/", methods=['POST', 'GET'])
def default_route():

    try:
        return process_alexa_request(request.get_json())
    except:
        pass

    return home_page()


if __name__ == '__main__':
    if os.path.exists(user_id_file):
        print(f"Removing existing user id file: {user_id_file}", flush=True)
        os.remove(user_id_file)
    port = 8000
    app.run(host='127.0.0.1', port=port)






