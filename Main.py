"""Initialisation des modules"""
import pygame
pygame.font.init() #indispensable pour créez des textes avec pygames
import time
import math

from module.creation_map import creation_map
from module.verification import verifie
from module.interface import cree_interface



"""Initialisation de l'écran"""

"""sur la largeur 750 premier px = écran du jeu les dernier 250 pixel = une interface"""
Ecran = pygame.display.set_mode((1000,750))
pygame.display.set_caption("FarWest city")



"""Initialisation de nos classes et de nos variables"""


"""Nos constantes"""


"""La constante score contient les scores utile au jeu"""
score = {"energie" : 0, "argent" : 5, "habithant" : 0, "impot": 0, "argent_max" : 100}
tuto = {}
nbr_tuto = 1
inventaire = {"cereale" : 0}


debut = time.time()
click = 0
tuple_souris = None
objet_selectionner = None
endroit = ["all", None]
souris_change = True


nbr_iteration_20 = 0

"""Nos textures qu'on initialise maintenant pour éviter toute perte de FPS après"""
route_rond = pygame.image.load('textures/route_rond.png').convert_alpha()
route_hauteur = pygame.image.load('textures/route_hauteur.png').convert_alpha()
route_cote = pygame.image.load('textures/route_cote.png').convert_alpha()

champ_0 = pygame.image.load('textures/champ.png').convert_alpha()
champ_1 = pygame.image.load('textures/champ1.png').convert_alpha()



debug = 0

"""Cette classe sert pour tout ce qui est l'interface de droite"""
class GUI() :

    def __init__(self, texture="", pos_x=0, pos_y=0) :
        self.texture = texture
        self.pos_x = 750 + pos_x
        self.pos_y = pos_y


    def GUI_affiche(self) :
        global Ecran
        Ecran.blit(self.texture, (self.pos_x, self.pos_y))



"""Nos instance de la classe GUI"""
GUI_FOND = GUI(texture = pygame.image.load('textures/GUI_Fond.png').convert_alpha())






"""Cette classe sert globalement à tous ce qui est objet qu'on affiche à l'écran principal maison, zone, et meme le curseur"""
class batiment() :



    """L'initialisation"""
    def __init__(self, texture="", taille = 1, elec = 0, lieu="all", click=None, habithant=0, impot=0, pose=0, evolue = None, cd_evolue = None, cout_evolue = 0, unique="osef", argent_max = None, recup = None, cereale = 0, temps = None, special = None, tutoriel = None) :
        self.texture = texture #permet de gérer les textures
        self.taille = taille #permet de gérer la taille
        self.elec = elec #permet de gérer l'électricité en changeant le score à l'ajout ou lorsqu'on enlève un batiment producteur
        self.lieu = lieu #permet de dire dans quelle zone le lieu doit être mis
        self.click = click #interface qui s'active si on clique sur un batiment
        self.habithant = habithant #Nombre d'habithant que fais gagnez le batiment
        self.impot = impot #savoir combien d'impot fait gagnez le batiment
        self.pose = pose #savoir combien d'argent le batiment coute à la pose
        self.evolue = evolue #savoir en quoi le batiment evolue
        self.cd_evolue = cd_evolue #savoir les conditions d'évolution
        self.cout_evolue = cout_evolue #information sur le coup d'évolution
        self.argent_max = argent_max #nombre de pièce maximum que l'on peut avoir
        self.recup = recup #savoir si on peut récuperer l'objet (on le met en string car après c'est soumis à une fonction eval)
        self.cereale = cereale #combien de cérale prend l'objet si il est recup
        self.temps = temps #si le batiment est régis à des lois temporelles
        self.special = special #si le batiment à une utilité spéciale
        self.tutoriel = tutoriel #savoir si le batiment est utiliser pour le tutoriel


        self.unique = unique #inormation pour savoir si le batiment est unique

        if self.unique != "osef" :
            score[self.unique] = False

        if self.tutoriel != None :
            tuto[self.tutoriel] = False









    """Notre fonction pour afficher"""
    def affiche(self, x, y) :
        global Ecran
        Ecran.blit(self.texture, (x, y))







"""Notre classe pour les évenement"""
class event() :

    def __init__(self, argent = 0, proba = 100, evalue="True") :
        self.argent = argent
        self.proba = proba
        self.evalue = evalue

    def vol(self, score) :
        if eval(self.evalue) :
            import random
            tirage = random.randint(1, 100)

            if tirage < self.proba or self.proba == 0 :
                score["argent"] *= self.argent
                return score
        else : return score



"""Nos instance de la classe evenement"""
braque = event(argent=-0.1, proba=10, evalue = "score['have_bank'] == True and score['have_sherif'] == False")


"""Les choses se servant de notre classe batiment"""
"""Notre monde"""
dimension = 3
la_map = creation_map(dimension)
map = creation_map(dimension)
dico_map = [ [ [] for i in range(0, dimension)] for i in range(0,dimension)]





"""Nos variable de la classe batiment"""



"""Les curseur"""
curseur = batiment(pygame.image.load('textures/curseur.png').convert_alpha())
curseur1 = batiment(pygame.image.load('textures/curseur1.png').convert_alpha())
curseur2 = batiment(pygame.image.load('textures/curseur2.png').convert_alpha())
curseur3 = batiment(pygame.image.load('textures/curseur3.png').convert_alpha())
curseur4 = batiment(pygame.image.load('textures/curseur4.png').convert_alpha())

