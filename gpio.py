import logging
import os
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
 
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
 
STATUSON = ["on", "switch on", "enable", "power on", "activate", "turn on", "kai"] # all values that are defined as synonyms in type
STATUSOFF = ["off", "switch off", "deactivate", "power off", "disable", "turn off", "guan"]
 
@ask.launch
def launch():
    speech_text = 'Welcome to the Raspberry Pi alexa automation.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)
 
@ask.intent('FanIntent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    fan_pin = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin,GPIO.OUT)
    if status in STATUSON:
        GPIO.output(fan_pin,GPIO.HIGH)
        return statement('Light was turned on')
    elif status in STATUSOFF:
        GPIO.output(fan_pin,GPIO.LOW)
        return statement('Light was turned off')
    else:
        return statement('Sorry, this command is not possible.')
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say fan on or fan off!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

