from .serializers import HouseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import House


# Create your views here.
class CreateHouseView(APIView):

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            house = serializer.save()
            return Response({'success': True, 'msg': 'Creation Success', 'id_house': house.id_house},
                            status=status.HTTP_201_CREATED)
        return Response({'success': False, 'msg': 'House already exist!'}, status=status.HTTP_400_BAD_REQUEST)


class GetHouseView(APIView):
    def post(self, request):
        try:
            house = House.objects.get(id_house=request.data['id_house'])
            return Response({'success': True, 'msg': house.toJson()}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Forbidden"}, status=status.HTTP_403_FORBIDDEN)


class GetAllHouseView(APIView):
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
            return Response({'success': False, 'msg': "Wrong page id or connection error with database"}, status=status.HTTP_400_BAD_REQUEST)
