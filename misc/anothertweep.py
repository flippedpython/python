import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"
consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
 
        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])
 
        return true
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    statuses = tweepy.Cursor(api.home_timeline).items(1)
    print('\n')
    #data = [s.text.encode('utf8') for s in statuses]
    data = [s.text for (s) in statuses]
    print('TWEET %s: \t\n\n' %(data))

    stream = Stream(auth, listener)
    stream.filter(track=['basketball'])
    #stream.filter(follow=[38744894], track=['#pythoncentral'])
