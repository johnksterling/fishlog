from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.index), name='trip_index'),
    url(r'^(?P<trip_id>[0-9]+)/$', login_required(views.trip_detail),
        name='trip_detail'),
    url(r'^(?P<trip_id>[0-9]+)/update$', login_required(views.update_trip),
        name='update_trip'),
    url(r'^(?P<trip_id>[0-9]+)/delete$', login_required(views.delete_trip),
        name='delete_trip'),
    url(r'^create$', login_required(views.create_trip), name='create_trip'),
    url(r'^new$', login_required(views.new_trip), name='new_trip'),
]
