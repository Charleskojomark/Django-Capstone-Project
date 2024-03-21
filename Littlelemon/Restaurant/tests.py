from django.test import TestCase
from django.urls import reverse
from .models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item),"IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.menu1 = Menu.objects.create(title="Item 1", price=10, inventory=50)
        self.menu2 = Menu.objects.create(title="Item 2", price=15, inventory=25)

    def test_getall(self):
        url = reverse('menu')  # Assuming you have defined the URL name for the Menu list view
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)