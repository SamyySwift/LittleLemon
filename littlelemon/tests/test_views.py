from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from resturant.models import Menu  # Import your Menu model here
from resturant.serializers import MenuSerializer  # Import your Menu serializer here


class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few test instances of the Menu model
        self.menu1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)

        self.menu2 = Menu.objects.create(Title="Beef", Price=90, Inventory=100)
        self.menu3 = Menu.objects.create(Title="Fish", Price=40, Inventory=100)

    def test_getall(self):
        # Create a test client for making API requests
        client = APIClient()

        # Define the URL for the view you want to test
        url = reverse("menu-list")

        response = client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Serialize the Menu objects
        expected_data = MenuSerializer(
            [self.menu1, self.menu2, self.menu3], many=True
        ).data

        # Check if the serialized data in the response matches the expected data
        self.assertEqual(response.data, expected_data)
        print("View returned appropriate data")
