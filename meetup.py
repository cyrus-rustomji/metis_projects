import urllib.request
import requests
import csv

# secrets.py is ignored by git
from secrets import meetup_auth_token

def fetch_data_and_write_csv(station_coordinates):
    headers = {"Authorization": meetup_auth_token }
    base_url = 'https://api.meetup.com/find/upcoming_events'
    events = []
    # quarter mile
    search_radius = 1
    search_query = 'women'
    endpoint = lambda lt, lg: '{0}?lat={1}&lon={2}&radius={3}&text={4}&key={5}'.format(base_url, lt, lg, search_radius, search_query, meetup_auth_token)

    for sc in station_coordinates:
        station, latitude, longitude = sc
        meetup_data = requests.get(endpoint(latitude, longitude), headers=headers).json()
        print(meetup_data)
        for event in meetup_data['events']:
            events.append({
                'group_name': event.get('group', {}).get('name', ''),
                'yes_rsvp_count': event.get('yes_rsvp_count', ''),
                'latitude': event.get('venue', {}).get('lat', ''),
                'longitude': event.get('venue', {}).get('lon', ''),
                'station': station
            })

    with open('meetup_data.csv', 'w') as meetup_data_csv:
        dict_writer = csv.DictWriter(meetup_data_csv, events[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(events)

station_coordinates = [
    ['34 ST-PENN STA', 40.750373, -73.991057],
    ['GRD CNTRL-42 ST', 40.751776, -73.976848],
    ['34 ST-HERALD SQ', 40.749719, -73.987823],
    ['23 ST', 40.744081, -73.995657],
    ['42 ST-PORT AUTH', 40.757308, -73.989735],
    ['59 ST', 40.762526, -73.967967],
    ['TIMES SQ-42 ST', 40.755290, -73.987495],
    ['14 ST-UNION SQ', 40.734673, -73.989951],
    ['FULTON ST', 40.709416, -74.006571],
    ['BEDFORD PK BLVD', 40.689627, -73.953522],
    ['BEDFORD PK BLVD', 40.873244, -73.887138],
    ['BEDFORD PK BLVD', 40.873412, -73.890064]
]

fetch_data_and_write_csv(station_coordinates)
