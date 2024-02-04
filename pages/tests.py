from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse, resolve
from .views import HomePageView

class HomePagesTests(SimpleTestCase):
    def setUp(self):
        url = reverse('pages:home')
        self.response = self.client.get(url)
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self): # new
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_url_resolves_home_view(self): # new
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)   


