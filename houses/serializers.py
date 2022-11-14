from rest_framework import serializers
from .models import House
from clients.models import Client


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = [
            'blocked','title','id_house','owner', 'description', 'location', 'base_price', 'extra_costs', 'taxes',
            'num_hab', 'num_bathrooms', 'num_beds', 'num_people', 'company_individual',
            'kitchen', 'swiming_pool', 'garden', 'billar_table', 'gym', 'TV', 'WIFII', 'dishwasher',
            'washing_machine', 'air_conditioning', 'free_parking', 'spacious', 'central', 'quite',
            'alarm', 'smoke_detector', 'health_kit'
        ]

    def save(self):
        house = House(
            title=self.validated_data['title'], owner=self.validated_data['owner'],
            description=self.validated_data['description'], location=self.validated_data['location'],
            base_price=self.validated_data['base_price'], extra_costs=self.validated_data['extra_costs'],
            taxes=self.validated_data['taxes'], num_hab=self.validated_data['num_hab'],
            num_bathrooms=self.validated_data['num_bathrooms'], num_beds=self.validated_data['num_beds'],
            num_people=self.validated_data['num_people'], company_individual=self.validated_data['company_individual'],
            kitchen=self.validated_data['kitchen'], swiming_pool=self.validated_data['swiming_pool'],
            garden=self.validated_data['garden'], billar_table=self.validated_data['billar_table'],
            gym=self.validated_data['gym'], TV=self.validated_data['TV'],
            WIFII=self.validated_data['WIFII'], dishwasher=self.validated_data['dishwasher'],
            washing_machine=self.validated_data['washing_machine'],
            air_conditioning=self.validated_data['air_conditioning'],
            free_parking=self.validated_data['free_parking'], spacious=self.validated_data['spacious'],
            central=self.validated_data['central'], quite=self.validated_data['quite'],
            alarm=self.validated_data['alarm'], smoke_detector=self.validated_data['smoke_detector'],
            health_kit=self.validated_data['health_kit']
        )
        house.save()
        house.id_house = house.id
        house.save()
        return house