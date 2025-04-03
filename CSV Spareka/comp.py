### YASSINE CHOUITI
### Script qui traite des données (inventaire PC) en CSV selon l'ordre suivant : 
### ID Original,N° de série,Marque,Modèle,Type de garantie,Statut,Inventaire PC,Société,Nom de l'appareil,Utilisateur Nom/prénom,Date d'achat,Date de fin de garantie
### ORDRE : 
### 1) Ajoute les postes avec agent en premier (syntaxe ancien inventaire)
### 2) Ajoute les postes avec agent MAIS absent dans l'ancien inventaire (= nouveau poste) en ajoutant un ID (car syntaxe csv Ninja)
### 3) Ajoute les postes sans agent (syntaxe ancien inventaire)
### 4) Affiche les dernières ligne de chaque étape pour surligner dans Sheets après

# 2 csv inventory file
with open('Data_Ninja.csv', 'r', encoding='utf-8') as ninja_file:
    new_sparek = ninja_file.readlines()
with open('Data_Lionel.csv', 'r', encoding='utf-8') as lionel_file:
    old_sparek = lionel_file.readlines()

# result file : le nouveau fichier sera organisé :
# Première partie (haute) : postes avec agent
# Deuxième partie (basse) : postes sans agent
new_file = open("Avec_Sans.csv", "w", encoding='utf-8')

# copie la première ligne csv
new_file.write(old_sparek[0]) 

# fetch computer in list
ninja_postes = [x.split(",") for x in new_sparek[1:]]
old_postes = [x.split(",") for x in old_sparek[1:]]

# liste sans agent (à modifier)
sans_agents = [x.split(",") for x in old_sparek[1:]]

# Poste avec agent mais pas dans l'ancien inventaires
new_postes = []

# pour me repérer
dernières_lignes = []

temp = None
# ajoute dans un premier temps les lignes des postes qui sont dans l'ancien inventaire et qui ont l'agent
for poste in old_postes:
    #print(poste)
    if poste[1] in [x[0] for x in ninja_postes]: # liste qui contient les numéro de serie des postes avec agent
        new_file.write(",".join(poste))
        sans_agents.remove(poste)
        temp = poste

# Permet de retrouver la dernière ligne à la fin de l'éxecution de la boucle
dernières_lignes.append(temp)

# Ajoute dans une liste les postes recensé sur Ninja qui ne sont pas dans l'ancien inventaire
for new in ninja_postes:
    last_id = int(old_postes[-1][0]) # récup le plus grand ID de poste (dernier élément car liste trié)
    if new[0] not in [x[1] for x in old_postes]:
        # penser à reformater manuellement cette ligne car elle est syntaxiquement différente de l'ancienne inventaire (csv)
        last_id += 1 # incrémente le dernier ID 
        new.insert(0, str(last_id))
        new_file.write(",".join(new))
        new_postes.append(new) # to keep track of newly added computer
        temp = new # pour récup dernier ligne (avec agent, pour tri)

# cf. ligne 33
dernières_lignes.append(temp)

# Puis ajoute tous les postes qui ne sont pas sur Ninja (= sans agent)
for postes in sans_agents:
    new_file.write(",".join(postes))

print(f'* Postes avec agent : {len(ninja_postes)}\n--> Dernière ligne AVEC AGENT :\n{dernières_lignes[0]}\
      \n\n* Postes sans agent : {len(sans_agents)}\
      \n\n* Nouveau(x) Postes : {len(new_postes)}\n--> Dernière ligne NOUVEAU POSTE : \n{dernières_lignes[1]}\
      \n\n* Total : {len(old_postes)}')
