from django.db import models

from clients.models import Client
from houses.models import House


class Trips(models.Model):
    id_house = models.ForeignKey(House, on_delete=models.CASCADE)
    timestamp = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_price = models.FloatField(max_length=7)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField()