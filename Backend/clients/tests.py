from django.test import TestCase

# Create your tests here.
from django.urls import reverse,path,include
from rest_framework import status
from rest_framework.test import APITestCase,URLPatternsTestCase
from django.test import Client as cl
from clients.models import Client

class ClientTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new client object.
        """

        data = {'name': 'Lucas',
        'surname': 'Garcia',
        'password': 'ASD1235',
        'email': 'lgarcia@yahoo.com',
        'phone': '123091243',
        'country': 'Argentina',
        'birthdate': '1987-06-12'}

        response = self.client.post('http://localhost:8000/api/client/lgarcia@yahoo.com/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(),3)
        self.assertEqual(Client.objects.get(name='Lucas').name, 'Lucas')

    def test_get_account_by_email(self):
        """
        Ensure we can create a new client object.
        """
        client = cl()

        response = client.get('http://localhost:8000/api/clients/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_log_in(self):
        """
            Ensure we can log in and the tocken is created
            Ensure that the counter for wrong paswords works as intended
            Ensure that once the pasword has been written wrong 5 times, the account is blocket for good
        """
        #first register two users

        data_registro1 = {'name': 'mail',
                'surname': 'falso1',
                'password': 'ASD1235',
                'email': 'mailfalso1@yahoo.com',
                'phone': '123091243',
                'country': 'Argentina',
                'birthdate': '1987-06-12'}
        data_registro2 = {'name': 'mail',
                'surname': 'falso2',
                'password': 'ASD1235',
                'email': 'mailfalso2@yahoo.com',
                'phone': '123091243',
                'country': 'Narnia',
                'birthdate': '1987-06-12'}
        self.client.post('http://localhost:8000/api/client/mailfalso1@yahoo.com/', data_registro1, format='json')
        self.client.post('http://localhost:8000/api/client/mailfalso2@yahoo.com/', data_registro2, format='json')

        data_good = {"email": "mailfalso1@yahoo.com",
                     "password": "ASD1235"}
        data_bad = {'email': 'mailfalso2@yahoo.com',
                    'password': 'ASD1111'}

        # Ensure that the counter for wrong paswords works as intended
        response = self.client.post('http://localhost:8000/api/clients/login/', data_bad,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Client.objects.get(email=data_bad['email']).failedLoginAttemps, 1)


        # Lets block the account
        for n in [2,3,4,5]:
            response = self.client.post('http://localhost:8000/api/clients/login/', data_bad,
                                        format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertEqual(Client.objects.get(email=data_bad['email']).failedLoginAttemps, n)
        response = self.client.post('http://localhost:8000/api/clients/login/', data_bad,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_423_LOCKED)

        #Lets log in correctly
        response = self.client.post('http://localhost:8000/api/clients/login/', data_good,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
