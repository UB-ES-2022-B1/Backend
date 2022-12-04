
# Create your views here.
from rest_framework.permissions import IsAuthenticated

from .serializers import HouseSerializer, ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import datetime
from io import BytesIO
import os
from .models import House

from azure.storage.blob import BlobServiceClient
from rest_framework.permissions import AllowAny


# Create your views here.
class CreateHouseView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            house = serializer.save()

            return Response({'success': True, 'msg': 'Creation Success', 'id_house': house.id_house},
                            status=status.HTTP_201_CREATED)
        return Response({'success': False, 'msg': 'House already exist!'}, status=status.HTTP_400_BAD_REQUEST)


class UploadImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            House.objects.get(id_house=request.POST['id_house'])
            if len(request.FILES.getlist("files")) > 0:
                for file in request.FILES.getlist("files"):
                    uuid = datetime.datetime.now()
                    file_upload_name = str(uuid) + file.name
                    blob_service_client = BlobServiceClient.from_connection_string(conn_str=os.environ['STORAGE'])

                    container_client = blob_service_client.get_container_client(os.environ['CONTAINER'])
                    file_io = BytesIO(file.read())
                    container_client.upload_blob(name=file_upload_name, data=file_io)

                    serializer = ImageSerializer(data={'id_house': request.POST['id_house'], 'link': file_upload_name})
                    if serializer.is_valid():
                        serializer.save()

                return Response({'success': True, 'msg': 'Upload complete!'},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'msg': 'missing files'},
                                status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'success': False, 'msg': 'wrong house id'},
                            status=status.HTTP_404_NOT_FOUND)


class GetHouseView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            house = House.objects.get(id_house=request.data['id_house'])

            return Response({'success': True, 'msg': house.toJson()}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Wrong house id"}, status=status.HTTP_404_NOT_FOUND)


class GetAllHouseView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            # Obtengo todas las casas de la base de datos
            houses = House.objects.all()

            # Extraigo los bloques de 20 en 20 en función del page_id
            if len(houses) > request.data['page_id'] * 20:
                index = request.data['page_id'] * 20
                house_set = houses[index:index + 20]

            else:
                house_set = houses[0:20]
            # Si obtengo bloques más pequeños, los completo añadiendo más elementos repetidos
            if len(house_set) < 20:
                length = 20 - len(house_set)
                house_set = house_set + houses[0:length]

            ids = []
            for house in house_set:
                ids.append(house.id_house)

            return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Wrong page id or connection error with database"},
                            status=status.HTTP_400_BAD_REQUEST)


class SearchHousesView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        try:
            houses = House.objects.all()
            ids = []
            for i in houses:
                if request.data['town'].upper() == i.town.upper() and request.data['num_people'] <= i.num_people:
                    ids.append(i.id_house)
            if ids:
                return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)

            return Response({'success': True, 'msg': "No matches with client preferences"},
                            status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'success': False, 'msg': "Connexion error with Database"},
                            status=status.HTTP_400_BAD_REQUEST)


# Función para devolver las viviendas registradas de un propietario.
class GetOwnHouses(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Filtro las casas cuyo propietario sea igual que el usuario que ha realizado la consulta
        houses = House.objects.filter(owner=request.user.email)

        # Retorno los ids de las casas
        ids = []
        for i in houses:
            ids.append(i.id_house)
        if ids:
            return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)

        return Response({'success': True, 'msg': "No matches with client preferences"},
                        status=status.HTTP_204_NO_CONTENT)
