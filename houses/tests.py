# Create your tests here.

from rest_framework import status
from rest_framework.test import APITestCase
from .models import House
from datetime import datetime, timedelta


class VivendaTest(APITestCase):
    data_client = {"name": "Lucas",
                   "surname": "Garcia",
                   "password": "ASD1235",
                   "email": "mailfalso1@yahoo.com",
                   "phone": "123091243",
                   "country": "Argentina",
                   "birthdate": "1987-06-12"}

    data_login = {"password": "ASD1235",
                  "email": "mailfalso1@yahoo.com"}

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
    data_house2 = {
        "title": "casa1",
        "owner": "mailfalso1@yahoo.com",
        "description": "bonica",
        "province": "Barcelona",
        "country": "España",
        "town": "Barcelona",
        "street": "Carrer Aribau 22",
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
    data_house3 = {
        "title": "casa1",
        "owner": "mailfalso1@yahoo.com",
        "description": "bonica",
        "province": "Girona",
        "country": "España",
        "town": "Salou",
        "street": "Carrer del Pi 20",
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

    def test_create_vivenda(self):
        """
        Ensure we can create a new vivenda object.
        """
        # we will create an account and a house attached to it


        self.client.post('http://localhost:8000/accounts/register', self.data_client, format='json')

        response = self.client.post('http://127.0.0.1:8000/accounts/login', self.data_login, format='json')
        token = response.json()['access']
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(House.objects.count(), 1)
        self.assertEqual(House.objects.get(owner='mailfalso1@yahoo.com').title, 'casa1')

    def test_searchVivienda(self):

        self.client.post('http://localhost:8000/accounts/register', self.data_client, format='json')

        response = self.client.post('http://127.0.0.1:8000/accounts/login', self.data_login, format='json')
        token = response.json()['access']
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house2,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house3,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')

        data_trip = {"id_house": 1,
                     "total_price": 190.23,
                     "check_in": "2022-12-25",
                     "check_out": "2022-12-29",
                     "guests": 3
                     }
        response = self.client.post('http://127.0.0.1:8000/trips/reserve', data=data_trip,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data_trip = {"id_house": 2,
                     "total_price": 198,
                     "check_in": "2022-12-10",
                     "check_out": "2022-12-13",
                     "guests": 3
                     }
        response = self.client.post('http://127.0.0.1:8000/trips/reserve', data=data_trip,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        search_data = {"town": "sAloU",
                        "num_people": 5,
                        "check_in":  "2022-12-25",
                        "check_out": "2022-12-29"
                        }

        search_data2 = {"town": "SALOU",
                        "num_people": 15,
                        "check_in":  "2022-12-13",
                        "check_out":"2022-12-15"
                        }
        search_data3 = {"town": "sAloU",
                        "num_people": 5,
                        "check_in":  "2022-12-13",
                        "check_out":"2022-12-15"
                        }

        response = self.client.post('http://localhost:8000/houses/search-houses', search_data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ids'][0], 3)

        response = self.client.post('http://localhost:8000/houses/search-houses', search_data2,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.post('http://localhost:8000/houses/search-houses', search_data3,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['ids']), 2)

    def test_get_own_houses(self):
        self.client.post('http://localhost:8000/accounts/register', self.data_client, format='json')
        response = self.client.post('http://127.0.0.1:8000/accounts/login', self.data_login, format='json')
        token = response.json()['access']
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house2,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('http://127.0.0.1:8000/houses/get-own-houses',
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(len(response.data['ids']), 1)

    def test_delete_house(self):
        self.client.post('http://localhost:8000/accounts/register', self.data_client, format='json')
        response = self.client.post('http://127.0.0.1:8000/accounts/login', self.data_login, format='json')
        token = response.json()['access']
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.data_house2['owner'] = 'other@gmail.com'
        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house2,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://127.0.0.1:8000/houses/register', data=self.data_house3,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://localhost:8000/houses/delete-house', data={"id_house": 1},
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post('http://localhost:8000/houses/delete-house', data={"id_house": 2},
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        data_trip = {"id_house": 3,
                     "total_price": 198,
                     "check_in": datetime.date(datetime.now()),
                     "check_out": datetime.date(datetime.now()) + timedelta(days=3),
                     "guests": 3
                     }
        response = self.client.post('http://127.0.0.1:8000/trips/reserve', data=data_trip,
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('http://localhost:8000/houses/delete-house', data={"id_house": 3},
                                    **{'HTTP_AUTHORIZATION': f'Bearer {token}'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)