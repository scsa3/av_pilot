from django.test import TestCase
from django.urls import reverse


class FilterListTests(TestCase):
    def test_index(self):
        path = reverse('filter:filter-list') + "?category=123"
        response = self.client.get(path)
        print(response)
