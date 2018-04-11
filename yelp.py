import urllib.request
import requests
import csv

headers = {"Authorization":"Bearer 421BA_xYdh0Xq7dGFe1pkaI7WqWnJ5UcHZZgg8WwNQ34_7GlbvrRU4dnCGE9dmXOZrX5xVFquiL9X4B35qBuBcA4Jt1D9ys3h0z6pxnfFd8Frf9UYXQ9xKMDOnjNWnYx"}
base_url = 'https://api.yelp.com/v3/businesses/search'
station_coordinates = [{'station': 'Grand Central Station', 'latitude': 40.753, 'longitude': -73.9771}]
businesses = []
# half mile in meters
search_radius = int(0.5 / 0.00062137)
endpoint = lambda lt, lg: '{0}?latitude={1}&longitude={2}&radius={3}&limit=50'.format(base_url, lt, lg, search_radius)

for sc in station_coordinates:
    yelp_data = requests.get(endpoint(sc['latitude'], sc['longitude']), headers=headers).json()
    for business in yelp_data['businesses']:
        businesses.append({
            'name': business.get('name', ''),
            'price': business.get('price', ''),
            'rating': business.get('rating', ''),
            'latitude': business.get('latitude', ''),
            'longitude': business.get('longitude', ''),
            'station': sc.get('station', ''),
            'distance': business.get('distance', '')
        })

with open('yelp_data.csv', 'w') as yelp_data_csv:
    dict_writer = csv.DictWriter(yelp_data_csv, businesses[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(businesses)
