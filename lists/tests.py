from django.http import HttpRequest
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

    def test_home_page_returns_correct_html(self):
        """
        Root URL should resolve to valid html page.
        """

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
