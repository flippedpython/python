# tbis worked 14/10/15

from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import pyupm_servo as servo 
import time, sys, signal, atexit
import pyupm_my9221 as upmMy9221

# Instantiate a MY9221, we use D2 for the data, and D3 for the
# data clock.  This was tested with a Grove LED bar.
myLEDBar = upmMy9221.MY9221(2, 3)

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"

# Exit handlers
def SIGINTHandler(signum, frame):
    raise SystemExit

def exitHandler():
    myLEDBar.setBarLevel(0, True)
    print('Exiting')
    sys.exit(0)

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        if ('servo' in data):
            myLEDBar.setBarLevel(10, directionBool)
            
            print('servo')
            
            # Set the servo arm to 90 degrees
            gServo.setAngle(90)
            print 'Set angle to 90'
            time.sleep(1)
            print 'Set angle to 0'
            gServo.setAngle(180)
            myLEDBar.setBarLevel(0, directionBool)
                                 
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()

    # Create the servo object using D5
    gServo = servo.ES08A(5)
    gServo.setAngle(0)

    # This function lets you run code on exit
    atexit.register(exitHandler)
    # This function stops python from printing a stacktrace when you hit control-C
    signal.signal(signal.SIGINT, SIGINTHandler)
    myLEDBar.setBarLevel(0, directionBool)
    
    directionBool = True
    level = 1

    auth = OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['candiEngineering'])
