"""Système pour créer des interfaces"""



def cree_interface(info, batiment_selectionner, verifie=False) :

    """L'initialisation"""
    import pygame
    pygame.font.init() #indispensable pour créez des textes avec pygames
    Ecran = pygame.display.set_mode((1000,750))
    pygame.display.set_caption("FarWest city")
    click = 0
    bande_jaune = pygame.image.load('textures/bande_jaune.png').convert_alpha()
    GUI_Fond = pygame.image.load('textures/GUI_Fond.png').convert_alpha()
    cree = True

    """Création de la boucle"""
    fin = False
    while not fin:

        """Taches commune"""
        """Gestion des évenement"""
        for event in pygame.event.get():



            """Pour quittez"""
            if event.type == pygame.QUIT:
                fin = True
                return None

            """Pour cliquez sur la souris"""
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    fin = True
                    return None
                if event.button == 3 :
                    fin = True
                    return False

            """Pour le relachement de la souris"""
            if event.type == pygame.MOUSEBUTTONUP :
                click = 0



        """Gestions des évènement du clavier"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] :
            return "menue"




        if keys[pygame.K_SPACE] :
            return batiment_selectionner

        pygame.display.update()













        if cree == True :



            """Pour l'information sur le fond"""
            try :
                if info["fond"] != None :
                    Ecran.fill(info["fond"])
            except : break



            """Pour l'information sur le titre"""
            try :
                if info["titre"] != None :

                    Ecran.blit(bande_jaune, (0, 25))
                    ma_police = pygame.font.SysFont('Arial', 20)
                    texte = ma_police.render(str(info["titre"]), True, (0, 0, 0))
                    Ecran.blit(texte,(0,0))


            except : break



            """Pour l'information sur le resume"""
            try :
                if info["resume"] != None :

                    ma_police = pygame.font.SysFont('Arial', 15)
                    texte = ma_police.render("Resume : " + str(info["resume"]), False, (0, 0, 0))
                    Ecran.blit(texte,(10,50))

            except : pass







            """Pour l'information sur la consommation"""
            try :
                if info["consommation"] != None :
                    ma_police = pygame.font.SysFont('Arial', 25)
                    texte = ma_police.render("Consommation : " + str(info["consommation"]), True, (180, 0, 0))
                    Ecran.blit(texte,(500,710))


            except : pass



            """Pour l'information sur l'impot"""
            try :
                if info["impot"] != None :
                    ma_police = pygame.font.SysFont('Arial', 25)
                    texte = ma_police.render("Impot: " + str(info["impot"]), True, (180, 0, 0))
                    Ecran.blit(texte,(20,710))


            except : pass











            """Requiere que l'utilisateur pose le batiment"""
            if verifie == True :


                """Pour l'information sur le nombre de céréale"""
                try :
                    if info["nbr_cereale"] != None :
                        ma_police = pygame.font.SysFont('Arial', 13)
                        texte = ma_police.render("Nombre de céréale :  " + str(info["nbr_cereale"]) + " T", False, (0, 0, 0))
                        Ecran.blit(texte,(40,90))
                except : pass



                """Pour l'information sur le bilan d'argent"""
                try :
                    if info["bilan_argent"] != None :
                        ma_police = pygame.font.SysFont('Arial', 13)
                        texte = ma_police.render(str(info["bilan_argent"]), False, (0, 0, 0))
                        Ecran.blit(texte,(40,90))
                except : pass


                """Pour l'information sur le bilan d'énergie"""
                try :
                    if info["bilan_energie"] != None :
                        ma_police = pygame.font.SysFont('Arial', 13)
                        texte = ma_police.render("Bilan energetique de la ville : " + str(info["bilan_energie"]), False, (0, 0, 0))
                        Ecran.blit(texte,(40,110))
                except : pass



                """Pour l'information sur le bilan d'impot"""
                try :
                    if info["bilan_argent"] != None :
                        ma_police = pygame.font.SysFont('Arial', 13)
                        texte = ma_police.render("Revenue (Impot - Perte) : " + str(info["bilan_impot"]) + " K", False, (0, 0, 0))
                        Ecran.blit(texte,(40,130))
                except : pass



                """Pour l'information sur le bilan d'habithant"""
                try :
                    if info["bilan_habithant"] != None :
                        ma_police = pygame.font.SysFont('Arial', 13)
                        texte = ma_police.render("Nombre d'habithant : " + str(info["bilan_habithant"]) , False, (0, 0, 0))
                        Ecran.blit(texte,(40,150))
                except : pass



                """Pour l'information sur la capacité de stockage"""
                try :
                    if info["coffre"] != None :
                        ma_police = pygame.font.SysFont('Arial', 18)
                        texte = ma_police.render("Taille du coffre : " + str(info["coffre"]) , False, (180, 0, 0))
                        Ecran.blit(texte,(40,80))
                except : pass



                """Pour l'information sur l'erreur"""
                try :
                    if info["erreur"] != None :
                        ma_police = pygame.font.SysFont('Arial', 20)
                        texte = ma_police.render(str(info["erreur"]) , False, (180, 0, 0))
                        Ecran.blit(texte,(40,90))
                except : pass



                """Pour l'information sur le nombre d'habithant"""
                try :
                    if info["nbr_habithant"] != None :
                        ma_police = pygame.font.SysFont('Arial', 20)
                        texte = ma_police.render("Nombre d'habithant : " + str(info["nbr_habithant"]) , False, (0, 0, 0))
                        Ecran.blit(texte,(40,90))
                except : pass


                """Pour l'information sur l'évolution"""
                try :
                    if info["evolution"] != None :
                        ma_police = pygame.font.SysFont('Arial', 20)
                        texte = ma_police.render("Condition d'evolution : " + str(info["evolution"]) , False, (0, 0, 0))
                        Ecran.blit(texte,(5,680))
                except : pass


            else :
                """Pour l'information sur le cout de la pose"""
                try :
                    if info["pose"] != None :

                        Ecran.blit(bande_jaune, (0, 25))

                        if info["pose"] != "0" :
                            ma_police = pygame.font.SysFont('Arial', 20)
                            texte = ma_police.render("Coute a la pose : " + str(info["pose"]), True, (180, 0, 0))
                            Ecran.blit(texte,(500,0))

                except : break




        """L'explication"""
        Ecran.blit(GUI_Fond,(750,0))



        ma_police = pygame.font.SysFont('Arial', 25)
        texte = ma_police.render("Comment sa marche ?", True, (0, 0, 0))
        Ecran.blit(texte,(760,0))


        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Espace : Sélectionnez l'objet", False, (0, 0, 0))
        Ecran.blit(texte,(780,50))

        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Click : Changez d'objet", False, (0, 0, 0))
        Ecran.blit(texte,(780,80))



        ma_police = pygame.font.SysFont('Arial', 15)
        texte = ma_police.render("Echap : Retour en arrière", False, (0, 0, 0))
        Ecran.blit(texte,(780,110))




        cree = False












        pygame.display.update()