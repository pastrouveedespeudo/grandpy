import app as script

def hi(name):
    return "hello " + str(name)

def test_hi():
    assert hi("jb") == "hello jb"


def test_apostrohpe():
    parametre = "Salut GrandPY ! Est-ce que tu connais l'adresse"
    sortie = "Salut GrandPY ! Est-ce que tu connais le adresse"
    assert script.apostrohpe(parametre) == sortie

def test_parsing_texte():
    data = "Salut GrandPY ! Est-ce que tu connais le adresse de openclassrooms"
    sortie = "openclassrooms"

    assert script.parsing_texte(data) == sortie


def test_searching():
    para = 'OpenClassRooms'
    sortie = ('OpenClassRooms, 7, Cité Paradis, Porte-St-Denis, 10e, Paris, Île-de-France, France métropolitaine, 75010, France', 48.8747786, 2.3504885)
    assert script.searching(para) == sortie


    
