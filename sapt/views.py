from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from sapt.models import sapt
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from sapt.serializ import *
from django.http import HttpResponse

from django.db.models import Q, Sum, Max, query, Subquery, QuerySet, Count


# Create your views here.
class getserial1(APIView):
    def get(self, request):
        query = sapt.objects.all()
        ser = serialmodl(query, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)



class getview(APIView):
    def get(self,request):
     qiery=sapt.objects.all().filter(meli=request.GET['a'])
     ser=serialget(qiery,many=True)
     return Response(ser.data,status=status.HTTP_200_OK)

class updateview(APIView):
    def get(self,request):
        query = sapt.objects.all()
        ser = serialmodl(query, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
class postview(APIView):
    def post(self,request):
        seriali=serialmodl(data=request.data)
        if seriali.is_valid():
            seriali.save()
            return Response(seriali.data,status=status.HTTP_201_CREATED)
        return Response(seriali.errors,status=status.HTTP_400_BAD_REQUEST)

class postser(APIView):
    def post(self,request):
        seriali=serialget(data=request.data)
        if seriali.is_valid():
            meli=seriali.data.get('meli')
            nameandfamily=seriali.data.get('nameandfamily')
            tarmor=seriali.data.get('tarmoraje')
            taraz=seriali.data.get('taraz')
            tarta=seriali.data.get('tarta')
            kolest=seriali.data.get('kolestarhat')
            estarhattaednashodeh=seriali.data.get('estarhattaednashodeh')
            shsapt=seriali.data.get('shsapt')
        else:
          return Response(seriali.errors,status=status.HTTP_404_NOT_FOUND)
        sapt1=sapt()
        sapt1.meli=meli
        sapt1.tarmoraje=tarmor
        sapt1.taraz=taraz
        sapt1.tarta=tarta
        sapt1.kolestarhat=kolest
        sapt1.estarhattaednashodeh=estarhattaednashodeh
        sapt1.nameandfamily=nameandfamily
        sapt1.shsapt=shsapt
        sapt1.save()
        return Response(seriali.data,status=status.HTTP_200_OK)

class serchdata(APIView):
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def get(self,request):
        query=sapt.objects.filter(meli__contains=request.GET['name'])
        serial=serialmodl(query,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
class deletedata(APIView):
    def delete(self,request,pk):
        query=sapt.objects.get(meli=pk)
        query.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([permissions.IsAdminUser])
def vv(request):

    if request.method=='GET':
        query=sapt.objects.all()
        ser=serialmodl(query,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)