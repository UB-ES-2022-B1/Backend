from django.db import models

from clients.models import Client
from houses.models import House


class Favorites(models.Model):
    id_house = models.ForeignKey(House, on_delete=models.CASCADE)
    timestamp = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
