#Importing the required modules
import pandas as pd
import geopy.distance as dist
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
 
#Creating a dataframe with address of locations we want to reterive
locat = ['Saint Louis, Missouri' , 'Chicago, Illinois',\
         'Columbus, Ohio' , 'Pittsburgh, Pensylvania','Seattle, Washington']
df = pd.DataFrame({'add': locat})
 
#Creating an instance of Nominatim Class
geolocator = Nominatim(user_agent="my_request")
 
#applying the rate limiter wrapper
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
 
#Applying the method to pandas DataFrame
df['location'] = df['add'].apply(geocode)
df['Lat'] = df['location'].apply(lambda x: x.latitude if x else None)
df['Lon'] = df['location'].apply(lambda x: x.longitude if x else None)


coord1 = (df.iloc[0]['Lat'], df.iloc[0]['Lon'])
coord2 = (df.iloc[1]['Lat'], df.iloc[1]['Lon'])

print(dist.geodesic(coord1, coord2).miles)