from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from .models import HouseImage
from .serializers import HouseSerializer, HouseImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.
class CreateHouseView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            house = serializer.save()
            return Response({'success': True, 'msg': 'Creation Success', 'id_house': house.id_house},
                            status=status.HTTP_201_CREATED)
        return Response({'success': False, 'msg': 'House already exist!'}, status=status.HTTP_400_BAD_REQUEST)


class UploadedImagesViewSet(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self,request):
        serializer = HouseImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'msg': 'Creation Success',},
                            status=status.HTTP_201_CREATED)
