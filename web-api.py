# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain

from _future_ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import flask
from flask import request

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Initial test drive the servo motor. Will only test drive servo motor 0 and motor 1. If you need to test drive more servo motor, just add in more line.

print('Test drive the servo motor')
pwm.set_pwm(0, 0, servo_min)
time.sleep(1)
pwm.set_pwm(0, 0, servo_max)
time.sleep(1)
pwm.set_pwm(0, 0, servo_min)
time.sleep(1)
pwm.set_pwm(1, 0, servo_min)
time.sleep(1)
pwm.set_pwm(1, 0, servo_max)
time.sleep(1)
pwm.set_pwm(1, 0, servo_min)
time.sleep(1)

app = flask.Flask(_name_)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/servo', methods=['GET'])
def api_all():
    query_parameters = request.args

    id = int(query_parameters.get('id'))
    pwm.set_pwm(id, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(id, 0, servo_max)
    return "Completed"

print('Web API is ready now, press Ctrl-C to quit...')
app.run(host="0.0.0.0")
