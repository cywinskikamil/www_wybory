import logging
from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User

from projekt_zaliczeniowy.models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRozmiar, WojewodztwoRodzaj
from projekt_zaliczeniowy.serializers import GminaSerializer, WojewodztwoSerializer, KandydatSerializer, \
    WojewodztwoRodzajSerializer, WojewodztwoRozmiarSerializer, UserSerializer

logger = logging.getLogger(__name__)


class GminaList(generics.ListCreateAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class GminaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoList(generics.ListCreateAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoRodzajList(generics.ListCreateAPIView):
    queryset = WojewodztwoRodzaj.objects.all()
    serializer_class = WojewodztwoRodzajSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoRodzajDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WojewodztwoRodzaj.objects.all()
    serializer_class = WojewodztwoRodzajSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoRozmiarList(generics.ListCreateAPIView):
    queryset = WojewodztwoRozmiar.objects.all()
    serializer_class = WojewodztwoRozmiarSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class WojewodztwoRozmiarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WojewodztwoRozmiar.objects.all()
    serializer_class = WojewodztwoRozmiarSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class KandydatList(generics.ListCreateAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class KandydatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer
    permissions = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def start(request):
    return render(request, 'start.html')

# def date_handler(obj):
#     if hasattr(obj, 'isoformat'):
#         return obj.isoformat()
#     else:
#         raise TypeError
