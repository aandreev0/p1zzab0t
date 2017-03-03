# Import our Twitter credentials from credentials.py
import tweepy
import pprint
from secrets import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_results = api.search(q="pizza", count=100)
for i in search_results:
#i = search_results[0]
#i = api.get_status(837566335970205696)

   un = i.user.screen_name
   print un
#print [un, i.id]
   api.update_status(u'@'+un+u' '+u'\U0001F355'+u' yummy!',in_reply_to_status_id=i.id)
   
#for i in search_results:
#api.update_status(u'\U0001F355'+'qwe')
  # print i
