import simplejson
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from projekt_zaliczeniowy.models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRozmiar, WojewodztwoRodzaj
from projekt_zaliczeniowy.serializers import GminaSerializer, WojewodztwoSerializer, KandydatSerializer, \
    WojewodztwoRodzajSerializer, WojewodztwoRozmiarSerializer


class GminaList(generics.ListCreateAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer


class GminaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gmina.objects.all()
    serializer_class = GminaSerializer


class WojewodztwoList(generics.ListCreateAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer


class WojewodztwoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wojewodztwo.objects.all()
    serializer_class = WojewodztwoSerializer


class WojewodztwoRodzajList(generics.ListCreateAPIView):
    queryset = WojewodztwoRodzaj.objects.all()
    serializer_class = WojewodztwoRodzajSerializer


class WojewodztwoRodzajDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WojewodztwoRodzaj.objects.all()
    serializer_class = WojewodztwoRodzajSerializer


class WojewodztwoRozmiarList(generics.ListCreateAPIView):
    queryset = WojewodztwoRozmiar.objects.all()
    serializer_class = WojewodztwoRozmiarSerializer


class WojewodztwoRozmiarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WojewodztwoRozmiar.objects.all()
    serializer_class = WojewodztwoRozmiarSerializer


class KandydatList(generics.ListCreateAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer


class KandydatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kandydat.objects.all()
    serializer_class = KandydatSerializer


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

#
# def stworz_do_modala(m):
#     # desired_format = '%Y-%m-%d %H:%M:%S+%f:%f'
#     if not m.data_modyfikacji:
#         return {
#             'id': m.id,
#             'name': 'nie ma daty',
#             'allowed': m.liczba_uprawnionych,
#             'sheets': m.liczba_wydanych_kart,
#             'votes': m.liczba_uprawnionych,
#             'valid_votes': m.liczba_wydanych_kart,
#             'c1': m.liczba_glosow_oddanych_na_kandydata_nr_1,
#             'c2': m.liczba_glosow_oddanych_na_kandydata_nr_2,
#             'pc1': round(m.liczba_glosow_oddanych_na_kandydata_nr_1 / m.liczba_wydanych_kart * 100, 2),
#             'pc2': round(m.liczba_glosow_oddanych_na_kandydata_nr_2 / m.liczba_wydanych_kart * 100, 2),
#         }
#
#     return {
#         'id': m.id,
#         'name': m.nazwa,
#         'allowed': m.liczba_uprawnionych,
#         'sheets': m.liczba_wydanych_kart,
#         'votes': m.liczba_uprawnionych,
#         'valid_votes': m.liczba_wydanych_kart,
#         'c1': m.liczba_glosow_oddanych_na_kandydata_nr_1,
#         'c2': m.liczba_glosow_oddanych_na_kandydata_nr_2,
#         'pc1': round(m.liczba_glosow_oddanych_na_kandydata_nr_1/m.liczba_wydanych_kart * 100, 2),
#         'pc2': round(m.liczba_glosow_oddanych_na_kandydata_nr_2/m.liczba_wydanych_kart * 100, 2),
#         'date': str(m.data_modyfikacji)
#     }
#
#
# def modale_przez_wojewodztwo(request, mwojewodztwo):
#     if request.method == 'GET':
#         modale = []
#         if mwojewodztwo:
#             m_by_province = Gmina.objects.filter(wojewodztwo=mwojewodztwo)
#             for m in m_by_province:
#                 modale.append(stworz_do_modala(m))
#
#         json_municipalities = simplejson.dumps(modale)
#
#         return HttpResponse(json_municipalities)
#
#
# def modale_przez_rodzaj(request, rodzaj):
#     if request.method == 'GET':
#         modale = []
#         if rodzaj:
#             m_by_type = Gmina.objects.filter(rodzaj=rodzaj)
#             for m in m_by_type:
#                 modale.append(stworz_do_modala(m))
#
#         json_municipalities = simplejson.dumps(modale)
#
#         return HttpResponse(json_municipalities)
#
#
# def m_filter(min, max):
#     if max > 0:
#         return Gmina.objects.filter(liczba_mieszkancow__gte=min, liczba_mieszkancow__lte=max)
#     else:
#         return Gmina.objects.filter(liczba_mieszkancow__gte=min)
#
#
# def modale_przez_rozmiar(request, min, max):
#
#     if request.method == 'GET':
#
#         modale = []
#
#         min = int(min)
#         max = int(max)
#
#         m_by_size = m_filter(min, max)
#
#         for m in m_by_size:
#             modale.append(stworz_do_modala(m))
#
#         json_municipalities = simplejson.dumps(modale)
#
#         return HttpResponse(json_municipalities)
#
#
# def incorrect_votes(first_votes, second_votes, all_votes):
#     return first_votes <= 0 or second_votes <= 0 or first_votes + second_votes != all_votes
#
#
# def submit(request):
#     desired_format = '%Y-%m-%d %H-%M'
#
#     if request.method == "POST":
#         data = simplejson.loads(request.body)
#         myid = data['community_id']
#         first_votes = int(data['first_votes'])
#         second_votes = int(data['second_votes'])
#         date_modified = data['date_modified']
#         all_votes = int(data['all_votes'])
#
#         community = Gmina.objects.get(id=myid)
#         d1 = community.data_modyfikacji
#         d2 = date_modified
#
#         # print(d1, " ", d2)
#         #
#         if str(d1) == str(d2) and not incorrect_votes(first_votes, second_votes, all_votes):
#             current_date = datetime.now().isoformat()
#             community.liczba_glosow_oddanych_na_kandydata_nr_1 = first_votes
#             community.liczba_glosow_oddanych_na_kandydata_nr_2 = second_votes
#             community.data_modyfikacji = current_date
#             community.save()
#             return_dict = {
#                 'result': 'success',
#                 'date_modified': current_date,
#                 'gmina_nazwa': community.nazwa
#             }
#             json = simplejson.dumps(return_dict, default=date_handler)
#             return HttpResponse(json)
#         else:
#             return_dict = {
#                 'result': 'failure',
#                 'pierwsza': str(d1),
#                 'druga': str(d2),
#             }
#             json2 = simplejson.dumps(return_dict)
#             return HttpResponse(json2)

# def date_handler(obj):
#     if hasattr(obj, 'isoformat'):
#         return obj.isoformat()
#     else:
#         raise TypeError
#
#

#
#

#
#