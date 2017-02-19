from django.test import TestCase
from locations.services import USGSService
from datetime import date


# Create your tests here.
class LocationTest(TestCase):
    def test_USGS(self):
        good_trip_date = date(2016, 5, 27)
        flow = USGSService.fetch_river_data(key='01046500', trip_date=good_trip_date)
        assert flow == '3900'
