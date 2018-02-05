import geopy
from geopy.geocoders import Nominatim

#nom takes an address, and return lat/long coordinates
nom=Nominatim('3995 23rd St, San Francisco, CA 94114') #this format

df['Coordinates']=df['Address'].apply(nom.geocode) #apply method in pandas

#x points to values in Coordinate column
df['Latitude']=df['Coordinate'].apply(lambda x: x.latitude if x!=None else None) 

