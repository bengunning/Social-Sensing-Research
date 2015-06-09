#Ben Gunning
#Assignment 1
#Professor Wang
import fileinput
import json
import tweepy

consumer_key = 'g5khGWpUwzIPKMkLmVOHgV7TN'
consumer_secret = '9yGIdqDfFKz2QSuvZwf5UDb7q4ctHDP7iV2zKMXLrBTRmkki8M'
access_token = '588735535-nghcSvLrtvAYk01pg0H3raNWdiSkJFbAn67msrox'
access_token_secret = 'ZYYH2eu3fagcbrMEP0W1CijjmyyD4gWy6hBKUaQ4nKHbu'

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token , access_token_secret)

api = tweepy.API(auth)

ID_List = [34373370 , 26257166 , 12579252]

target = open('ex1.txt' , 'w')
for ID in ID_List:
	user = api.get_user(ID)
	target.write("Screen Name: %s\n" % user.screen_name)
	target.write("User Name: %s\n" % user.name)
	target.write("User Location: %s\n" % user.location)
	target.write("User Description: %s\n" % user.description)
	target.write("Number of followers: %i\n" % user.followers_count)
	target.write("Number of friends: %i\n" % user.friends_count)
	target.write("Number of statuses: %i\n" % user.statuses_count)
	target.write("User URL: %s\n\n" % user.url)
target.close()

target = open('ex2.txt' , 'w')
for ID in ID_List:
	user = api.get_user(ID)
	target.write("User: %i\n" % user.id)
	target.write("The Followers List\n")
	user_cursor = tweepy.Cursor(api.followers , screen_name = user.screen_name).items()
	for num in range(0,30):
		try:
			follower = next(user)
			target.write("%s\n" % follower.screen_name)
		except:
			print(num)
			break
	target.write("\nThe Friends List\n")
	user_cursor = tweepy.Cursor(api.friends , screen_name = user.screen_name).items()
	for num in range(0,30):
		try:
			friend = next(user)
			target.write("%s\n" % friend.screen_name)
		except:
			print (num)
			break
	target.write("\n")
target.close()

target = open('ex3.txt' , 'w')

target.close()