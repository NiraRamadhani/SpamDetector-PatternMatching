import tweepy
import json

class Tweet :
    def __init__(self, filename) :
        credentials = json.load(open(filename))
        auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
        auth.set_access_token(credentials['access_token'], credentials['access_secret'])

        self.api = tweepy.API(auth)

    def process_tweets(self, tweets_with_status) :
        tweets = []
        for tweet in tweets_with_status :
            tweets.append(tweet.full_text)

        json_tweets = dict()
        json_tweets['full_text'] = tweets

        return json_tweets

    def search_timeline(self, username, count = 20) :
        timeline = self.api.user_timeline(screen_name = username, count = count, tweet_mode = 'extended')
        tweets = self.process_tweets(timeline)

        return tweets

    def search_region(self, region, count = 20) :
        place = self.api.geo_search(query = region)
        place_id = place[0].id
        query = 'place:' + place_id
        region_tweets = self.api.search(q = query, count = count, tweet_mode = 'extended')
        tweets = self.process_tweets(region_tweets)

        return tweets

