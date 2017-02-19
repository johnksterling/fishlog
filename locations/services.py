import requests


USGS_URL = 'http://waterservices.usgs.gov/nwis/iv/?format=json&sites={0}&startDT={1}T13:00-0500&endDT={2}T15:00-0500&parameterCd=00060,00065&siteType=ST&siteStatus=all'


class USGSService:
    def fetch_river_data(key, trip_date):
        formatted_date = trip_date.strftime('%Y-%m-%d')
        formatted_url = USGS_URL.format(key, formatted_date, formatted_date)
        response = requests.get(url=formatted_url)
        resp_parsed = response.json()
        return resp_parsed['value']['timeSeries'][0]['values'][0]['value'][0]['value']
