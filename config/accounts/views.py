from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.accounts.models import User
from config.accounts.serializers import UserSerializer, UserRegistrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'User registered successfully'}, 
                status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# Create your views here.
def index(request):
    return HttpResponse("Hello World! You are the accounts index.")
