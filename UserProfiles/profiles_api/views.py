from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """Tests our API Views"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ returns list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, put, patch, delete)',
            'It is similar to traditional Django view',
            'Gives you the most control logic over'
        ]

        return Response({'message': 'Hello!!', 'an_apiview': an_apiview})


    def post(self, request):
        """Tests our sample Post API"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({'message': message})

        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Used to update the objects"""

        return Response({'method': 'put'})


    def patch(self, request, pk=None):
        """This updates only requested fields"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ This deletes the object"""

        return Response({'method': 'delete'})
