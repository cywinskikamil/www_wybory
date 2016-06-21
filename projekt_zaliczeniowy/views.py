import simplejson
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User

from projekt_zaliczeniowy.models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRozmiar, WojewodztwoRodzaj
from projekt_zaliczeniowy.serializers import GminaSerializer, WojewodztwoSerializer, KandydatSerializer, \
    WojewodztwoRodzajSerializer, WojewodztwoRozmiarSerializer, UserSerializer


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


def login_view(request):
    if request.method == "POST":
        if request.user.is_authenticated():
            django_logout(request)
            return_dict = {'action': 'logout', 'result': 'success'}
            json = simplejson.dumps(return_dict)
            return HttpResponse(json)
        else:
            data = simplejson.loads(request.body)
            username = data['username']
            password = data['password']

            return_dict = {'action': 'login', 'result': 'failure'}
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return_dict = {'action': 'login', 'result': 'success'}

            json = simplejson.dumps(return_dict)
            return HttpResponse(json)


def start(request):
    return render(request, 'start.html')

# def date_handler(obj):
#     if hasattr(obj, 'isoformat'):
#         return obj.isoformat()
#     else:
#         raise TypeError
