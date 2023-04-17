from django.test import TestCase


class MenuViewTest(TestCase):
    def setup(self):
        self.client.post(
            "/restaurant/menu/", {"title": "Rice", "price": "3", "inventory": "10"}
        )
        self.client.post(
            "/restaurant/menu/", {"title": "Fries", "price": "2", "inventory": "8"}
        )

    def test_get_all(self):
        self.setup()
        items = self.client.get("/restaurant/menu/").json()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[1]["title"], "Fries")