bande_x = batiment(pygame.image.load('textures/10_qd.png').convert_alpha())
bande_y = batiment(pygame.image.load('textures/10_zs.png').convert_alpha())









"""Le hand est un objet de 10 de large et hauteur on le place quand on veut placer des batiments assez grands"""
hand = batiment(pygame.image.load('textures/hand.png').convert_alpha(), taille=1)

"""le vide est comme le hand il indique que l'on peut placer des choses il fait également 10 * 10 de pixel"""
vide = batiment(pygame.image.load('textures/vide.png').convert_alpha(), taille=1)




""" Les dictionnaire pour dès qu'on clique """
"""Par soucis d'optimisation on les préremplis et on les actualise après (ici on se situe pas dans une boucle infini mais à l'initialisation qui ne se fait qu'une seule fois"""
CLICK_FELICITATION = {
"fond": (0,180,190),
 "titre" : "Felicitation",
 "resume" : "Vous avez améliorer votre batiment",
 "pose": "0"}


CLICK_BATIMENT = {
"fond": (0,180,190),
 "titre" : "Batiment",
 "resume" : "Accéder au menue des batiments",
 "pose": "0"}

CLICK_BATIMENT_DEBUT = {
"fond": (0,180,190),
 "titre" : "Batiment de debut",
 "resume" : "Les batiment pour créer une base solide",
 "pose": "0"}



CLICK_BATIMENT_AVANCER = {
"fond": (0,180,190),
 "titre" : "Batiment avancer",
 "resume" : "Les batiment pour créer une ville",
 "pose": "0"}


CLICK_UTILITAIRE = {
"fond": (255, 128, 192),
 "titre" : "Utilitaire",
 "resume" : "Accéder au menue des utilitaire",
 "pose": "0"
}

CLICK_DECORATION = {
"fond": (255,128, 64),
 "titre" : "Décoration",
 "resume" : "Accéder au menue des décorations",
 "pose": "0"
}


CLICK_GARRE = {
"fond": (0,180,190),
 "titre" : "Garre",
 "resume" : "Un batiment tout frais payer par l'état pour se déplacer, ce place au centre ville",
  "pose": "0"
}


CLICK_MAISON = {
"fond": (0,180,190),
 "titre" : "Maison",
 "resume" : "Les maisons permettent d'obtenir des habithants",
 "consommation" : "0 W",
 "impot" : "+1 K",
 "nbr_habithant": "1",
 "pose": "5 K",
 "evolution" : "Avoir de l'electricité et 7 K d'argent et 10 habithant"}

CLICK_MAISON2 = {
"fond": (0,180,190),
 "titre" : "Maison Améliorer",
 "resume" : "Les maisons permettent d'obtenir plus d'habithant",
 "consommation" : "-2 W",
 "impot" : "+3 K",
 "nbr_habithant": "4",
 "pose": "3 k",
  "evolution" : "Avoir de l'electricité et 30 K d'argent et 100 habithant"}



CLICK_MAISON3 = {
"fond": (0,180,190),
 "titre" : "Maison Améliorer +",
 "resume" : "Les maisons permettent d'obtenir plus d'habithant",
 "consommation" : "-10 W",
 "impot" : "+10 K",
 "nbr_habithant": "10",
 "pose": "3 k"}


CLICK_MINE = {
"fond": (0,180,190),
 "titre" : "Mine",
 "resume" : "Les mines se placent en campagne elles produisent du charbon produisant de l'électricité",
 "impot" : "-5 K",
 "consommation" : "+20 W",
 "pose": "30 K",
   "evolution" : "Avoir 20K d'argent"}



CLICK_MINE2 = {
"fond": (0,180,190),
 "titre" : "Mine améliorer",
 "resume" : "Les mines se placent à l'extérieur de la ville elles produisent du charbon produisant de l'électricité",
 "impot" : "-7 K",
 "consommation" : "+40 W",
 "pose": "30 K",
   "evolution" : "Avoir 40K d'argent"}



CLICK_MINE3 = {
"fond": (0,180,190),
 "titre" : "Mine améliorer +",
 "resume" : "Les mines se placent à l'extérieur de la ville elles produisent du charbon produisant de l'électricité",
 "impot" : "-10 K",
 "consommation" : "+80 W",
 "pose": "30 K",
}



CLICK_MAIRIE = {
"fond": (0,180,190),
 "titre" : "Mairie",
 "resume" : "Accédez à des informations sur votre ville, doit se placer au centre ville",
   "impot" : "-3 K",
  "consommation" : "-7 W",
  "pose": "15 K"
 }



CLICK_SHERIF = {
"fond": (0,180,190),
 "titre" : "Sherif",
 "resume" : "Empeche les voleurs de braquer votre banque, se place au centre ville",
   "impot" : "- 20K",
  "consommation" : "-5 W",
  "pose": "20 K"
 }



CLICK_RESERVE = {
"fond": (0,180,190),
 "titre" : "Réserve",
 "resume" : "Un batiment tout frait payer par l'état pour stocker vos objets, ce place au centre ville",
   "impot" : "0 K",
  "consommation" : "0 W",
  "pose": "0 K"
 }


CLICK_MAGAZIN = {
"fond": (0,180,190),
 "titre" : "Magazin",
 "resume" : "Un batiment tout frais payer par l'état pour vendre vos céréale à 0.1K l'unité, ce place au centre ville",
   "impot" : "0 K",
  "consommation" : "0 W",
  "pose": "0 K"
 }



