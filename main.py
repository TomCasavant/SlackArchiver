from pymongo import MongoClient
from slackclient import SlackClient
from ConfigParser import SafeConfigParser
import time

def logPreviousSlackData(API_Key):
	"""Gets all previous messages and puts them into a mongo database"""
	sc = SlackClient(API_Key)
	list = sc.api_call("channels.list")
	history = sc.api_call(
		"channels.history",
		channel ="C6UD3MMNW")
	insertDatabase(history['messages'])

def getCurrentMessages(API_Key):
	"""Actively logs messages into a mongo database"""
	sc = SlackClient(API_Key)
	if sc.rtm_connect():
		while True:
			messages= sc.rtm_read()
			time.sleep(1)
			if messages:
				insertDatabase(messages)

def printDatabase():
	"""Prints contents of database"""
	client = MongoClient()
	db = client['Slack-Database']
	collection = db['posts']
	a = collection.find({})
	for object in a:
		print object['text'], object['user']

def insertDatabase(messages):
	"""Takes messages and inserts them into a database"""
	client = MongoClient()
	db = client['Slack-Database']
	posts = db.posts
	for message in messages:
		if message['type'] == "message":
			posts.replace_one(message, message, upsert=True)
			print "Message Logged" 

if __name__ == "__main__":
	parser = SafeConfigParser()
	parser.read("config.ini") #Loads Config File to retrieve Slack API Token
	SLACK_API_TOKEN = parser.get("slack", "API_TOKEN")
#	logPreviousSlackData(SLACK_API_TOKEN)
#	printDatabase()
	getCurrentMessages(SLACK_API_TOKEN)

