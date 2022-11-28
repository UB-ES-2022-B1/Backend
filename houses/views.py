from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny

from clients.models import Client
from .serializers import HouseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import House


# Create your views here.
class CreateHouseView(APIView):
    permission_classes = [AllowAny, ]

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
    def get(self, request):
        try:
            houses = House.objects.all()
            ids = []
            for house in houses:
                ids.append(house.id_house)

            return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Forbidden"}, status=status.HTTP_403_FORBIDDEN)


class SearchHousesView(APIView):
    def post(self, request):
        try:
            houses = House.objects.all()
            ids = []
            for i in houses:
                if request.data['town'].upper() == i.town.upper() and request.data['num_people'] <= i.num_people:
                    ids.append(i.id_house)
            if len(ids) == 0:
                return Response({'success': True, 'msg': "No matches with client preferences"},
                                status=status.HTTP_204_NO_CONTENT)
            return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Connexion error with Database"},
                            status=status.HTTP_400_BAD_REQUEST)
