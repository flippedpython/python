from twitter import *
import datetime

access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"
consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_key_secret))

message = "Hello from Intel Edison CandiEngineering " + str(datetime.datetime.now())
print(message)

t.statuses.update(status=message)

