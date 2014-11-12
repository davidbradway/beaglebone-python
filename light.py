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
    import numpy as np
    import matplotlib.pyplot as plt
    import collections
    import twitter
    
    # Set Flags
    plotit = 0
    debug = 0
    printit = 1
    tweetit = 1
    
    # Set ADC
    sensor_pin = 'P9_40'
    ADC.setup()

    # Set data collection buffer
    buflength = 15
    circbuf=collections.deque(maxlen=buflength)
    
    # Plot the raw data
    if plotit:
        #plt.axis([0, 1000, -.1, 1.7])
        plt.ion()
        plt.show()
    
    # Print table of data
    if debug:
        print('Time\tVolts\t\tMedian\t\tVariance\t\tStable\t\t\tnewstateflag')
    
    if tweetit:
        api = twitter.Api(consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret='')
        
        if debug:
            print api.VerifyCredentials()
    
    i = 0
    med = 0
    stable = 0
    variance = 0
    newstateflag = False

    while True:
        now = datetime.datetime.now()
        reading = ADC.read(sensor_pin)
        volts = reading * 1.800
        circbuf.append(volts)
        med = np.median(circbuf)
        variance = np.var(circbuf)
        
        if variance < 0.001:
            stable = med
            newstateflag = False
        
        if variance > 0.01 and newstateflag == False:
            if med > stable:
                update = 'Lights on  %s' % (str(now))
                if printit:
                    print(update)
                if tweetit:
                    status = api.PostUpdate(update)
                
                newstateflag = True
            elif med < stable:
                update = 'Lights off %s' % (str(now))
                if printit:
                    print(update)
                if tweetit:
                    status = api.PostUpdate(update)
                
                newstateflag = True
        
        if debug:
            print('%s\t%f\t%f\t%f\t%f\t%f' % (now.second, volts, med, variance, stable, newstateflag))
        
        if plotit:
            plt.scatter(i, med)
            plt.draw()
        
        time.sleep(.25)
        i=i+1    

if __name__ == "__main__":
    main()
