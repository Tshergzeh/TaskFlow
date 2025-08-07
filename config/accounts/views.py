from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from config.accounts.models import User
from config.accounts.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello World! You are the accounts index.")
