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

    def test_uses_home_template(self):
        """
        Root URL should be using home.html template
        """

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        """
        Root URL should resolve to valid html page.
        """

        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_can_save_post_request(self):
        """
        Form should post data back to root URL
        """

        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
