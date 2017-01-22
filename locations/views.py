from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from locations.models import Location
from locations.forms import LocationForm


# Location access
def index(request):
    return list_locations(request)


def location_detail(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    form = LocationForm(instance=location)
    form.id = location.id
    return render(request, 'locations/detail.html', {'form': form})


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


def update_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    f = LocationForm(data=request.POST, instance=location)
    f.save()
    return list_locations(request)


def create_location(request):
    f = LocationForm(data=request.POST)
    f.save()
    return list_locations(request)


def new_location(request):
    location = Location(user=request.user)
    form = LocationForm(instance=location)
    return render(request, 'locations/new_location.html', {'form': form})

