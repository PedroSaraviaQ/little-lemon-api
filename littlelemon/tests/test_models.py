from django.test import TestCase
from restaurant.models import Menu


class MenuItemTest(TestCase):
    def test_item(self):
        item = Menu.objects.create(title="Frappuccino", price=5, inventory=7)
        self.assertEqual(str(item), "Frappuccino: 5")
