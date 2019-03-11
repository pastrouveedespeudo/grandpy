
@app.route('/wiki', methods=["POST"]) 
def wiki():
    b = ""
    data_wiki = request.form['data']

    nettoyage = apostrohpe(data_wiki)
    dernier_mot = parsing_texte(nettoyage)
    
    print(dernier_mot,'74777777777777777777777777777777777777777')
    search = searching(dernier_mot)
    print(search,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    c = select_wikipedia(search)

    
    if data_wiki:
    
        print(search,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        return jsonify({'data':c})

    #return jsonify({'error':'...'})

    

def select_wikipedia(para):
    liste = [[],[],[],[],[],[],[],[],[],[],[],
             [],[],[],[],[],[],[],[],[],[],[]]
    liste2 = []

    LISTE4 = [[],[],[],[],[],[],[],[],[],[],[],
              [],[],[],[],[],[],[],[],[],[],[]]

  
    LISTE_WIKI_PARSE = []
    c=0
    print(para,"46498789798798fezzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    para = str(para)
    for i in para:
   
        for j in i:
            if j == ",":
                c+=1
            else:
                liste[c].append(j)
  
    for i in liste:
        if i == []:
            pass
        else:
            liste2.append(i)
    
    for i in liste2:
     
        LISTE_WIKI_PARSE.append("".join(i))

    #print(LISTE_WIKI_PARSE,"89749879879879879879879879878")
    
    c = 0
    for i in LISTE_WIKI_PARSE:
        if i == []:
            pass
        else:
            print(i)
            a = search_wikipedia(i)
            LISTE4[c].append(a)

        c+=1

    print("oyéoyéoyéoyéoéyoéyoéyoyéoyé")
    liliste = []
    if LISTE4 == []:
        return "Rien n'a été trouvé cha c bizzard ma gueule"

    lliste = []
    for i in LISTE4:
        lliste.append(i)
        with open("yo.py", "w", errors = "ignore") as file:
            file.write(str(lliste))

    liste5 = []
    for i in lliste:
        if i == [] or i == [[[], [], [], [], [], [], [], [], [], [], []]]:
            pass
        else:
            if i[0] == []:
                pass
            else:
                c= 0
                for j in i[0][0]:
                    for k in j:
                        c+=1

                if c < 200:
                    pass
                elif c > 10000:
                    pass
                else:
                    liste5 = i[0][0]

    with open("yo.py","w") as file:
        file.write(str(liste5[0][:2000]))
    return str(liste5[0][:2000]) + "..."


def search_wikipedia(para):

    
    LISTE4 = [[],[],[],[],[],[],[],[],[],[],[]]
    
    liste = []
    liste2 = []
    liste3 = []
    compteur = 0
    
    print(para,"000000000012345678913456789")
    path = "https://fr.wikipedia.org/wiki/{}".format(para)

    one = "Vous pouvez partager vos connaissances en"
    two = "Géolocalisation"
    three = " sur un des projets-frères de Wikipédia"
    
    requete = requests.get(path)
    page = requete.content
    soup = BeautifulSoup(page, "html.parser")
    
    propriete = soup.find_all("p")
    for i in propriete:
        liste.append(i.get_text())

    c = 0
    for i in liste:
        c+=1
        
        a = str(i).find(one)
        b = str(i).find(two)
        c = str(i).find(three)
      
        if a >= 0 or b >= 0 or c >= 0:
            pass
        else:
            liste2.append(i)

    
    for i in liste2:
        for j in i:
            if j == "\n":
                pass
            else:
                liste3.append(j)

    liste3 = "".join(liste3)
    #print(liste3)
    a = str(liste3).find(str("la page demandée est vide ou contient"))
    b = str(liste3).find(str("Soit vous avez mal écrit"))
    
    if a < 0 and b < 0 and liste3 != "modifier ":
        LISTE4[compteur].append(str(liste3))
        compteur+=1
        
    liste3 = []  
    #print(LISTE4)
    return LISTE4
 






