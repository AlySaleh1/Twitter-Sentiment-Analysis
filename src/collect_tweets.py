# Aly Saleh, 5th Dec 2021
# This file uses tweepy to extract tweets with specific keywords, each tweet as a json object
# The tweets are stored under data in the form of keyword.txt
# To run this script, you need to use a consumer key, consumer secret, access token, access token secret
# Info on how to get these here: https://developer.twitter.com/en/products/twitter-api
# sources: https://www.youtube.com/watch?v=ae62pHnBdAg

import tweepy
import json


# only original tweets are collected, retweets and replies are not collected
def tweets_writer_json(keyword_array, twitter_api, num_tweets):
    for keyword in keyword_array:
        output_path = '../data/' + keyword + '.txt'
        query = keyword + ' -filter:retweets AND -filter:replies'

        # cursor contains the tweets
        cursor = tweepy.Cursor(twitter_api.search_tweets, q=query, tweet_mode="extended", lang='en', result_type='recent').items(num_tweets)

        with open(output_path, 'w') as output_file:
            for tweet in cursor:
                tweet_string = json.dumps(tweet._json)
                output_file.write(tweet_string + '\n')


def main():

    # to see the logs of the API
    tweepy.debug(True)

    # if you want to use this code, add your consumer key, consumer secret, access token, access token secret
    auth = tweepy.OAuthHandler('CONSUMER KEY', 'CONSUMER SECRET')
    auth.set_access_token('ACCESS TOKEN', 'ACCESS TOKEN SECRET')

    api = tweepy.API(auth)

    # keywords200 means for each keyword, we will get 200 tweets with that keyword
    keywords200 = ['covid', 'vax', 'vaccination']
    keywords80 = ['moderna', 'astrazeneca', 'pfizer']
    keywords160 = ['vaccine']

    tweets_writer_json(keywords200, api, 200)
    tweets_writer_json(keywords80, api, 80)
    tweets_writer_json(keywords160, api, 80)


if __name__ == '__main__':
    main()
