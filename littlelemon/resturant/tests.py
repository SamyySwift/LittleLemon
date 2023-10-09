from django.test import TestCase
from .models import Menu

# Create your tests here.


class MenuItemTest(TestCase):
    item = Menu.objects.get(pk=1)
    item_str = item.get_item()

    assert item_str == {"Beef Salad": "12.00"}
