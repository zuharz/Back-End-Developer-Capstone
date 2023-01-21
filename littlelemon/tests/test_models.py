from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def setUp(self) -> None:
        self._menu_itemm_title = 'Ice Cream'
        Menu.objects.create(title=f'{self._menu_itemm_title}', price=12.99, inventory=100)
    
    def test_add_menu_item(self) -> None:
        self.menu_item = Menu.objects.get(title=f'{self._menu_itemm_title}')
        self.assertEqual(str(self.menu_item), f'{self._menu_itemm_title} : 12.99')