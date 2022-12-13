from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from clients.models import Client
from favorites.models import Favorites
from favorites.serializers import FavoritesSerializer
from houses.models import House
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import datetime


# Create your views here.
class AddToFavorites(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Obtención de los objetos necesarios para crear un favorito.
            house = House.objects.get(id=request.data["id_house"])
            client = Client.objects.get(email=request.user.email)

            if request.data["toAdd"] == True:
                # Campos a almacenar en la base de datos.
                fields = dict()
                fields["id_client"] = client.pk
                fields["id_house"] = house.pk
                fields["timestamp"] = datetime.date.today()
                serializer = FavoritesSerializer(data=fields)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': True, 'msg': 'Added to favorites'},
                                    status=status.HTTP_201_CREATED)
                return Response({'success': False, 'msg': 'Error with database!'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                Favorites.objects.filter(id_client=client.pk, id_house=house.pk).delete()
                return Response({'success': True, 'msg': 'Removed from favorites'},
                                status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'success': False, 'msg': 'Incorrect house id!'},
                            status=status.HTTP_400_BAD_REQUEST)


class GetOwnFavorites(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:

            client = Client.objects.get(email=request.user.email)
            favorites = Favorites.objects.filter(id_client=client.pk)
            serializer = FavoritesSerializer(favorites, many=True)
            return Response({'success': True, 'favorites': serializer.data},
                            status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response({'success': False, 'msg': 'Incorrect house id!'},
                            status=status.HTTP_400_BAD_REQUEST)