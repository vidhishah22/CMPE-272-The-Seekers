from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import oauth2 as oauth
from django.template import loader
from .apps import TwitterapiConfig


def index(request):
    return render(request, 'TwitterApi/home.html')


# Authorize tokens and call api
def call_twitter_api(endpoint):
    oauth_consumer = oauth.Consumer(key=TwitterapiConfig.consumer_key, secret=TwitterapiConfig.consumer_secret)
    oauth_token = oauth.Token(key=TwitterapiConfig.access_token, secret=TwitterapiConfig.access_token_secret)
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

    print('\nTweet Id : ', id_tweets['id'], '\nTweet : ', id_tweets['text'], '\nTweet ScreenName : ',
          id_tweets['user']['screen_name'], '\nTweet Created At : ', id_tweets['user']['created_at'])
    context = {'id_tweet': id_tweets}
    return render(request, 'TwitterApi/getidbasedtweet.html', context)


# Get Friends list
def get_friends(request):
    timeline_endpoint = "https://api.twitter.com/1.1/friends/list.json?cursor=-1&screen_name=Seekers " \
                        "Tweet&skip_status=true&include_user_entities=false "
    friends_list = call_twitter_api(timeline_endpoint)

    for friends in friends_list['users']:
        print('\nid : ', friends['id'], '\nName : ', friends['name'], '\nScreen Name : ', friends['screen_name'],
              '\nLocation : ', friends['location'], '\nFollowers Count : ', friends['followers_count'],
              '\nFriends Count : ', friends['friends_count'], '\nListed Count : ', friends['listed_count'],
              '\nFavourites Count : ', friends['favourites_count'])

    context = {'friends': friends_list['users']}
    return render(request, 'TwitterApi/getfriends.html', context)


# Get Followers list
def get_followers(request):
    timeline_endpoint = "https://api.twitter.com/1.1/followers/list.json?cursor=-1&screen_name=Seekers " \
                        "Tweet&skip_status=true&include_user_entities=false "
    followers_list = call_twitter_api(timeline_endpoint)

    for followers in followers_list['users']:
        print('\nid : ', followers['id'], '\nName : ', followers['name'], '\nScreen Name : ', followers['screen_name'],
              '\nLocation : ', followers['location'], '\nFollowers Count : ', followers['followers_count'],
              '\nFriends Count : ', followers['friends_count'], '\nListed Count : ', followers['listed_count'],
              '\nFavourites Count : ', followers['favourites_count'])

    context = {'followers': followers_list['users']}
    return render(request, 'TwitterApi/getfollowers.html', context)


# Get Account Settings
def get_account_settings(request):
    timeline_endpoint = "https://api.twitter.com/1.1/account/settings.json"
    account_settings_list = call_twitter_api(timeline_endpoint)
    print('\n','Screen Name : ',account_settings_list['screen_name'],
          '\n Geo Enabled : ',account_settings_list['geo_enabled'],'\n Language :', account_settings_list['language'],
          '\n Discoverable_by_email :', account_settings_list['discoverable_by_email'],
          '\n Discoverable_by_mobile_phone :', account_settings_list['discoverable_by_mobile_phone'])

    context = {'account_settings': account_settings_list}
    return render(request, 'TwitterApi/getaccountsettings.html', context)


# Get Twitters Privacy Policy
def get_privacy_policy(request):
    timeline_endpoint = "https://api.twitter.com/1.1/help/privacy.json"
    privacy_policy_list = call_twitter_api(timeline_endpoint)
    print("Twitter Privacy Policy\n", privacy_policy_list['privacy'])
    context = {'privacy_policy': privacy_policy_list}
    return render(request, 'TwitterApi/getprivacypolicy.html', context)


# Get Twitters Terms of Service
def get_terms_of_service(request):
    timeline_endpoint = "https://api.twitter.com/1.1/help/tos.json"
    terms_of_service_list = call_twitter_api(timeline_endpoint)
    print("Twitter Terms of Service\n", terms_of_service_list['tos'])
    context = {'terms_of_service': terms_of_service_list}
    return render(request, 'TwitterApi/gettermsofservice.html', context)