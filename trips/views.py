from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from trips.forms import TripForm
from trips.models import Trip, TripPicture


# Trip access
def index(request):
    return list_trips(request)


def new_trip(request):
    trip = Trip(user=request.user)
    form = TripForm(instance=trip)
    return render(request, 'trips/new_trip.html', {'form': form})


def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    form = TripForm(instance=trip)
    form.id = trip.id
    return render(request, 'trips/detail.html', {'form': form})


def list_trips(request):
    trip_list = Trip.objects.filter(user=request.user).order_by('-trip_date')[:5]
    context = {
        'trip_list': trip_list,
    }
    return render(request, 'trips/index.html', context)


def create_trip(request):
    f = TripForm(data=request.POST)
    f.save()
    return list_trips(request)


def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    trip.delete()
    return list_trips(request)


def update_trip(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    f = TripForm(data=request.POST, instance=trip)
    if f.is_valid():
        f.save()
        return list_trips(request)
    else:
        f.id = trip_id
        return render(request, 'trips/detail.html', {'form': f})


class CreateTripView(FormView):
    template_name = 'trips/new_trip.html'
    form_class = TripForm
    success_url = '/trips/'

    def form_valid(self, form):
        trip = get_object_or_404(Trip, pk=form.get('id'))
        for each in form.cleaned_data['attachments']:
            TripPicture.objects.create(image=each, trip=trip)
        return super(CreateTripView, self).form_valid(form)
