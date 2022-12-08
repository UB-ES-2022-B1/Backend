from rest_framework import serializers

from trips.models import Trips


class TripsSerializer(serializers.ModelSerializer):
    class Meta():
        model = Trips

        fields = [
            'id_client',
            'timestamp',
            'id_house',
            'total_price',
            'check_in',
            'check_out',
            'guests',
        ]

    def save(self):
        trip = Trips(
            id_client=self.validated_data['id_client'],
            id_house=self.validated_data['id_house'],
            timestamp=self.validated_data['timestamp'],
            total_price=self.validated_data['total_price'],
            check_in=self.validated_data['check_in'],
            check_out=self.validated_data['check_out'],
            guests=self.validated_data['guests'],
        )

        trip.save()
