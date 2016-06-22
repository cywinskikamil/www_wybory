from datetime import datetime
import sys, logging
from rest_framework import serializers
from projekt_zaliczeniowy.models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRodzaj, WojewodztwoRozmiar
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class GminaSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        gmina = Gmina.objects.get(nazwa=attrs['nazwa'])
        gmina_d = str(Gmina.objects.get(nazwa=attrs['nazwa']).data_modyfikacji)[:23]
        gmina_d2 = str(attrs['data_modyfikacji'])[:23]
        if gmina_d != gmina_d2:
            logger.error('no nie')
            raise serializers.ValidationError('Dane zmodyfikowane wcześniej przez kogoś innego o godzinie' + gmina_d)
        attrs['data_modyfikacji'] = datetime.now()
        instance = Gmina(**attrs)
        instance.clean()
        return attrs

    class Meta:
        model = Gmina
        fields = ('id', 'wojewodztwo', 'nazwa', 'rodzaj', 'liczba_mieszkancow', 'liczba_uprawnionych',
                  'liczba_wydanych_kart', 'liczba_glosow_oddanych_na_kandydata_nr_1',
                  'liczba_glosow_oddanych_na_kandydata_nr_2', 'data_modyfikacji', 'suma_glosow')


class WojewodztwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wojewodztwo
        fields = ('id', 'nazwa', 'suma_glosow', 'wszystko')


class WojewodztwoRozmiarSerializer(serializers.ModelSerializer):
    class Meta:
        model = WojewodztwoRozmiar
        fields = ('id', 'dolny_limit', 'gorny_limit', 'suma_glosow', 'wszystko')


class WojewodztwoRodzajSerializer(serializers.ModelSerializer):
    class Meta:
        model = WojewodztwoRodzaj
        fields = ('id', 'rodzaj', 'suma_glosow', 'wszystko')


class KandydatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kandydat
        fields = ('id', 'imie', 'nazwisko', 'liczba_glosow', 'wszystkie_glosy')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
