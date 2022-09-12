from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers 


# Create your views here.
class HelloApiView(APIView):
    """ APi view de prueba """
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Retornar lista de características del APIView """
        an_apiview = [
            'Usamos métodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la lógica de nuestra aplicación', 
            'Está mapeado manualmente a los URLs',
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Maneja actualización parcial de un objeto"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ borra un objeto"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API view set"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """ Retornar mensaje de Hola Mundo """
        a_viewset = [
            'Usa acciones (list, create, retrieve, update, partial update',
            'Automaticamente mapea a los URLs usando Routers',
            'Provee más funcionalidad con menos código'
        ]
        
        return Response({'message': 'Hola!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """ Crear nuevo mensaje de hola mundo """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """ Obtiene un objeto y su ID """
        
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """ Actualiza un objeto """
        
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """ Actualiza parcialmente un objeto """
        
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Destruye un objeto """
        
        return Response({'http_method': 'DELETE'})