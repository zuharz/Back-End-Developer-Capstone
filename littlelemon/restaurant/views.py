from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from .models import Booking, Menu

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated] 