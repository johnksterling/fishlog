from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.index), name='index'),
    url(r'^(?P<trip_id>[0-9]+)/$', login_required(views.trip_detail), name='trip_detail'),
    url(r'^(?P<trip_id>[0-9]+)/update$', login_required(views.update_trip), name='update_trip'),
    url(r'^new$', login_required(views.new_trip), name='new_trip'),
]
