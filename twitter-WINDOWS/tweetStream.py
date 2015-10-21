#import time
from twython import TwythonStreamer
from twython import Twython
# Search terms
TERMS = 'london paris'
print('looking for ', TERMS)

# Twitter application authentication
APP_KEY = "ittMnB2nfikzmPSQurSaJDLSu"
APP_SECRET = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"
OAUTH_TOKEN = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
OAUTH_TOKEN_SECRET = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

#access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
#access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"
#consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
#consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print(data['text'].encode('utf-8'))
            print()
            #GPIO.output(LED, GPIO.HIGH)
            #time.sleep(0.5)
            #GPIO.output(LED, GPIO.LOW)

# Create streamer
try:
    print('trying.....')
    #twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    #twitter.update_status(status="Hello world.")
    
    stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track=TERMS)
    print(stream)

except KeyboardInterrupt:
    print('keyboard interupt')
        #GPIO.cleanup()
