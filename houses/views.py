from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from .serializers import HouseSerializer, ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import House
import uuid
from azure.storage.blob import BlockBlobService

# Create your views here.
class CreateHouseView(APIView):

    def post(self, request):
        links= request.data['images']
        data= request.data.copy()
        data.pop('images')
        serializer = HouseSerializer(data=data)
        if serializer.is_valid():
            house = serializer.save()
            for i in links:
                serializer= ImageSerializer(data= {'id_house':house.id_house,'link':i})
                serializer.save()
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
    def get(self,request):
        try:
            houses = House.objects.all()
            ids = []
            for house in houses:
                ids.append(house.id_house)

            return Response({'success': True, 'ids': ids}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
