# from datetime import datetime
import sys, logging
from rest_framework import serializers
from projekt_zaliczeniowy.models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRodzaj, WojewodztwoRozmiar
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class GminaSerializer(serializers.ModelSerializer):

    def validate_data_modyfikacji(self, value):

        logger.error(value)
        return value

    def validate(self, attrs):
        logger.error('ogolnie')
        # date = attrs['data_modyfikacji']
        # gmina = Gmina.objects.get(pk=pk)
        # if gmina.data_modyfikacji != date:
        #     raise ValueError
        # attrs['data_modyfikacji'] = datetime.now().isoformat()
        # raise serializers.ValidationError('hehe')
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
