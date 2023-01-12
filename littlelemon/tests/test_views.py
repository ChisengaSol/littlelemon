from django.test import TestCase

# Create your tests here.
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream",price=80,inventory=100)