from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        """
        Set up a few test instances of the Menu model.
        """
        self.client = APIClient()
        # Create test menu items
        self.menu1 = Menu.objects.create(Title="Ice Cream", Price=80, Inventory=100)
        self.menu2 = Menu.objects.create(Title="Pizza", Price=150, Inventory=50)
        self.menu3 = Menu.objects.create(Title="Burger", Price=120, Inventory=70)
        self.url = "/restaurant/menu/"

    def test_getall(self):
        """
        Test the retrieval of all menu items.
        """
        response = self.client.get(self.url)

        # Serialize the data manually
        expected_data = MenuSerializer([self.menu1, self.menu2, self.menu3], many=True).data
        
        # Assert the response status and content
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
