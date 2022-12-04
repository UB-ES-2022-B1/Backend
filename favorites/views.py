from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from clients.models import Client
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

            # Campos a almacenar en la base de datos.
            fields = dict()
            fields["id_client"] = client.pk
            fields["id_house"] = house.pk
            fields["timestamp"] = datetime.date.today()

            serializer = FavoritesSerializer(data=fields)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'msg': 'Added Success'},
                                status=status.HTTP_201_CREATED)
            return Response({'success': False, 'msg': 'Error with database!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'success': False, 'msg': 'Incorrect house id!'},
                            status=status.HTTP_400_BAD_REQUEST)
