"""Génération de la map"""

"""Pour générer notre map on va proposer à l'utilisateur une taille petite, normale, et grande
Notre carte correspondrait souvent à
x x x
x o x
x x x
ici pour une carte la plus petite de 3 avec o le centre ville et x les quartiers il y'aura comme taille 3 petit, 5 moyen et 7 grand"""

def creation_map( dimension) :

    map_globale = []
    quartier = "x"
    centre_ville = "o"

    """Création d'une carte de x de largeur et hauteur dimension"""
    for i in range(0, dimension) :
        map_globale.append([])
        for y in range(0, dimension) :
            map_globale[i].append(quartier)


    """Création du centre ville"""
    if dimension == 3 :
        map_globale[1][1] = centre_ville

    elif dimension == 5 :
        map_globale[2][2] = centre_ville
        map_globale[2][1] = centre_ville
        map_globale[2][3] = centre_ville
        map_globale[1][2] = centre_ville
        map_globale[3][2] = centre_ville

    elif dimension == 7 :
        map_globale[3][3] = centre_ville
        map_globale[3][4] = centre_ville
        map_globale[3][2] = centre_ville
        map_globale[2][3] = centre_ville
        map_globale[2][4] = centre_ville
        map_globale[2][2] = centre_ville
        map_globale[4][3] = centre_ville
        map_globale[4][4] = centre_ville
        map_globale[4][2] = centre_ville

    return map_globale