from django.http import HttpResponse


# Trip access
def index(request):
    return list_trips(request)

def trip_detail(request, trip_id):
    return HttpResponse('You found trip %s' % trip_id)

def list_trips(request):
    return HttpResponse('All Trips')

