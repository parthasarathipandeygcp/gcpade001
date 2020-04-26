import os
import tweepy
import tweetPublishsm

# authorization tokens
consumer_key = os.environ['twitter_api_key']
consumer_secret = os.environ['twitter_api_secret_key']
access_key = os.environ['twitter_access_token']
access_secret = os.environ['twitter_access_token_secret']


# StreamListener class inherits from tweepy.StreamListener and overrides on_status/on_error methods.
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # if "retweeted_status" attribute exists, flag this tweet as a retweet.
        is_retweet = hasattr(status, "retweeted_status")

        # check if text has been truncated
        if hasattr(status,"extended_tweet"):
            text = status.extended_tweet["full_text"]
        else:
            text = status.text

        # check if this is a quote tweet.
        is_quote = hasattr(status, "quoted_status")
        quoted_text = ""
        if is_quote:
            # check if quoted tweet's text has been truncated before recording it
            if hasattr(status.quoted_status,"extended_tweet"):
                quoted_text = status.quoted_status.extended_tweet["full_text"]
            else:
                quoted_text = status.quoted_status.text

        # remove characters that might cause problems with csv encoding
        remove_characters = [",","\n"]
        for c in remove_characters:
            text.replace(c," ")
            quoted_text.replace(c, " ")

 #       with open("out.csv", "a", encoding='utf-8') as f:
 #           f.write("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))
        createdtime=str(status.created_at)
        tweets={'tweet_id':status.id_str,'created_at':createdtime, 'user':status.user.screen_name,'location':status.user.location, 'is_retweet': is_retweet,'is_quote':is_quote}
        print (status.id_str)
        tweetPublishsm.write_to_topic(tweets)
        #print("%s,%s,%s,%s,%s,%s\n" % (status.created_at,status.user.screen_name,is_retweet,is_quote,text,quoted_text))
    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()
    

if __name__ == "__main__":
    # complete authorization and initialize API endpoint

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener,tweet_mode='extended')
    tags = ["COVID19"]
    tweets=stream.filter(track=tags)
    