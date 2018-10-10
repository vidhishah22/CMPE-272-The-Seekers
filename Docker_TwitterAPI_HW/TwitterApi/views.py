from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import oauth2 as oauth
from django.template import loader


def getusertweets(request):
    consumer_key = "oE5oJ3jDwGSHadbN4BK4yNYuy"
    consumer_secret = "nmlzHoqkt0tw9hLpFbWWgSzDsEYlfPeVmMlOeybHN84hmJxarn"
    access_token = "1046137456301506560-4RbRVcUt2FChkrljWF0jD06ikZyaqQ"
    access_token_secret = "l508SIOvH01kdNSuXTzmwANoZlooDJA66ndRJ8Let5nMK"

    consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
    access_token = oauth.Token(key=access_token, secret=access_token_secret)
    client = oauth.Client(consumer, access_token)

    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Seekers Tweet&count=5"
    respone, data = client.request(timeline_endpoint)
    tweets = json.loads(data)

    for tweet in tweets:
        print('Tweet id : ', tweet['id'], 'Tweet Text :', tweet['text'])

    context = {'tweet': tweets}
    return render(request, 'TwitterApi/home.html', context)
