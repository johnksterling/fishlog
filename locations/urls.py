from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<location_id>[0-9]+)/delete$', login_required(views.delete_location),
        name='delete_location'),
    url(r'^(?P<location_id>[0-9]+)/$', views.location_detail, name='location_detail'),
]
