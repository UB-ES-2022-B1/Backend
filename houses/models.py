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

    def toJson(self):
        json = {"blocked": self.blocked,
                "title": self.title,
                "owner": self.owner,
                "description": self.description,
                "location": self.location,
                "id_house": self.id_house,
                "base_price": self.base_price,
                "extra_costs": self.extra_costs,
                "taxes": self.taxes,
                "num_hab": self.num_hab,
                "num_beds": self.num_beds,
                "num_bathrooms": self.num_bathrooms,
                "num_people": self.num_people,
                "company_individual": self.company_individual,
                "kitchen": self.kitchen,
                "swiming_pool": self.swiming_pool,
                "garden": self.garden,
                "billar_table": self.billar_table,
                "gym": self.gym,
                "TV": self.TV,
                "WIFII": self.WIFII,
                "dishwasher": self.dishwasher,
                "washing_machine": self.washing_machine,
                "air_conditioning": self.air_conditioning,
                "free_parking": self.free_parking,
                "spacious": self.spacious,
                "central": self.central,
                "quite": self.quite,
                "alarm": self.alarm,
                "smoke_detector": self.smoke_detector,
                "health_kit": self.health_kit}
        return json


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name="house_id", on_delete=models.CASCADE)
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
