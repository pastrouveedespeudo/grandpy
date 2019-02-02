from geopy.geocoders import Nominatim

geocoder = Nominatim()
adresse = "openclassrooms"
location = geocoder.geocode(adresse, True, 30)
print((location.latitude, location.longitude))
print(location.address)


#(48.8747786, 2.3504885)
#OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France
#faut mettre les coordonnées dans le truk

#je sais faut utiliser appi google map mais au pire prend un air ébété e tu dis oui mais ca va plus vite, ou ca revient au meme

#suivis d'un je sais pas ou au pire fais le faut juste faire un truk et jlutilise en affichant la map 

#nik passons au design mtn :D et fais une mini base de donnée

#avec register pour compenser ca 
