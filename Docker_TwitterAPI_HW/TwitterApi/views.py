from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import oauth2 as oauth
from django.template import loader
from .apps import TwitterapiConfig


def index(request):
    return render(request,'TwitterApi/base.html')


# Authorize tokens and call api
def call_twitter_api(endpoint):
    oauth_consumer = oauth.Consumer(key=TwitterapiConfig.consumer_key, secret=TwitterapiConfig.consumer_secret)
    oauth_token = oauth.Token(key=TwitterapiConfig.access_token, secret=TwitterapiConfig.access_token_secret)
    print (oauth_token)
    client = oauth.Client(oauth_consumer, oauth_token)

    response, data = client.request(endpoint)
    return json.loads(data)


# Get Status User Timeline
def get_user_tweets(request):
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Seekers Tweet&count=20"
    tweets = call_twitter_api(timeline_endpoint)
    for tweet in tweets:
        print('Tweet id : ', tweet['id'], 'Tweet Text :', tweet['text'])

    context = {'tweet': tweets}
    return render(request, 'TwitterApi/getusertweet.html', context)


# Get Status Mention Timeline
def get_mention_tweets(request):
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/mentions_timeline.json?count=20"
    mentions = call_twitter_api(timeline_endpoint)
    for usermention in mentions:
        print('Mention id : ', usermention['id'], 'Mention Text :', usermention['text'])

    context = {'usermention': mentions}
    return render(request, 'TwitterApi/getmentionstweet.html', context)


# Get Status Based On Tweet Id
def get_id_based_tweets(request):
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/show.json?id=1049869614321000448"
    id_tweets = call_twitter_api(timeline_endpoint)

    context = {'id_tweet': id_tweets}
    # print(render(request, 'TwitterApi/getidbasedtweet.html', context).status_code)
    return render(request, 'TwitterApi/getidbasedtweet.html', context)