CLICK_BANQUE = {
"fond": (0,180,190),
 "titre" : "Banque",
 "resume" : "Placez une banque dans votre ville pour stocker de l'argent doit se placer au centre ville",
 "coffre" : "1000 K",
 "impot" : "-10 K",
 "consommation" : "-5 W",
 "pose": "50 K",
 "evolution" : "Avoir 500K d'argent"}



CLICK_BANQUE2 = {
"fond": (0,180,190),
 "titre" : "Banque",
 "resume" : "Placez une banque dans votre ville pour stocker de l'argent doit se placer au centre ville",
 "coffre" : "10000 K",
 "impot" : "-100 K",
 "consommation" : "-50 W",
 "pose": "50 K",
 "evolution" : "Avoir 5000K d'argent"}

CLICK_BANQUE3 = {
"fond": (0,180,190),
 "titre" : "Banque",
 "resume" : "Placez une banque dans votre ville pour stocker de l'argent doit se placer au centre ville",
 "coffre" : "100000 K",
 "impot" : "-1000 K",
 "consommation" : "-100 W",
 "pose": "50 K"}



CLICK_ROUTE = {
 "fond" : (255, 128, 192),
 "titre": "Route",
 "resume": "Crée des routes",
 "pose": "0.5 K"}



CLICK_RAIL = {
 "fond" : (255, 128, 192),
 "titre": "Rail",
 "resume": "Créer des rails",
 "pose": "0.5 K"}



CLICK_EAU = {
 "fond" : (255,128, 64),
 "titre": "Eau",
 "resume": "Place un point d'eau",
 "pose": "1 K"}



CLICK_CASTUS = {
  "fond" : (255,128, 64),
 "titre": "Cactus",
 "resume": "Place un cactus",
 "pose": "1 K"}


CLICK_CHAMP = {
  "fond" : (255, 128, 192),
 "titre": "Champ",
 "resume": "Place un champ, doit se poser en dehors de la ville",
 "pose": "1 K"}



"""Les interfaces correspondant à nos objets posable"""

"""Les batiments de niveau 3"""

"""La maison 3"""
maison3 = batiment(pygame.image.load('textures/maison3.png').convert_alpha(), taille=3, elec=-5, click = CLICK_MAISON3, habithant=10, impot=10)

"""La mine3"""
mine3 = batiment(pygame.image.load('textures/mine3.png').convert_alpha(), taille=10, elec=80,  lieu="quartier", click = CLICK_MINE3, impot=-10, pose=30)

"""La banque3"""

banque3 = batiment(pygame.image.load('textures/banque3.png').convert_alpha(), taille=7, elec=-100, lieu="centre", click= CLICK_BANQUE2, impot=-1000, pose = 40, unique="have_bank", argent_max = 99900)





"""Les batiments de niveau 2"""

"""La maison2"""
maison2 = batiment(pygame.image.load('textures/maison2.png').convert_alpha(), taille=3, elec=-2, click = CLICK_MAISON2, habithant=4, impot=3, evolue = maison3, cd_evolue = "score['argent'] >= 30 and score['energie'] > 0 and score['habithant'] > 99", cout_evolue = 30)

"""La mine2"""
mine2 = batiment(pygame.image.load('textures/mine2.png').convert_alpha(), taille=10, elec=40,  lieu="quartier", click = CLICK_MINE2, impot=-7, pose=30, evolue = mine3, cd_evolue = "score['argent'] >= 40", cout_evolue = 40)

"""La banque2"""
banque2 = batiment(pygame.image.load('textures/banque2.png').convert_alpha(), taille=7, elec=-50, lieu="centre", click= CLICK_BANQUE2, impot=-100, pose = 40, unique="have_bank", argent_max = 9900, evolue = banque3, cd_evolue = "score['argent'] >= 5000 ", cout_evolue = 5000)




"""Les batiments de niveau 1"""


"""La garre"""
garre = batiment(pygame.image.load('textures/garre.png').convert_alpha(), taille=15, elec= 0, click = CLICK_GARRE, tutoriel = "Gare", lieu="centre", unique="have_garre")

"""La maison"""
maison = batiment(pygame.image.load('textures/maison.png').convert_alpha(), taille=3, elec= 0, click = CLICK_MAISON, habithant=1, impot=1, pose=5, evolue = maison2, cd_evolue = "score['argent'] >= 7 and score['energie'] > 0 and score['habithant'] > 9", cout_evolue = 7, tutoriel = "Maison")

"""La mine"""
mine = batiment(pygame.image.load('textures/mine.png').convert_alpha(), taille=10, elec=20,  lieu="quartier", click = CLICK_MINE, impot=-3, pose=30, evolue = mine2, cd_evolue = "score['argent'] >= 20", cout_evolue = 20, tutoriel = "Mine")

"""La banque"""
banque = batiment(pygame.image.load('textures/banque.png').convert_alpha(), taille=7, elec=-5, lieu="centre", click= CLICK_BANQUE, impot=-10, pose = 40, unique="have_bank", argent_max = 900, evolue = banque2, cd_evolue = "score['argent'] >= 500 ", cout_evolue = 500, tutoriel = "Banque")

"""La mairie"""
mairie = batiment(pygame.image.load('textures/mairie.png').convert_alpha(), taille=10, elec=-7, lieu="centre", click= CLICK_MAIRIE, impot=-3, pose = 15, unique="have_hotel", tutoriel = "Mairie")


