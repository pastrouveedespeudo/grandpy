from geopy.geocoders import Nominatim
#from tchat import *

class geolocalisation:

    @classmethod
    def recherche(cls, adresse, variable):

        cls.adresse = adresse
        cls.variable = []

        geocoder = Nominatim()
      
        location = geocoder.geocode(adresse, True, 30)
        print("addresse: ",location.address,"yoooooooooooo")
        cls.variable.append(location.address)
        
        print((location.latitude, location.longitude))
        print(cls.variable)
  

        

        #ici on mettra le chat au cas ou c du thcat ou inver.
        
            




#variable = ""

#yo = geolocalisation()
#yo.recherche("OpenClassrooms", variable)
