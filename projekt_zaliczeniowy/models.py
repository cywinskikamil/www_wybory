from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_not_spaces(value):
    if value.strip() == '':
        raise ValidationError(u"You must provide more than just whitespace.")


class WojewodztwoRozmiar(models.Model):
    dolny_limit = models.IntegerField(default=0, blank=False)
    gorny_limit = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.dolny_limit) + " " + str(self.gorny_limit)

    def lista_gmin(self):
        return Gmina.objects.filter(liczba_mieszkancow__gte=self.dolny_limit,
                                    liczba_mieszkancow__lte=self.gorny_limit).values()


class WojewodztwoRodzaj(models.Model):
    WIES = 'WIES'
    MIASTO = 'MIASTO'
    STATKI = 'STATKI'
    ZAGRANICA = 'ZAGRANICA'
    rodzaje = (
        (WIES, 'wieś'),
        (MIASTO, 'miasto'),
        (STATKI, 'statki'),
        (ZAGRANICA, 'zagranica')
    )
    rodzaj = models.CharField(max_length=30, choices=rodzaje, default='MIASTO', blank=False)

    def __str__(self):
        return self.rodzaj

    def lista_gmin(self):
        return Gmina.objects.filter(rodzaj=self.rodzaj).values()


class Wojewodztwo(models.Model):
    nazwa = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa

    def lista_gmin(self):
        return Gmina.objects.filter(wojewodztwo=self.id).values()


class Gmina(models.Model):
    WIES = 'WIES'
    MIASTO = 'MIASTO'
    STATKI = 'STATKI'
    ZAGRANICA = 'ZAGRANICA'
    rodzaje = (
        (WIES, 'wieś'),
        (MIASTO, 'miasto'),
        (STATKI, 'statki'),
        (ZAGRANICA, 'zagranica')
    )
    wojewodztwo = models.ForeignKey(Wojewodztwo, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=30, default="-", blank=False, null=False)
    rodzaj = models.CharField(max_length=30, choices=rodzaje, default='MIASTO', blank=False)
    liczba_mieszkancow = models.IntegerField(default=0, blank=False, null=False)
    liczba_uprawnionych = models.IntegerField(default=0, blank=False)
    liczba_wydanych_kart = models.IntegerField(default=0, blank=False)
    liczba_glosow_oddanych_na_kandydata_nr_1 = models.IntegerField(default=0, blank=False)
    liczba_glosow_oddanych_na_kandydata_nr_2 = models.IntegerField(default=0, blank=False)
    data_modyfikacji = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        unique_together = ('wojewodztwo', 'nazwa')

    def __str__(self):
        return self.nazwa + " w " + self.wojewodztwo.nazwa


class Kandydat(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)

    def liczba_glosow(self):
        result = 0
        gminy = Gmina.objects.all()
        for gmina in gminy:
            if self.imie == 'Lech':
                result += gmina.liczba_glosow_oddanych_na_kandydata_nr_1
            else:
                result += gmina.liczba_glosow_oddanych_na_kandydata_nr_2
        return result

    # def wszystkie_glosy(self):
    #     result = 0
    #     gminy = Gmina.objects.all()
    #     for gmina in gminy:
    #         result += gmina.liczba_glosow_oddanych_na_kandydata_nr_1
    #         result += gmina.liczba_glosow_oddanych_na_kandydata_nr_2
    #     return result

    def __str__(self):
        return self.nazwisko.upper() + " " + self.imie
