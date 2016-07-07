import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase

from .models import Trip
from locations.models import Location


class TripMethodTests(TestCase):

    def test_score_limit(self):
        """
        Scores must be limited to <=100
        """
        working_trip = Trip(score=99)
        self.assertEqual(working_trip.score, 99)

    def test_index_view(self):
        test_location = Location.objects.create(name='Test Location', latitude=0, longitude=0)
        test_trip = Trip.objects.create(description='Desc', trip_date=timezone.now(), score=25, location=test_location)
        response = self.client.get(reverse('index'))
        print response.context['trip_list']
        self.assertQuerysetEqual(response.context['trip_list'],['<Trip: Desc>'])
