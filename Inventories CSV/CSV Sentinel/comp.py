## Yassine Chouiti, 2025
## Ajout d'un algorithme de parcours de liste en O(n) avec implémentation de hashmap (dictionnaire) pour assigner un ID à chaque organisation
## Cela me permettra de faire un tri plus poussé sur Sheets

with open("Full_Ninja_2.csv", "r", encoding="utf-8") as ninja:
    ninja2 = ninja.readlines()

with open("Full_Sentinel.csv", "r", encoding="utf-8") as sentinel:
    sentinel2 = sentinel.readlines()

postes_ninja = [x.split(",")[0:2] for x in ninja2[1:]]
postes_sentinel = [x.split(",")[0].replace("\"","") for x in sentinel2[1:]]

print(postes_ninja)

sans_sentinel = open("Sans_Sentinel.csv", "a", encoding='utf-8')
sans_sentinel.write(f'ID Organisation,{','.join(ninja2[0].split(",")[0:2])}\n')

ctr = 0

id_orga = {}
id_ind = 0

for poste in postes_ninja:
    if poste[0] not in postes_sentinel:
        ctr += 1 # Compter le nombre de poste en sortie de programme

        # Masterclass :  check dans un dictionnaire si l'ID orga est déjà présent
        # --> ajoute à l'index 0 du "poste" l'id orga (right shift les données) trouvé depuis le dico id_orga
        # --> S'il n'existe pas, l'ajoute à id_orga
        # --> enfin, ajoute l'ID orga au poste
        try:
            poste.insert(0, str(id_orga[poste[1]]))
        except:
            id_ind += 1
            id_orga[poste[1]] = id_ind
        finally:
            if len(poste) == 2: # Sinon il ajoute 2 fois et ajoute les nom des pc en tant qu'id orga
                poste.insert(0, str(id_orga[poste[1]]))

        sans_sentinel.write(f'{','.join(poste)}\n') # to add carriage return

print(f'Postes sans sentinel : {ctr}')