"""Le sherif"""
sherif = batiment(pygame.image.load('textures/sherif.png').convert_alpha(), taille=5, elec=-5, lieu="centre", click= CLICK_SHERIF, impot=-20, pose = 20, unique="have_sherif", tutoriel = "Sherif")


"""La réserve"""
reserve = batiment(pygame.image.load('textures/reserve.png').convert_alpha(), taille=8, elec=0, lieu="centre", click= CLICK_RESERVE, impot=0, pose = 0, unique="have_reserve", tutoriel="Reserve")


"""Notre magazin"""
magazin = batiment(pygame.image.load('textures/magazin.png').convert_alpha(), taille=4, click=CLICK_MAGAZIN, pose= 0, unique="have_magazin", lieu="centre", special = True, tutoriel = "Magazin")


""" Nos routes"""
route = batiment(pygame.image.load('textures/route_hauteur.png').convert_alpha(), taille=1, click=CLICK_ROUTE, pose= 0.5)


""" Notre eau"""
eau = batiment(pygame.image.load('textures/eau.png').convert_alpha(), taille=1, click=CLICK_EAU, pose= 1)


""" Notre cactus"""
cactus = batiment(pygame.image.load('textures/cactus.png').convert_alpha(), taille=1, click=CLICK_CASTUS, pose= 1)


"""Notre champ"""
champ = batiment(pygame.image.load('textures/champ.png').convert_alpha(), taille=1, click=CLICK_CHAMP, pose= 1, recup= "True", cereale = 1, temps = 10, lieu="quartier",     tutoriel="Champ")


"""L'interface pour le choix d'un de nos objets"""

#Comme c'est censé être à ne pas supprimer si j'y comprendrai rien
#memo_choix = [CLICK_BATIMENT, CLICK_UTILITAIRE, CLICK_DECORATION]
#choix = memo_choix
#choix_batiment = [CLICK_BATIMENT_DEBUT, CLICK_BATIMENT_AVANCER]
#choix_batiment_debut = [reserve, magazin]
#choix_batiment_avancer = [maison, mine, mairie, sherif, banque]
#choix_utilitaire = [route, champ]
#choix_decoration = [eau, cactus]

memo_choix = [CLICK_BATIMENT]
choix_batiment = [CLICK_BATIMENT_DEBUT]
choix_batiment_debut = [reserve]
choix_batiment_avancer = []
choix_utilitaire = []
choix_decoration = []



mapdup = map[:]


"""Les clefs seront un couple map_y, map_x , y, x"""
dico_temps = {}


"""Initialisation d'une zone vide"""
for i in range(0, len(mapdup)) :
    for ii in range(0, len(mapdup)) :
        if mapdup[i][ii] == "x" or mapdup[i][ii] == "o" :
            map[i][ii] = [[vide for i in range(0, 75)] for i in range(0, 75)]

map_x = 1
map_y = 1
map_max = len(map)



"""Initialisation avant la fin"""
construction = None
zone_charger = map[map_y][map_x]


























"""Notre jeu"""

temps_debug = time.time()
moyenne_debug = []

