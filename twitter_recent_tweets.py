import time
import tweepy
import pandas as pd 

twitter_key = pd.read_csv('/Users/spnck/documents/twitter_api_keys.csv', header=None)

consumer_key = twitter_key[1][0]
consumer_secret_key = twitter_key[1][1]
access_token = twitter_key[1][3]
access_secret_token = twitter_key[1][4]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth, wait_on_rate_limit=True)

def search_tweets(stock_name):
    searchQuery = stock_name + '-filter:retweets'
    tweets = tweepy.Cursor(api.search, searchQuery, result_type='recent').items(1)
    
    tweet_list = [[tweet.id, tweet.favorite_count,
                   tweet.retweet_count, tweet.created_at] for tweet in tweets]
    
    #print('tweet scraped')
    return tweet_list

appl_list = []
pltr_list = []
appl_id = []
pltr_id = []

interval_count = 8000
for i in range(interval_count):
    while True:
        new_tweet_appl = search_tweets('$APPL')
        new_tweet_pltr = search_tweets('$PLTR') 
        if new_tweet_pltr[0] in pltr_id:
            print('[' + str(i) +  '] ' + 'Repeat Tweet Found...')
            time.sleep(10)
            break
        if new_tweet_appl[0] in appl_id:
            print('[' + str(i) +  '] ' + 'Repeat Tweet Found...')
            time.sleep(10)
            break
        appl_list.append(new_tweet_appl)
        pltr_list.append(new_tweet_pltr)
        appl_id.append(new_tweet_appl[0])
        pltr_id.append(new_tweet_pltr[0])
        
        print('New Tweets Added')
        
        time.sleep(10)

appl_list = [item for sublist in appl_list for item in sublist]
pltr_list = [item for sublist in pltr_list for item in sublist]
print('Done')

apple_df = pd.DataFrame(appl_list)
pltr_df = pd.DataFrame(pltr_list)
apple_df.to_csv(r'/Users/spnck/documents/appl.csv', header=False)
pltr_df.to_csv(r'/Users/spnck/documents/pltr.csv', header=False)