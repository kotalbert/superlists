from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class TestHomePage(TestCase):

    def test_resolve_home_page(self):
        """
        Root URL should resolve to home page view.
        """

        found = resolve('/')
        self.assertEqual(found.func, home_page)
