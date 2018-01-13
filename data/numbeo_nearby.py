import pandas as pd
import config, requests, json
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

indices_df = pd.read_csv('./indices/numbeo_ds_indices.csv')

city_list = indices_df['city'].copy()

# replace cities with no vicinity cities with nearby cities that have data
city_list[0] = 'San Jose'
city_list[10] = 'San Jose'
city_list[11] = 'Venice Beach'
city_list[12] = 'Mountain View'
city_list[13] = 'Arvada'
city_list[14] = 'Arvada'
city_list[16] = 'McDonough'
city_list[18] = 'Zionsville'
city_list[20] = 'Brookline'
city_list[22] = 'Saint Louis'
city_list[24] = 'Mint Hill'
city_list[25] = 'Knightdale'
city_list[27] = 'Indian Hill'
city_list[28] = 'Cleveland Heights'
city_list[30] = 'Jenkintown'
city_list[32] = 'Richardson'
city_list[35] = 'Murphy'
city_list[40] = 'Clyde Hill'
city_list[41] = 'Tukwila'

counter1 = 0
for city in city_list:
    url = "https://www.numbeo.com/api/close_cities_with_prices?api_key={}&query={}&min_contributors=2&max_distance=100".format(config.key, city)
    response = requests.get(url)
    json_data = json.loads(response.text)

    nearby_cities_df = pd.DataFrame(columns=['short_name', 'latitude', 'longitude', 'city_id', 'city_vicinity'])

    counter2 = 0
    for data in json_data['cities']:
        df_append = pd.DataFrame(data, columns=['short_name', 'latitude', 'longitude', 'city_id'], index=[counter2])
        df_append['city_vicinity'] = indices_df['city'][counter1]

        geolocator = Nominatim()
        location = geolocator.geocode(indices_df['city'][counter1], timeout=10)
        city1 = (location.latitude, location.longitude)
        city2 = (df_append['latitude'][counter2], df_append['longitude'][counter2])
        miles_to = vincenty(city1, city2).miles
        df_append['distance_mi'] = miles_to



        nearby_cities_df = nearby_cities_df.append(df_append)
        sendit = nearby_cities_df[['short_name', 'city_id', 'latitude', 'longitude', 'city_vicinity', 'distance_mi']]

        sendit.to_csv('./cities/{}_vicinity.csv'.format(indices_df['city'][counter1].lower()))
        counter2 += 1

    counter1 += 1
