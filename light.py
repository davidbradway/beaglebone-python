#!/usr/bin/python
"""
light.py

Read analog values from the photoresistor

=======
run with:
    sudo ./light.py

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


def main():
    import Adafruit_BBIO.ADC as ADC
    import time
    import datetime
    
    sensor_pin = 'P9_40'
    
    ADC.setup()
    
    print('Time\tReading\t\tVolts')
    
    while True:
        now = datetime.datetime.now()
        reading = ADC.read(sensor_pin)
        volts = reading * 1.800
        print('%s\t%f\t%f' % (now.second, reading, volts))
        time.sleep(1)

if __name__ == "__main__":
    main()
