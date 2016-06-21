from django.conf.urls import url, include
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
    url(r'^wojewodztwosrozmiar/(?P<pk>[0-9]+)/$', views.WojewodztwoRozmiarDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^$', views.start, name='start'),
    url(r'^login', views.login_view, name='login'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]