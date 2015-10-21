from twitter import *

access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"
consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_key_secret))

#t.statuses.update(status="Hello from my Python Code 3.5 CandiEngineering")

# Get your "home" timeline
#print(t.statuses.home_timeline()[0])

import json

mine = t.search.tweets(q="CandiEngineering")
print(len(mine))
print(mine['statuses'][0]['created_at'])
print(mine['statuses'][0]['user']['name'])
print(mine['statuses'][0]['user']['location'])
print(mine['statuses'][0]['user']['followers_count'])
print(mine['statuses'][0]['user']['created_at'])
print(mine['statuses'][0]['text'],'\n',mine['statuses'][0]['text'])
print(mine['statuses'][1]['text'])


    
