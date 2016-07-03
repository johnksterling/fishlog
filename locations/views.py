from django.http import HttpResponse

# Location access
def index(request):
    return list_locations(request)

def location_detail(request, location_id):
    return HttpResponse('You found location %s' % location_id)

def list_locations(request):
    return HttpResponse('All Locations')
