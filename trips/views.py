from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from houses.models import House
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import datetime

from trips.serializers import TripsSerializer


# Create your views here.
class MakeTripView(APIView):
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
            fields["total_price"] = request.data["total_price"]
            fields["check_in"] = request.data["check_in"]
            fields["check_out"] = request.data["check_out"]
            fields["guests"] = request.data["guests"]

            serializer = TripsSerializer(data=fields)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'msg': 'Trip ordered'},
                                status=status.HTTP_201_CREATED)
            return Response({'success': False, 'msg': 'Error with database!'},
                            status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'success': False, 'msg': 'Incorrect house id!'},
                            status=status.HTTP_400_BAD_REQUEST)

