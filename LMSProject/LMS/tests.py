from django.test import TestCase

# Create your tests here.

import unittest
from django.test.client import RequestFactory
from .views import *
from django.contrib.sessions.middleware import SessionMiddleware
from LMS.models import *
from django.test import Client
import jwt
from unittest.mock import patch, Mock
class SimpleTest(unittest.TestCase):

    #export DJANGO_SETTINGS_MODULE=TwitterApi.settings
    emp=None

    # @classmethod
    # def setUpTestData(cls):
    #     Employee.objects.create(First_Name='Big', Last_Name='Bob', Email_Address='bigbob@gmail.com', Emp_No=9999,
    #                             Birth_Date='1953-09-02', Hire_Date='1986-06-26')

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()
        # Employee.objects.create(First_Name='Big', Last_Name='Bob', Email_Address='bigbob@gmail.com', Emp_No=9999, Birth_Date='1953-09-02', Hire_Date='1986-06-26')

    def add_session_to_request(self, request):
        """Annotate a request object with a session"""
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        return request

    # @patch('jwt.decode')
    # def test_profile(self, mock_jwt):
    #     print("TC2: Get Profile Page:")
    #     request = self.factory.get('/LMS/TheSeekers/')
    #     request=self.add_session_to_request(request)
    #     # print ('2222222---->', request.session)
    #     # print(self.emp)
    #     request.session['id_token']="abcd"
    #     userinfo =  {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'}, 'http://Lms.seekers.com/user_metadata': {}, 'given_name': 'Big', 'name': 'Big Bob', 'picture': 'https://lh4.googleusercontent.com/-rW-L8-Mdn6Y/AAAAAAAAAAI/AAAAAAAAGj0/dxNCMduKcmM/photo.jpg', 'gender': 'female', 'locale': 'en-GB', 'updated_at': '2018-12-07T18:18:05.806Z', 'email': 'bigbob@gmail.com', 'email_verified': True, 'iss': 'https://seekerslms.auth0.com/', 'sub': 'google-oauth2|104087801749009073568', 'aud': 'LCTMUEpEUe9eV_0NWzAkUvkqF6cC19aT', 'iat': 1544206686, 'exp': 1544242686}
    #     mock_jwt.return_value = userinfo
    #     output2 = profile(request)
    #     # print("*****output 1234:",output2.content)
    #     self.assertEqual(output2.status_code, 200)

    # @patch('jwt.decode')
    # def test_Home(self, mock_jwt):
    #     print("TC3: Get Home Page:")
    #     request = self.factory.get('/LMS/TheSeekers/')
    #     request = self.add_session_to_request(request)
    #     # print ('2222222---->', request.session)
    #     # print(self.emp)
    #     request.session['id_token'] = "abcd"
    #     userinfo = {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'},
    #                 'http://Lms.seekers.com/user_metadata': {}, 'given_name': 'Big', 'name': 'Big Bob',
    #                 'picture': 'https://lh4.googleusercontent.com/-rW-L8-Mdn6Y/AAAAAAAAAAI/AAAAAAAAGj0/dxNCMduKcmM/photo.jpg',
    #                 'gender': 'female', 'locale': 'en-GB', 'updated_at': '2018-12-07T18:18:05.806Z',
    #                 'email': 'bigbob@gmail.com', 'email_verified': True, 'iss': 'https://seekerslms.auth0.com/',
    #                 'sub': 'google-oauth2|104087801749009073568', 'aud': 'LCTMUEpEUe9eV_0NWzAkUvkqF6cC19aT',
    #                 'iat': 1544206686, 'exp': 1544242686}
    #     mock_jwt.return_value = userinfo
    #     output3 = Home(request)
    #     # print("*****output 1234:",output2.content)
    #     self.assertEqual(output3.status_code, 200)

if __name__ == '__main__':
    unittest.main()

