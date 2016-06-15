from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^gminas/$', views.GminaList.as_view()),
    url(r'^gminas/(?P<pk>\d+)/$', views.GminaDetail.as_view()),
    url(r'^kandydats/$', views.KandydatList.as_view()),
    url(r'^kandydats/(?P<pk>[0-9]+)/$', views.KandydatDetail.as_view()),
    url(r'^wojewodztwos/$', views.WojewodztwoList.as_view()),
    url(r'^wojewodztwos/(?P<pk>[0-9]+)/$', views.WojewodztwoDetail.as_view()),
    url(r'^wojewodztwosrodzaj/$', views.WojewodztwoRodzajList.as_view()),
    url(r'^wojewodztwosrodzaj/(?P<pk>[0-9]+)/$', views.WojewodztwoRodzajDetail.as_view()),
    url(r'^wojewodztwosrozmiar/$', views.WojewodztwoRozmiarList.as_view()),
    url(r'^wojewodztwosrozmiar/(?P<pk>[0-9]+)/$', views.WojewodztwoRodzajDetail.as_view()),
    url(r'^$', views.start, name='start'),
    url(r'^login', views.login_view, name='login'),
    # url(r'^modale_przez_wojewodztwo/(\d+)/$',
    #     views.modale_przez_wojewodztwo,
    #     name='modale_przez_wojewodztwo'),
    # url(r'^modale_przez_rodzaj/(\w+)/$',
    #     views.modale_przez_rodzaj,
    #     name='modale_przez_rodzaj'),
    # url(r'^modale_przez_rozmiar/(\d+)/(\d+)/$',
    #     views.modale_przez_rozmiar,
    #     name='modale_przez_rozmiar'),
    #
    # url(r'^submit', views.submit, name='submit'),
]