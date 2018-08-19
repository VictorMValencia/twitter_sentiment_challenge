import csv as csv
import tweepy
from textblob import TextBlob

consumer_key = 'fbaehYi72cXGxNz2gh6UzCizS'
consumer_secret = 'Vb61KpHu7SeniXKdGvkiTe08JOfY1fAV4Cgjza9SwBHfqU6tM7'

access_token = '1967823085-Pts7UqTPeRII3zg5tgMqp6e6oudg48AmYQcWcBL'
access_token_secret ='zUo9ImcfCfEDGSowgPZpcTvUp7Wc3ymt1VUzs8Hv4OfYr'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

def get_label(analysis, threshold = 0):
    if analysis.sentiment[0]>threshold:
        return 'Positive'
    else:
        return 'Negative'

with open('sentiment.csv', 'w',  newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['Tweet','Sentiment Polarity'])

    for tweets in public_tweets:
        ##print(tweets.text)
        analysis = TextBlob(tweets.text)
        writer.writerow([tweets.text,get_label(analysis)])
