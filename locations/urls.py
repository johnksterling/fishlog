from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.index, name='location_index'),
    url(r'^(?P<location_id>[0-9]+)/delete$', login_required(views.delete_location),
        name='delete_location'),
    url(r'^(?P<location_id>[0-9]+)/$', views.location_detail, name='location_detail'),
    url(r'^map$', views.view_map, name='view_map'),
    url(r'^(?P<location_id>[0-9]+)/update$', login_required(views.update_location), name='update_location'),
    url(r'^create$', login_required(views.create_location), name='create_location'),
    url(r'^new$', login_required(views.new_location), name='new_location'),
]
