from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def policz_procent(liczba_na_1, calosc):
    if calosc > 0:
        return round(liczba_na_1 * 100 / calosc, 2), round((calosc - liczba_na_1) * 100 / calosc, 2)
    return 50, 50


def liczba_glosow(kolektyw):
    liczba = 0
    liczba_1 = 0
    for obiekt in kolektyw:
        liczba_1 += obiekt.liczba_glosow_oddanych_na_kandydata_nr_1
        liczba += obiekt.liczba_glosow_oddanych_na_kandydata_nr_1 + obiekt.liczba_glosow_oddanych_na_kandydata_nr_2
    procenty = policz_procent(liczba_1, liczba)
    return liczba, liczba_1, procenty[0], liczba - liczba_1, procenty[1]


def validate_not_spaces(value):
    if value.strip() == '':
        raise ValidationError(u"You must provide more than just whitespace.")


class WojewodztwoRozmiar(models.Model):
    dolny_limit = models.IntegerField(default=0, blank=False)
    gorny_limit = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return str(self.dolny_limit) + " " + str(self.gorny_limit)

    def suma_glosow(self):
        return liczba_glosow(Gmina.objects.filter(liczba_mieszkancow__gte=self.dolny_limit,
                                                  liczba_mieszkancow__lte=self.gorny_limit))

    def wszystko(self):
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

    def suma_glosow(self):
        return liczba_glosow(Gmina.objects.filter(rodzaj=self.rodzaj))

    def wszystko(self):
        return Gmina.objects.filter(rodzaj=self.rodzaj).values()


class Wojewodztwo(models.Model):
    nazwa = models.CharField(max_length=30)

    def __str__(self):
        return self.nazwa

    def suma_glosow(self):
        return liczba_glosow(Gmina.objects.filter(wojewodztwo=self.id))

    def wszystko(self):
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

    def suma_glosow(self):
        return liczba_glosow([self])

    def clean(self):
        if self.liczba_glosow_oddanych_na_kandydata_nr_1 < 0 or self.liczba_glosow_oddanych_na_kandydata_nr_2 < 0:
            raise ValidationError('ujemna liczba glosow')
        if self.liczba_glosow_oddanych_na_kandydata_nr_1 + self.liczba_glosow_oddanych_na_kandydata_nr_2 > \
                self.liczba_wydanych_kart:
            raise ValidationError('niezgodan liczba głosów')


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

    def wszystkie_glosy(self):
        result = 0
        gminy = Gmina.objects.all()
        for gmina in gminy:
            result += gmina.liczba_glosow_oddanych_na_kandydata_nr_1
            result += gmina.liczba_glosow_oddanych_na_kandydata_nr_2
        return result

    def __str__(self):
        return self.nazwisko.upper() + " " + self.imie

