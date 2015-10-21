import tweepy
import datetime

access_token = "411603486-3DGQ34Z2NR4ngIkbURdmBsktWkdtNZLyaNWZfDVb"
access_token_secret = "eDVLbnNFFkzah1LvWDpx3nGrRHSzIRUXMV5lWPNWY16HJ"
consumer_key = "ittMnB2nfikzmPSQurSaJDLSu"
consumer_key_secret = "fI7MnXoIb9lArbDRQncKDY8Hqp6rZJ9E5Cgh6zPqFe1uKsygcb"

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

myStatus = "C&I Engineering " + str(datetime.datetime.now())
api.update_status(status=myStatus)


user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count) +'\n')

# Get the User object for twitter...
user = api.get_user('nickclarke444')

##Models contain the data and some helper methods which we can then use:

print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)


