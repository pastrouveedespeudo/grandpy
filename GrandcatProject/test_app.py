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
