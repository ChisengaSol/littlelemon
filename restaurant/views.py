from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# class SingleBookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Booking.objects.all()
#     serializer_class = MenuSerializer
