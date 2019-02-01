import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib

class FAUTAJAX:

    @classmethod
    def rechercher(cls, recherche):

        cls.liste = []
        cls.recherche = recherche
        path = "https://www.google.com/maps/search/{}".format(str(cls.recherche))


        with urllib.request.urlopen(path) as url:
            s = url.read()

        cls.liste.append(s)

     

    @classmethod
    def recherche_liste(cls):
        classe = "textarea"
        search = str(cls.liste).find(str(classe))
    
        print(search)
        print(cls.liste[search-200:search])





yo = FAUTAJAX()
yo.rechercher("openclassrooms")
yo.recherche_liste()
