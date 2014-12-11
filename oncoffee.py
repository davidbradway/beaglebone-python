#!/usr/bin/python
"""
coffee.py

Library for making coffee

=======
run with:
    sudo ./coffee.py

Copyright 2014 David P. Bradway (dpb6@duke.edu)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__author__ = "David Bradway"
__email__ = "dpb6@duke.edu"
__license__ = "Apache v2.0"

import Adafruit_BBIO.GPIO as GPIO
import time

isSetup = False

def setup():
    GPIO.setup("P9_11", GPIO.OUT)
    isSetup = True

def loop():
    time.sleep(.5)

def on():
    if not isSetup:
        setup()
    GPIO.output("P9_11", GPIO.HIGH)

def off():
    if not isSetup:
        setup()
    GPIO.output("P9_11", GPIO.LOW)

def start():
    on()

def stop():
    off()

def brew():
    on()

if __name__ == "__main__":
    setup()
    brew()
    while True:
        loop()
