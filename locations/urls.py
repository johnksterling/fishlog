from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<location_id>[0-9]+)/$', views.location_detail, name='location_detail'),
]
