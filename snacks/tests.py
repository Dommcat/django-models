from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


# Create your tests here.
class SnackTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snacks = Snack.objects.create(
            name='Veggie Chips', purchaser=self.user)

    def test_string_representation(self):
        self.assertEqual(str(self.snacks), 'Veggie Chips')

    def test_snack_name(self):
        self.assertEqual(f'{self.snacks.name}', 'Veggie Chips')

    def test_list_page_status_code(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snacks_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snacks_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_no_page_status_code(self):
        url = '/snacks_detail'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

