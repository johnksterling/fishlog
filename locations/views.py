from django.shortcuts import render
from django.http import HttpResponse
from locations.models import Location


# Location access
def index(request):
    return list_locations(request)


def location_detail(request, location_id):
    return HttpResponse('You found location %s' % location_id)


def delete_location(request, location_id):
    return HttpResponse('Deleting %s' % location_id)


def view_map(request):
    location_list = Location.objects.all().order_by('name')[:5]
    context = {
        'location_list': location_list,
    }
    return render(request, 'locations/map.html', context)


def list_locations(request):
    location_list = Location.objects.all().order_by('name')[:5]
    context = {
        'location_list': location_list,
    }
    return render(request, 'locations/index.html', context)
