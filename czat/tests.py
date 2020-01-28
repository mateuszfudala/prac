from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from .views import DodajWiadomosc, EdytujWiadomosc

class testujetes(SimpleTestCase):
    def test_jeden_z_wielu(self):
        url = reverse('dodaj')
        print(resolve(url))

