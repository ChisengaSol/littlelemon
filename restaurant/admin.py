from django.contrib import admin
from .models import Menu,Booking
# Register your models here.
my_models = [Menu,Booking] # iterable list for multiple models

admin.site.register(my_models)