import datetime

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
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
        user = User.objects.create_user('test', 'test@test.com', 'password')
        user.save()
        test_location = Location.objects.create(name='Test Location', user=user, latitude=0, longitude=0)
        trip = Trip.objects.create(description='Desc', trip_date=timezone.now(), user=user, score=25, location=test_location)
        trip.save()
        self.client.login(username='test', password='password')
        response = self.client.get(reverse('trip_index'))
        self.assertQuerysetEqual(response.context['trip_list'], ['<Trip: Desc>'])
