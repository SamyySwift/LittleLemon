from django.test import TestCase
from resturant.models import Menu


# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        item_str = item.get_item()
        self.assertEqual(item_str, "IceCream : 80")
        print("Model returned correct data")
