from geopy.geocoders import Nominatim

geocoder = Nominatim()
adresse = "openclassrooms"
location = geocoder.geocode(adresse, True, 30)
print((location.latitude, location.longitude))


#ok refais les cours ok t'as vu pleins de tuto cool mais y'a certain truk que tu sais pas faire comme ajax

#jy comprend rien, fais ajax et refais les cours et t'aura juste a mettre lalti et la longi et c bon
