from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics,viewsets

from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer

# Create your views here.
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu":menu_data}
    return render(request,'menu.html',main_data)

def index(request):
    return render(request, 'index.html', {})

def home(request):
    return render(request, 'index.html', {})

# class BookingView(APIView):
#     def get(self,request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items,many=True)
#         return Response(serializer.data) #return JSON

#     def post(self,request):
#         serializer = bookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data})

# class MenuItemView(APIView):
#     def get(self,request):
#         items = Menu.objects.all()
#         serializer = menuSerializer(items,many=True)
#         return Response(serializer.data) #return JSON

#     def post(self,request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success","data":serializer.data})
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
