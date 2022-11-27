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

        data_house = {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "province": "Tarragona",
            "country": "España",
            "town": "Salou",
            "street": "Carrer de la Mar 22",
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
        data_login = {"password": "ASD1235",
                      "email": "mailfalso1@yahoo.com"}
        self.client.post('http://localhost:8000/accounts/register', data_client, format='json')
        self.client.post('http://localhost:8000/accounts/login', data_login, format='json')
        response = self.client.post('http://localhost:8000/houses/register', data_house, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(House.objects.count(), 1)
        self.assertEqual(House.objects.get(owner_id='mailfalso1@yahoo.com').title, 'casa1')

    def test_searchVivienda(self):
        data_house = {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "province": "Tarragona",
            "country": "España",
            "town": "Salou",
            "street": "Carrer de la Mar 22",
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
        data_house2= {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "province": "Tarragona",
            "country": "España",
            "town": "Barcelona",
            "street": "Carrer de la Mar 22",
            "base_price": "100",
            "extra_costs": "10",
            "taxes": "4",
            "num_hab": "4",
            "num_beds": "8",
            "num_bathrooms": "4",
            "num_people": "3",
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
        data_house3= {
            "title": "casa1",
            "owner": "mailfalso1@yahoo.com",
            "description": "bonica",
            "province": "Tarragona",
            "country": "España",
            "town": "Salou",
            "street": "Carrer de la Mar 20",
            "base_price": "100",
            "extra_costs": "10",
            "taxes": "4",
            "num_hab": "4",
            "num_beds": "8",
            "num_bathrooms": "4",
            "num_people": "5",
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

        response = self.client.post('http://localhost:8000/houses/search-houses', {"town": "salou","num_people": 3}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post('http://localhost:8000/houses/register', data_house, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('http://localhost:8000/houses/register', data_house2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('http://localhost:8000/houses/register', data_house3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://localhost:8000/houses/search-houses', {"town": "salou", "num_people": 3},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ids'][0],1)

        response = self.client.post('http://localhost:8000/houses/search-houses', {"town": "salou", "num_people": 15},format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(response.data['ids']),0)

        response = self.client.post('http://localhost:8000/houses/search-houses', {"town": "salou", "num_people": 5},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['ids']), 2)