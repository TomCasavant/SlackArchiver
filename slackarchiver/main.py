from ConfigParser import SafeConfigParser
import time
from pymongo import MongoClient
from slackclient import SlackClient
import os

def log_previous_slack_data(slackclient, mongoclient):
    """Gets all previous messages and puts them into a mongo database"""
    channels = slackclient.api_call("channels.list")['channels']

    for channel in channels:

        history = slackclient.api_call(
            "channels.history",
            channel=channel['id'])
        insert_database(history['messages'], mongoclient)


def start_listening(slackclient, mongoclient):
    """Actively logs messages into a mongo database"""
    if slackclient.rtm_connect():
        while True:
            messages = slackclient.rtm_read()
            if messages:
                insert_database(messages, mongoclient)
            time.sleep(1)
    else:
        print "Unable to connect"


def print_database(client):
    """Prints contents of database"""
    database = client['Slack-Database']
    collection = database['posts']
    find_all = collection.find({})
    for document in find_all:
#        print document['text'], document['user']
        print document

def insert_database(messages, client):
    """Takes messages and inserts them into a database"""
    database = client['Slack-Database']
    posts = database.posts
    for message in messages:
        if message['type'] == "message":
            posts.replace_one(message, message, upsert=True)
            print "Message Logged"


if __name__ == "__main__":
    parser = SafeConfigParser()
    parser.read(os.environ['CONIFG'])  # Loads Config File to retrieve Slack API Token
    SLACK_API_TOKEN = parser.get("slack", "API_TOKEN")

    mongo = MongoClient()
    slack = SlackClient(SLACK_API_TOKEN)

    #log_previous_slack_data(slack, mongo)
    #print_database(mongo)
    start_listening(slack, mongo)
