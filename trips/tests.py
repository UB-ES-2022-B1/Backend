from django.test import TestCase

from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase


class TripsTest(APITestCase):
    data_registro = {"name": "Lucas",
                     "surname": "falso1",
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

    def test_reserve_trip(self):
        self.client.post('http://localhost:8000/accounts/register', self.data_registro, format='json')

        data_good = {"password": "ASD1235", "email": "mailfalso1@yahoo.com"}
        response = self.client.post('http://127.0.0.1:8000/accounts/login', data_good, format='json')
        token = response.json()['access']

        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_trip = {"id_house": 1,
                     "total_price": 190.23,
                     "check_in": "2022-12-25",
                     "check_out": "2022-12-29",
                     "guests": 3
                     }
        response = self.client.post('http://127.0.0.1:8000/trips/reserve', data=data_trip,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
