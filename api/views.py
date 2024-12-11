from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.serializers import PropertySerializer

from api.models import Property

# Create your views here.


class PropertyListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Property.objects.all()

        serializer_instance=PropertySerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    

    def post(self,request,*args,**kwargs):

        serializer_instance=PropertySerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)