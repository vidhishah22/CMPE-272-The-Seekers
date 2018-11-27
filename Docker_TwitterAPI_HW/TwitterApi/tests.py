"""
@Authors: Pragya Gautam, Reetika Goel
@Purpose: It contains Unit test cases for 8 Twitter API implemented
"""

import unittest
from django.test.client import RequestFactory
from .views import *


class SimpleTest(unittest.TestCase):

    #export DJANGO_SETTINGS_MODULE=TwitterApi.settings

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_get_user_tweets(self):
        print("TC1: Get User Tweets Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output1 = get_user_tweets(request)
        self.assertEqual(output1.status_code, 200)

    def test_get_mention_tweets(self):
        print("TC2: Get Mention Tweets Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output2 = get_mention_tweets(request)
        self.assertEqual(output2.status_code, 200)

    def test_get_id_based_tweets(self):
        print("TC3: Get ID based Tweets Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output3 = get_id_based_tweets(request)
        self.assertEqual(output3.status_code, 200)

    def test_get_friends(self):
        print("TC4: Get Friends Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output4 = get_friends(request)
        self.assertEqual(output4.status_code, 200)

    def test_get_followers(self):
        print("TC5: Get Followers Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output5 = get_followers(request)
        self.assertEqual(output5.status_code, 200)

    def test_get_account_settings(self):
        print("TC6: Get Account Settings Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output6 = get_account_settings(request)
        self.assertEqual(output6.status_code, 200)

    def test_get_privacy_policy(self):
        print("TC7: Get Privacy Policy Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output7 = get_privacy_policy(request)
        self.assertEqual(output7.status_code, 200)

    def test_get_terms_of_service(self):
        print("TC8: Get Privacy Policy Unit Test")
        request = self.factory.get('/TwitterApi/TheSeekers/')

        output8 = get_terms_of_service(request)
        self.assertEqual(output8.status_code, 200)

if __name__ == '__main__':
    unittest.main()