fin = False
while not fin:
    debug += 1
    nbr_iteration_20 +=1

    score["argent"] += 1












    """Gestion des évenement"""
    for event in pygame.event.get():



        """Pour quittez"""
        if event.type == pygame.QUIT:
            fin = True

        elif event.type == pygame.MOUSEBUTTONDOWN :
            """Pour cliquez sur la souris"""
            if event.button == 1 :
                click = 1
            if event.button == 3 :
                click = 2

        elif event.type == pygame.MOUSEBUTTONUP :
            click = 0

















    """Controle au clavier et à la souris """


    """Clavier"""



    """ Système pour ce déplacer sur la carte"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        if map_x != 0 :
            map_x -= 1
            time.sleep(0.125)
            Ecran.fill((0,0,0))
            zone_charger = map[map_y][map_x]



    elif keys[pygame.K_d]:
        if map_x < map_max - 1 :
            map_x += 1
            time.sleep(0.125)
            Ecran.fill((0,0,0))
            zone_charger = map[map_y][map_x]


    elif keys[pygame.K_w]:
        if map_y < map_max - 1 :
            map_y += 1
            time.sleep(0.125)
            Ecran.fill((0,0,0))
            zone_charger = map[map_y][map_x]


    elif keys[pygame.K_s]:
        if map_y != 0 :
            map_y -= 1
            time.sleep(0.125)
            Ecran.fill((0,0,0))
            zone_charger = map[map_y][map_x]










    elif keys[pygame.K_TAB] :
        """Choix d'un batiment"""
        choix = memo_choix
        ancien = construction
        construction = None
        index = 0



        while construction == None or construction == False or construction == "redo" or construction == "menue" :

            if isinstance(choix[index], batiment) :
                construction = cree_interface(choix[index].click, choix[index])
                time.sleep(0.125)



            else :
                construction = cree_interface(choix[index], vide)

                if construction == vide :
                    construction = "redo"




                    if choix[index] == CLICK_BATIMENT :
                        choix = choix_batiment

                    elif choix[index] == CLICK_BATIMENT_DEBUT :
                        choix = choix_batiment_debut

                    elif choix[index] == CLICK_BATIMENT_AVANCER :
                        choix = choix_batiment_avancer




                    elif choix[index] == CLICK_UTILITAIRE :
                        choix = choix_utilitaire

                    elif choix[index] == CLICK_DECORATION :
                        choix = choix_decoration

                    index = 0





            if construction == False :
                index += 1
                if index >= len(choix) :
                    index = 0




            elif construction == None :
                index -= 1
                if index < 0 :
                    index = len(choix) - 1



            #"""Pouvoir revenir en arrière sur le menue"""
            elif construction == "menue" :


                if choix == memo_choix :
                    construction = ancien



                else :
                    choix = memo_choix
                    index = 0

















    """souris"""









    """Système de gestion de la souris"""

    position_souris = list(pygame.mouse.get_pos())
    position_souris[0] = position_souris[0] // 10 * 10
    position_souris[1] = position_souris[1] // 10 * 10




    if click >= 1 :
        y_souris = int(position_souris[1] / 10)
        x_souris = int(position_souris[0] / 10)













        """Système pour placer des objets"""
        if click == 1 and construction != None  :
            if score["argent"] >= construction.pose or construction.pose == 0 :
                zone_charger = map[map_y][map_x]



                #vérification que l'on puisse placer l'objet
                if construction.taille == 1 :
                    if x_souris <= 74 and construction.lieu in endroit:
                        if zone_charger[y_souris][x_souris] != hand :
                            if zone_charger[y_souris][x_souris] != construction :
                                map[map_y][map_x][y_souris][x_souris] = construction

                                if map[map_y][map_x][y_souris][x_souris].temps != None :
                                    dico_temps[(map_y, map_x, y_souris, x_souris)] = time.time()



                                score["argent"] -= construction.pose
                                tuto[construction.tutoriel] = True






                #système pour des objets de x dimension
                elif construction.taille > 1 and construction.lieu in endroit :

                    if construction.unique == "osef" or score[construction.unique] == False :

                        possible = True
                        for i in range(0,  construction.taille) :
                            for ii in range(0, construction.taille) :
                                try :
                                    if zone_charger[y_souris + ii][x_souris + i] != vide :
                                        possible = False

                                except IndexError :
                                    possible = False

                        if possible == True :
                            for i in range(0, construction.taille) :
                                for ii in range(0, construction.taille) :
                                    map[map_y][map_x][y_souris + ii ][x_souris + i] = hand





                            dico_map[map_y][map_x].append( {(x_souris * 10, y_souris * 10) : construction} )
                            if construction.unique != "osef" :
                                score[construction.unique] = True
                            score["energie"] += construction.elec
                            score["habithant"] += construction.habithant
                            score["impot"] += construction.impot
                            score["argent"] -= construction.pose
                            tuto[construction.tutoriel] = True
                            click = 0

                            if construction.argent_max != None :
                                score["argent_max"] += construction.argent_max





























    """Moteur graphique"""
    x = 0
    y = 0



    """en premier la liste qui compose nos map (batiment simple)"""
    if nbr_iteration_20 > 20 :
        Ecran.fill((255, 127, 39))

        for i in zone_charger :

            for ii in i :



                if ii != hand or ii != vide :


                    """Controle des textures de notre route"""





                    """Pour les champs"""
                    if ii == champ :
                        if time.time() - dico_temps[(map_y, map_x, int( y // 10), int(x // 10))] > ii.temps :
                            ii.texture =  champ_1
                        else :
                            ii.texture = champ_0













                    #"""Pour les routes"""
                    elif ii == route :
                        dico_check = {"haut" : False, "cote" : False}


                        try :
                            if y - 10 >= 0 :
                                if zone_charger[int((y - 10) / 10)][int(x / 10)] == route :
                                    dico_check["haut"] = True
                        except : pass

                        if dico_check["haut"] == False :
                            try :
                                if zone_charger[int((y + 10) / 10)][int(x / 10)] == route :
                                    dico_check["haut"] = True
                            except : pass


                        try :
                            if x - 10 >= 0 :
                                if zone_charger[int(y / 10)][int((x - 10) / 10)] == route :
                                    dico_check["cote"] = True
                        except : pass


                        if dico_check["cote"] == False :
                            try :
                                if zone_charger[int(y / 10)][int((x + 10) / 10)] == route :
                                    dico_check["cote"] = True
                            except : pass

                        if (dico_check["haut"] == True and dico_check["cote"] == True) or (dico_check["haut"] == False and dico_check["cote"] == False):
                            ii.texture =  route_rond
                        elif dico_check["haut"] == True :
                            ii.texture = route_hauteur
                        elif dico_check["cote"] == True :
                            ii.texture = route_cote









                ii.affiche(x, y)


                x += 10



            x = 0
            y += 10









    """en second les batiments complexe"""
    for i in dico_map[map_y][map_x] :
        for ii in i.keys() :
            x = ii[0]
            y = ii[1]

            if map[map_y][map_x][int(y // 10)][int(x // 10)] == hand :
                i[ii].affiche(x, y)



            else :
                score["energie"] -= i[ii].elec
                score["habithant"] -= i[ii].habithant
                score["impot"] -= i[ii].impot
                if i[ii].unique != "osef" :
                    score[i[ii].unique] = False

                    if construction.argent_max != None :
                        score["argent_max"] -= construction.argent_max


                del i[ii]
                break


















            """savoir si on sélectionne un gros batiment ou pas"""
            y_souris = int(position_souris[1] / 10)
            x_souris = int(position_souris[0] / 10)

            resultat = verifie (i[ii], x, x_souris, y, y_souris)


            if resultat :
                objet_selectionner = i[ii]


                tuple_souris = [
                (x // 10, x // 10 + i[ii].taille),
                (y // 10, y // 10 + i[ii].taille)
                ]


                """Les interraction qui se font avec la barre espace"""
                if keys[pygame.K_SPACE] :

                    """Les batiments speciaux"""
                    if i[ii].special != None :
                        if i[ii] == magazin :
                            if inventaire["cereale"] > 0 :
                                score["argent"] += inventaire["cereale"] * 0.1
                                inventaire["cereale"] = 0

                                if nbr_tuto == 5 :
                                    nbr_tuto += 1
                                    choix_batiment.append(CLICK_BATIMENT_AVANCER)
                                    choix_batiment_avancer.append(maison)


                    #"""Le système d'évolution"""
                    elif i[ii].evolue != None and peut_evoluer == True :



                        score["argent"] -= i[ii].cout_evolue
                        score["energie"] -= i[ii].elec
                        score["habithant"] -= i[ii].habithant
                        score["impot"] -= i[ii].impot

                        if nbr_tuto == 9 :
                            nbr_tuto += 1
                            choix_batiment_avancer.append(sherif)


                        if construction.argent_max != None :
                            score["argent_max"] -= construction.argent_max





                        test = i[ii]
                        while test == i[ii] :
                            test = cree_interface(CLICK_FELICITATION, i[ii])

                        i[ii] = i[ii].evolue






                        score["energie"] += i[ii].elec
                        score["habithant"] += i[ii].habithant
                        score["impot"] += i[ii].impot

                        if construction.argent_max != None :
                            score["argent_max"] += construction.argent_max

















        """Système pour actualiser les informations de l'objet sélectionner"""


        """Pour la mairie"""
        if objet_selectionner == mairie :
            if score["energie"] > 0 :
                try :
                    del CLICK_MAIRIE["erreur"]
                except : pass
                CLICK_MAIRIE["bilan_argent"] = "Compte bancaire de la ville :" + str(round(score["argent"], 3)) + "k    Taille du coffre : " + str(score["argent_max"]) + " K"
                CLICK_MAIRIE["bilan_energie"] = str(score["energie"])
                CLICK_MAIRIE["bilan_impot"] = str(score["impot"])
                CLICK_MAIRIE["bilan_habithant"] = str(score["habithant"])
            else :
                try :
                    del CLICK_MAIRIE["bilan_energie"]
                    del CLICK_MAIRIE["bilan_argent"]
                    del CLICK_MAIRIE["bilan_impot"]
                    del CLICK_MAIRIE["bilan_habithant"]
                except : pass
                CLICK_MAIRIE["erreur"] = "Sans électricité la mairie ne peut pas fonctionner"

        elif objet_selectionner == reserve :
            CLICK_RESERVE["nbr_cereale"] = inventaire["cereale"]



        if objet_selectionner == magazin :
            CLICK_MAGAZIN["bilan_argent"] = "Argent actuel :" + str(round(score["argent"], 3)) + "K"













    """Un curseur qui s'adapte à la taille des éléments"""
    if tuple_souris == None :
        objet_x = position_souris[0] // 10
        objet_y = position_souris[1] // 10

        if objet_x <= 74 :
            if zone_charger[objet_y][objet_x].recup == None :
                curseur.affiche(position_souris[0], position_souris[1])










            #"""La possibiliter de récupérer les objets au sol de 10 px par 10 px"""
            else :
                nposition_souris = list(pygame.mouse.get_pos())
                nx_souris = nposition_souris[0] // 10
                ny_souris = nposition_souris[1] // 10

                if position_souris[0] < 750 :
                    curseur4.affiche(position_souris[0], position_souris[1])


                try :
                    if time.time() - dico_temps[(map_y, map_x, ny_souris, nx_souris)] > zone_charger[objet_y][objet_x].temps :
                        if keys[pygame.K_SPACE] :


                            inventaire["cereale"] += zone_charger[objet_y][objet_x].cereale

                            """système propre à l'objet pour le faire changer"""
                            dico_temps[(map_y, map_x, ny_souris, nx_souris)] = time.time()





                    else :
                            curseur.affiche(position_souris[0], position_souris[1])
                except :
                        curseur.affiche(position_souris[0], position_souris[1])
















    else :
        x_tuple = tuple_souris[0]
        y_tuple = tuple_souris[1]



        if objet_selectionner.special != None :
            mon_curseur = curseur3



        elif objet_selectionner.evolue == None :
                mon_curseur = curseur1
                peut_evoluer = False



        elif eval(objet_selectionner.cd_evolue) == True :
            mon_curseur = curseur2
            peut_evoluer = True



        else :
            mon_curseur = curseur1
            peut_evoluer = False




        for x in range(x_tuple[0], x_tuple[1]) :
            for y in range(y_tuple[0], y_tuple[1]) :

                if zone_charger[y][x] == hand :
                    mon_curseur.affiche(x * 10, y * 10)


                """Mettre des bandes noire pour faire jolie"""
                if y == y_tuple[0] :
                    bande_x.affiche(x*10, y* 10)

                elif y == y_tuple[1] - 1 :
                    bande_x.affiche(x*10, y * 10 + 9)


                if x == x_tuple[0] :
                    bande_y.affiche(x*10, y*10)

                elif x == x_tuple[1] - 1 :
                    bande_y.affiche(x*10+9, y*10)














    """Supprimez des éléments sur la carte"""






    """Système pour enlever des objets qui font une case sur une case"""
    if click == 2 :
        zone_charger = map[map_y][map_x]

        if tuple_souris == None :
            try :
                map[map_y][map_x][y_souris][x_souris] = vide
                del dico_temps[(map_y, map_x, y_souris, x_souris)]
            except : pass







            """Système pour enlever des objets qui font plusieurs case sur plusieurs cases"""
        else :
            for x in range(x_tuple[0], x_tuple[1]) :
                for y in range(y_tuple[0], y_tuple[1]) :
                    map[map_y][map_x][y][x] = vide
            click = 0











    """Système pour sélectionner des batiments (si on appuie sur espace on sélectionne ce batiment)"""
    if click == 1 and tuple_souris != None and objet_selectionner != None :
        memo_construction = construction
        construction = cree_interface(objet_selectionner.click, objet_selectionner, verifie=True)
        if construction == None or construction == False or construction == "redo" or construction == "menue" :
            construction = memo_construction
        del memo_construction
        click = 0












    """Système pour voir l'évolution d'un batiment"""
    if tuple_souris != None and objet_selectionner.evolue != None and keys[pygame.K_BACKSPACE] :
        cree_interface(objet_selectionner.evolue.click, objet_selectionner, verifie=True)










    """système pour savoir si on est dans un quartier ou au centre ville"""
    if la_map[map_y][map_x] == "o" :
        endroit[1] = "centre"


    elif la_map[map_y][map_x] == "x" :
        endroit[1] = "quartier"










    """Système d'impot qui s'execute toute les 60 secondes pour ajoutez à argent la somme des impots"""
    now = time.time()

    if now - debut > 60 :
        if score["energie"] >= 0 and score["impot"] >= 0:
            score["argent"] += score["impot"]
        elif score["impot"] < 0 :
            score["argent"] += score["impot"]

        debut = time.time()
        braque.vol(score)







    """Système liez au score"""
    if score["argent"] > score["argent_max"] :
        score["argent"] = score["argent_max"]

    if score["have_reserve"] == False :
        if objet_x <= 74 :
            inventaire["cereale"] += zone_charger[objet_y][objet_x].cereale



















    if nbr_iteration_20 > 20 :



        """Notre interface a droite"""




        """Mettre le fond blanc"""
        GUI_FOND.GUI_affiche()





        """Savoir si on est au centre ville ou dans un quartier"""
        ma_police = pygame.font.SysFont('Arial', 25)
        if "centre" in endroit : texte = ma_police.render("Centre ville", True, (0, 0, 0))
        if "quartier" in endroit : texte = ma_police.render("Campagne", True, (0, 0, 0))
        Ecran.blit(texte,(760,0))






        """Les controles"""
        ma_police = pygame.font.SysFont('Arial', 25)
        texte = ma_police.render("Les controles :", True, (0, 0, 0))
        Ecran.blit(texte,(760, 620))


        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("ZQSD : Se déplacer", False, (0, 0, 0))
        Ecran.blit(texte,(790,650))


        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Tab : Choisir une construction", False, (0, 0, 0))
        Ecran.blit(texte,(790,670))

        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Espace : Utilisez l'objet", False, (0, 0, 0))
        Ecran.blit(texte,(790,690))


        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Click Gauche : Construire / Voir", False, (0, 0, 0))
        Ecran.blit(texte,(790,710))


        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Click Droit : Enlevez", False, (0, 0, 0))
        Ecran.blit(texte,(790,730))














        """Nos tutoriels"""
        ma_police = pygame.font.SysFont('Arial', 25)
        texte = ma_police.render("Tutoriel :", True, (0, 0, 0))
        Ecran.blit(texte,(760, 50))



        try :
            del texte
            del texte2
            del texte3
            del texte4
            del texte5
            del texte6
            del texte7
        except : pass
        ma_police = pygame.font.SysFont('Arial', 15)
        ma_police2 = pygame.font.SysFont('Arial', 13)


        """Nos affichages selon là ou on en est"""
        if tuto["Reserve"] == False and nbr_tuto == 1 :
            texte = ma_police.render("Placez une réserve :", True, (0, 0, 0))
            texte2 = ma_police2.render("Ouvrez le menue tab", True, (0, 0, 0))
            texte3 = ma_police2.render("Confirmez avec la barre espace", True, (0, 0, 0))
            texte4 = ma_police2.render("Placez avec click gauche", True, (0, 0, 0))
            texte5 = ma_police2.render("Permet de stocker les objets", True, (0, 0, 0))

        if tuto["Reserve"] == True and nbr_tuto == 1 :
            nbr_tuto += 1
            choix_batiment_debut.append(magazin)




        if tuto["Magazin"] == False and nbr_tuto == 2 :
            texte = ma_police.render("Placez un magazin", True, (0, 0, 0))
            texte2 = ma_police2.render("Ouvrez le menue tab", True, (0, 0, 0))
            texte3 = ma_police2.render("Confirmez avec la barre espace", True, (0, 0, 0))
            texte4 = ma_police2.render("Se déplacez avec le click", True, (0, 0, 0))
            texte5 = ma_police2.render("Placez avec click gauche", True, (0, 0, 0))
            texte6 = ma_police2.render("Permez de vendre les objets", True, (0, 0, 0))

        if tuto["Magazin"] == True and nbr_tuto == 2 :
            nbr_tuto += 1
            memo_choix.append(CLICK_UTILITAIRE)
            choix_utilitaire.append(champ)




        if tuto["Champ"] == False and nbr_tuto == 3 :
            texte = ma_police.render("Placez un champ", True, (0, 0, 0))
            texte2 = ma_police2.render("se trouve dans le menue utilitaire", True, (0, 0, 0))
            texte3 = ma_police2.render("se met en dehors de la ville", True, (0, 0, 0))
            texte4 = ma_police2.render("Permez de faire des plantations", True, (0, 0, 0))
        if tuto["Champ"] == True and nbr_tuto == 3 :
            nbr_tuto += 1




        if inventaire["cereale"] < 10 and nbr_tuto == 4 :
            texte = ma_police.render("Récoltez 10 céréale", True, (0, 0, 0))
            texte2 =  ma_police2.render("Attendre que sa pousse", True, (0, 0, 0))
            texte3 =  ma_police2.render("Appuyez sur espace pour récoltez", True, (0, 0, 0))
        if inventaire["cereale"] >= 10 and nbr_tuto == 4 :
            nbr_tuto += 1


        if nbr_tuto == 5 :
            texte = ma_police.render("Vendez vos céréales au magazin", True, (0, 0, 0))
            texte2 =  ma_police2.render("Donne de l'argent", True, (0, 0, 0))



        if tuto["Maison"] == False and nbr_tuto == 6 :
            texte = ma_police.render("Placez une maison", True, (0, 0, 0))
            texte2 =  ma_police2.render("Allez dans construction avancer", True, (0, 0, 0))
            texte3 =  ma_police2.render("Des gens y habithent et paie des impots""", True, (0, 0, 0))
        if tuto["Maison"] == True and nbr_tuto == 6 :
            nbr_tuto += 1
            choix_batiment_avancer.append(mine)


        if tuto["Mine"] == False and nbr_tuto == 7 :
            texte = ma_police.render("Placez une mine", True, (0, 0, 0))
            texte2 =  ma_police2.render("Allez dans construction avancer", True, (0, 0, 0))
            texte3 =  ma_police2.render("Se met en dehors de la ville", True, (0, 0, 0))
            texte4 =  ma_police2.render("Génère de l'électricité", True, (0, 0, 0))
        if tuto["Mine"] == True and nbr_tuto == 7 :
            choix_batiment_avancer.append(mairie)
            nbr_tuto += 1



        if tuto["Mairie"] == False and nbr_tuto == 8 :
            texte = ma_police.render("Placez une mairie", True, (0, 0, 0))
            texte2 =  ma_police2.render("Allez dans construction avancer", True, (0, 0, 0))
            texte3 =  ma_police2.render("Se met en ville", True, (0, 0, 0))
            texte4 =  ma_police2.render("Donne des infos sur la ville", True, (0, 0, 0))
        if tuto["Mairie"] == True and nbr_tuto == 8 :
            nbr_tuto += 1

        if nbr_tuto == 9 :
            texte = ma_police.render("Améliorez un batiment", True, (0, 0, 0))
            texte2 =  ma_police2.render("Si il est bleu appuyer sur espace", True, (0, 0, 0))
            texte3 =  ma_police2.render("Les conditions doivent être valide", True, (0, 0, 0))
            texte4 =  ma_police2.render("Augmente la rentabilité du batiment", True, (0, 0, 0))



        if tuto["Sherif"] == False and nbr_tuto == 10 :
            texte = ma_police.render("Placez le sherif", True, (0, 0, 0))
            texte2 =  ma_police2.render("Allez dans construction avancer", True, (0, 0, 0))
            texte3 =  ma_police2.render("Se met en ville", True, (0, 0, 0))
            texte4 =  ma_police2.render("Evite de se faire voler", True, (0, 0, 0))

        if tuto["Sherif"] == True and nbr_tuto == 10 :
            nbr_tuto += 1
            choix_batiment_avancer.append(banque)

        if tuto["Banque"] == False and nbr_tuto == 11 :
            texte = ma_police.render("Placez une banque", True, (0, 0, 0))
            texte2 =  ma_police2.render("Allez dans construction avancer", True, (0, 0, 0))
            texte3 =  ma_police2.render("Se met en ville", True, (0, 0, 0))
            texte4 =  ma_police2.render("Permet de stocker plus d'argent", True, (0, 0, 0))
        if tuto["Banque"] == True and nbr_tuto == 11 :
            nbr_tuto += 1
            choix_utilitaire.append(route)
            memo_choix.append(CLICK_DECORATION)
            choix_decoration.append(cactus)
            choix_decoration.append(eau)

        if nbr_tuto == 12 :
            texte = ma_police.render("Jouez", True, (0, 0, 0))













        try :
            Ecran.blit(texte,(770, 80))
            Ecran.blit(texte2,(780, 100))
            Ecran.blit(texte3,(780, 120))
            Ecran.blit(texte4,(780, 140))
            Ecran.blit(texte5,(780, 160))
            Ecran.blit(texte6,(780, 180))
            Ecran.blit(texte6,(780, 200))
        except : pass





















    """Tout ce qui enlève les bug et optimise"""

    tuple_souris = None
    pygame.display.update()

    if time.time() - temps_debug > 1 :
        moyenne_debug.append(debug)
        somme = 0
        for i in moyenne_debug :
            somme += i
        somme /= len(moyenne_debug)
        #print(int(somme))
        debug = 0
        temps_debug = time.time()



    if nbr_iteration_20 > 20 :
        nbr_iteration_20 = 0




















    score["argent"] = 100
pygame.quit() #On quitte pygame