
import os
from PIL import Image

class image:

    @classmethod
    def reziser(cls, modele):
        
        cls.modele = modele

        path = r"C:\Users\jeanbaptiste\nouveaugrandpy\flaskk\app\static\images\tourne\{}"
        osPath = r"C:\Users\jeanbaptiste\nouveaugrandpy\flaskk\app\static\images\tourne"
        src = path.format(cls.modele)
        
        img = Image.open(src)
        
        largeur = img.size[0]
        hauteur = img.size[1]

        os.chdir(osPath)
        liste = os.listdir()
        print(liste)

        for i in liste:
            
            im = Image.open(i)
            im = im.resize((largeur, hauteur), Image.ANTIALIAS)
            name = str(i)+'.jpg'
            im.save(name)


if __name__ == "__main__":

    yo = image()
    yo.reziser("tourne3.jpg")
