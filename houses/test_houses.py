from django.test import TestCase

# Create your tests here.
from django.test import TestCase

# Create your tests here.

from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
# from django.test import Client as cl
from .models import House


class VivendaTest(APITestCase):

    def test_create_vivenda(self):
        """
        Ensure we can create a new vivenda object.
        """
        # we will create an account and a hous attached to it

        data_client = {"name": "Lucas",
                       "surname": "Garcia",
                       "password": "ASD1235",
                       "email": "mailfalso1@yahoo.com",
                       "phone": "123091243",
                       "country": "Argentina",
                       "birthdate": "1987-06-12"}

        data_login = {"email": "mailfalso1@yahoo.com",
                      "password": "ASD1235"}

        data_house = {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "location": "Tarragona",
            "base_price": "100",
            "extra_costs": "10",
            "taxes": "4",
            "num_hab": "4",
            "num_beds": "8",
            "num_bathrooms": "4",
            "num_people": "10",
            "company_individual": "particular",
            "kitchen": "True",
            "swiming_pool": "True",
            "garden": "True",
            "billar_table": "True",
            "gym": "True",
            "TV": "True",
            "WIFII": "True",
            "dishwasher": "True",
            "washing_machine": "True",
            "air_conditioning": "False",
            "free_parking": "False",
            "spacious": "False",
            "central": "False",
            "quite": "False",
            "alarm": "False",
            "smoke_detector": "False",
            "health_kit": "False"

        }
        self.client.post('http://localhost:8000/accounts/register', data_client, format='json')
        self.client.post('http://localhost:8000/accounts/login', data_login, format='json')

        response = self.client.post('http://localhost:8000/houses/register', data_house, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(House.objects.count(), 1)
        self.assertEqual(House.objects.get(owner='mailfalso1@yahoo.com').title, 'casa1')
