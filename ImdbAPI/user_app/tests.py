from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data={
            "username":"testcase",
            "email":"testcase@gmai.com",
            "password":"testcasehere",
            "password2":"testcasehere"
        }
        response=self.client.post(reverse('register'),data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user=User.objects.create_user(username="example",password="password123")
    
    def test_login(self):
        data={
            "username":"example",
            "password":'password123'
        }
        response=self.client.post(reverse('login'),data=data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    # def test_logout(self):
    #     # data={
    #     #     "username":"example",
    #     #     "password":'password123'
    #     # }
    #     # response=self.client.post(reverse('login'),data=data)
    #     # token=response.data['token']
    #     # print(token)
    #     # self.client.credentials(HTTP_AUTHORIZATION='BEARER '+token)
    #     # logout_response=self.client.post(reverse('logout'))
    #     # self.assertEqual(logout_response.status_code,status.HTTP_200_OK)
    #     self.token=Token.objects.get(user__username="example")
    #     self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
    #     response=self.client.post(reverse('logout'))
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)