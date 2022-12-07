from rest_framework import serializers

from favorites.models import Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Favorites

        fields = [
            'id_client',
            'timestamp',
            'id_house',
        ]

    def save(self):
        favorite = Favorites(
            id_client=self.validated_data['id_client'],
            id_house=self.validated_data['id_house'],
            timestamp=self.validated_data['timestamp']
        )

        favorite.save()
