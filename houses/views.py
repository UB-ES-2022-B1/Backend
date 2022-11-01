from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from .serializers import HouseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import House

# Create your views here.
class CreateHouseView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'msg': 'Creation Success'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'msg': 'House already exist!'}, status=status.HTTP_400_BAD_REQUEST)


class GetHouseView(APIView):
    def post(self, request):
        try:
            house = House.objects.get(id_house=request.data['id_house'])
            return Response({'success': True, 'msg': house.toJson()}, status=status.HTTP_200_OK)
        except:
            return Response({'success': False, 'msg': "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
