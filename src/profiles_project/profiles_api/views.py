from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from . import permissions
from . import serializers
from . import models
# Create your views here.

from pprint import pprint

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of Api features"""

        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Hello Niz, how are you?'
        ]

        return Response({
            'message' : 'Hello!',
            'an_apiview' : an_apiview
        })

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):

        return Response({'method':'patch'})

    def delete(self, request, pk=None):

        return Response({'method':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test APi viewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset =[
            'uses action (list, create, update , retrieve)'
        ]

        return Response({'message':'hello!', 'a_viewset':a_viewset})

    def create(self, request):

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'messsage':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handles getting an object by it's ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handles deleting an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles create, creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password nd returns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """User the obtainAuthToken APIView to validate and creata a token"""

        return ObtainAuthToken().post(request)