from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Tests our API Views"""

    def get(self, request, format=None):
        """ returns list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions(get, post, put, patch, delete)',
            'It is similar to traditional Django view',
            'Gives you the most control logic over'
        ]

        return Response({'message': 'Hello!!', 'an_apiview': an_apiview})
