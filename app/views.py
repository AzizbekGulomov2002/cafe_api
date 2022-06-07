import genericpath

from urllib import response
from django.shortcuts import render


from rest_framework import generics

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu,Mahsulot
from .serializers import MahsulotSerializers, MenuSerializers


# class AllMenu(APIView):
#     def get(self,request):
#         all = Menu.objects.all()
#         serializer = MenuSerializers(all,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
    
# class AllMahsulot(APIView):
#     def get(self,request):
#         all = Mahsulot.objects.all()
#         serializer = MahsulotSerializers(all,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

class MenuModel(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    
class MenuModel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    
    
class MahsulotModel(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers
    
class MahsulotModel(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializers