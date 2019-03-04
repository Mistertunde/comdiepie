import tweepy
import time
print("This is my Twitter Bot")
# NOTE:  my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.

CONSUMER_KEY ='DIp1eQbA5SaaSpodEe8TdMaMY'
CONSUMER_SECRET= 'GsORMdIgWOFfUdwOUgvyiSFPiLq1viHVXParg0mWcXZoj7b01L'
ACCESS_KEY='1100173195313926145-lNL4UkoS3NkoYtaEhMPVnHpATSqNnc'
ACCESS_SECRET='zrHF5xNYAImttSeHYtZ0ADhzChzrnY449D27GfUrmBke9'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# mentions = api.mentions_timeline()
# for mention in mentions:
#print(str(mention.id) + '-' +  mention.text)
#if '#helloworld' in mention.text.lower():
#     print("found Hello World")
#     print("responding back....")


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("Replying to tweets........")
    #first tweet id  1101567997150482434 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                             last_seen_id,
                             tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
            '#HelloWorld back to you!', mention.id)
            api.retweet(last_seen_id)
while True:
    reply_to_tweets()
    time.sleep(10)
