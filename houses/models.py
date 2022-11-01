from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class House(models.Model):
    blocked = models.CharField(max_length=50) #True => cant be up for sale || False =>
    title = models.CharField(max_length=50)
    owner_id = models.EmailField(max_length=255,unique=True,)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    #image = models.ImageField(upload_to=pics)

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

    def create_light(self,title,owner_id, description, location, base_price, extra_costs, taxes,
                     num_hab, num_bathrooms, num_beds, num_people, company_individual):
        self.title = title
        self.owner_id = owner_id
        self.description = description
        self.location = location
        self.base_price = base_price
        self.extra_costs = extra_costs
        self.taxes = taxes
        self.num_hab = num_hab
        self.num_bathroom = num_bathrooms

        self.num_beds = num_beds
        self.num_people = num_people
        self.company_individual = company_individual
    def create_vivenda_complete(
            self,title,owner_id, description, location, base_price, extra_costs, taxes,
             num_hab, num_bathrooms, num_beds, num_people, company_individual,
            kitchen, swiming_pool,garden, billar_table, gym, TV, WIFII, dishwasher,
            washing_machine, air_conditioning, free_parking, spacious, central, quite,
            alarm, smoke_detector, health_kit
    ):

        self.create_complete(title, title,owner_id, description, location, base_price, extra_costs,
                                taxes,num_hab, num_bathrooms, num_beds, num_people, company_individual)

        self.kitchen = kitchen
        self.swiming_pool = swiming_pool
        self.garden = garden
        self.billar_table = billar_table
        self.gym = gym
        self.TV = TV
        self.WIFII = WIFII
        self.dishwasher = dishwasher
        self.washing_machine = washing_machine
        self.air_conditioning =air_conditioning
        self.free_parking = free_parking
        self.spacious = spacious
        self.central = central
        self.quiet = quite
        self.alarm = alarm
        self.smoke_detector = smoke_detector
        self.health_kit = health_kit
        """house.save(using=self._db)
        return user"""