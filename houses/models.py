from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from clients.models import Client
import uuid


class House(models.Model):
    blocked = models.CharField(max_length=50)  # True => cant be up for sale || False =>
    title = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    # image = models.ImageField(upload_to=pics)
    id_house = models.IntegerField(null=True)

    base_price = models.FloatField(max_length=7)
    extra_costs = models.FloatField(max_length=7)
    taxes = models.FloatField(max_length=7)

    num_hab = models.IntegerField()
    num_beds = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_people = models.IntegerField()
    company_individual = models.CharField(max_length=100)

    # The next cases can be True or False, but by default they are None to show that they havent been filled yet
    kitchen = models.BooleanField()
    swiming_pool = models.BooleanField()
    garden = models.BooleanField()
    billar_table = models.BooleanField()
    gym = models.BooleanField()
    TV = models.BooleanField()
    WIFII = models.BooleanField()
    dishwasher = models.BooleanField()
    washing_machine = models.BooleanField()
    air_conditioning = models.BooleanField()
    free_parking = models.BooleanField()
    spacious = models.BooleanField()
    central = models.BooleanField()
    quite = models.BooleanField()
    alarm = models.BooleanField()
    smoke_detector = models.BooleanField()
    health_kit = models.BooleanField()


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name="house_id", on_delete=models.CASCADE)
    image = models.ImageField("Uploaded image",upload_to=scramble_uploaded_filename)
