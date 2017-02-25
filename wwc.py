import tweepy
import json
from tweepy import OAuthHandler

 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

count=0
list=[]

for friend in tweepy.Cursor(api.followers,screen_name="WWCodePune").items():
    list.append(friend._json['screen_name'])


print "Number of followers:",len(list)

for name in list:
	print name

if("YOUR USERNAME" in list):
	print "You already follow!"
else:
	print "starting to follow WWCodePune"
	api.create_friendship("WWCodePune")






