from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from trips.models import Trip
from django.template import loader

# Trip access
def index(request):
    return list_trips(request)

def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})

def list_trips(request):
    trip_list = Trip.objects.order_by('-trip_date')[:5]
    context = {
        'trip_list': trip_list,
    }
    return render(request, 'trips/index.html', context)
