import phonenumbers

import folium

from mynumber import number

from phonenumbers import geocoder

key = '0c4924517d254736a603b408dbcb22dc'

samNumber=phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(samNumber, "en")
print(yourlocation)


## getservice provider

from phonenumbers import carrier

service_provider= phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder= OpenCageGeocode(key)

query = str (yourlocation)

result = geocoder.geocode(query)
print(result)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

print(lat, lng)

mymap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup= yourlocation).add_to((mymap))
mymap.save("myLocation.html")
