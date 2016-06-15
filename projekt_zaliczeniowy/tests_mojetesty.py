from django.test import TestCase
from projekt_zaliczeniowy.models import *
from django import forms
from .views import policz_procent, incorrect_votes
from .admin import GminaForm
# Create your tests here.


class WojewodztwoTestCase(TestCase):
    def setUp(self):
        Wojewodztwo.objects.create(nazwa='pomorskie')

    def test_nazwa_wojewodztwa(self):
        pomorskie = Wojewodztwo.objects.get(id=1)
        self.assertEqual(pomorskie.nazwa, "pomorskie")


class GminaAdminFormTestCase(TestCase):

    def test_gmina_wrong_numbers(self):
        data = {
            'liczba_mieszkancow': 10000,
            'liczba_uprawnionych': 9000,
            'liczba_wydanych_kart': 8000,
            'liczba_glosow_oddanych_na_kandydata_nr_1': 7000,
            'liczba_glosow_oddanych_na_kandydata_nr_2': 1500,
        }
        form = GminaForm(data)
        self.assertFalse(form.is_valid())


class ViewsHelpersTestCase(TestCase):

    def test_policz_procent_accepts(self):
        self.assertEqual(policz_procent(40, 100), (40, 60))

    def test_policz_procent_zero(self):
        self.assertEqual(policz_procent(40, 0), (50, 50))

    def test_incorrect_votes_correct(self):
        self.assertFalse(incorrect_votes(20, 40, 60))

    def test_incorrect_votes_incorrect(self):
        self.assertTrue(incorrect_votes(20, 50, 60))

    def test_incorrect_votes_minus(self):
        self.assertTrue(incorrect_votes(-4, 40, 40))