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


    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

    def add_session_to_request(self, request):
        """Annotate a request object with a session"""
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        return request

    def test_login(self):
        print("TC1: Get Login Page:")
        request = self.factory.get('/LMS/TheSeekers/')
        output1 = login(request)
        print("Working Successfully: Status Code -->",output1.status_code,"OK!")
        self.assertEqual(output1.status_code, 200)

    @patch('jwt.decode')
    def test_profile(self, mock_jwt):
        print("TC2: Get Profile Page:")
        Employee.objects.create(First_Name='Big', Last_Name='Bob', Email_Address='bigbob@gmail.com', Birth_Date='1953-09-02', Hire_Date='1986-06-26')
        request = self.factory.get('/LMS/TheSeekers/')
        request=self.add_session_to_request(request)
        request.session['id_token']="abcd"
        userinfo =  {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'},'email': 'bigbob@gmail.com'}
        mock_jwt.return_value = userinfo
        output2 = profile(request)
        print("Working Successfully: Status Code -->", output2.status_code, "OK!")
        self.assertEqual(output2.status_code, 200)

    @patch('jwt.decode')
    def test_Home(self, mock_jwt):
        print("TC3: Get Home Page:")
        Employee.objects.create(First_Name='Vidhi', Last_Name='Shah', Email_Address='vidhishah22@gmail.com',
                                Birth_Date='1953-09-02', Hire_Date='1986-06-26')
        request = self.factory.get('/LMS/TheSeekers/')
        request = self.add_session_to_request(request)
        request.session['id_token'] = "abcd"
        userinfo = {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'},
                    'email': 'vidhishah22@gmail.com'}
        mock_jwt.return_value = userinfo
        output3 = Home(request)
        print("Working Successfully: Status Code -->", output3.status_code, "OK!")
        self.assertEqual(output3.status_code, 200)


    @patch('jwt.decode')
    def test_ApplyForLeave(self, mock_jwt):
        print("TC4: Get ApplyForLeave Page:")
        employee = Employee.objects.create(First_Name='Iron', Last_Name='Man', Email_Address='ironaman@gmail.com',
                                Birth_Date='1953-09-02', Hire_Date='1986-06-26')
        empMgrDept = EmpMgrDept.objects.create(Emp_FullName="Iron Man",Emp_No_EmpMgrDept_id=employee.Emp_No,Manager_Emp_ID_id=employee.Emp_No)
        leave=LeaveBalance.objects.create(Emp_No_LeaveBal_id=employee.Emp_No,Leave_Type="Personal")
        request = self.factory.get('/LMS/TheSeekers/')
        request = self.add_session_to_request(request)
        request.session['id_token'] = "abcd"
        userinfo = {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'},
                    'email': 'ironaman@gmail.com'}
        mock_jwt.return_value = userinfo
        output4 = ApplyForLeave(request)
        print("Working Successfully: Status Code -->", output4.status_code, "OK!")
        self.assertEqual(output4.status_code, 200)

    @patch('jwt.decode')
    def test_ApproveLeave(self, mock_jwt):
        print("TC5: Get ApproveLeave Page:")
        employee2 = Employee.objects.create(First_Name='Angella', Last_Name='Jollie', Email_Address='angellajollie@gmail.com',
                                Birth_Date='1953-09-02', Hire_Date='1986-06-26')
        leave2=LeaveBalance.objects.create(Emp_No_LeaveBal_id=employee2.Emp_No,Leave_Type="Personal")
        request = self.factory.get('/LMS/TheSeekers/')
        request = self.add_session_to_request(request)
        request.session['id_token'] = "abcd"
        userinfo = {'http://Lms.seekers.com/app_metadata': {'role': 'Manager'},
                    'email': 'angellajollie@gmail.com'}
        mock_jwt.return_value = userinfo
        output5 = ApproveLeave(request)
        print("Working Successfully: Status Code -->", output5.status_code, "OK!")
        self.assertEqual(output5.status_code, 200)


if __name__ == '__main__':
    unittest.main()

