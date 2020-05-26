import pygame

#Images :
icon = pygame.image.load("assets/icon.png")
bouton_play = pygame.image.load("assets/bouton_play.png")
bouton_play = pygame.transform.scale(bouton_play, (700, 500))
bouton_option = pygame.image.load("assets/bouton_option.png")
bouton_option = pygame.transform.scale(bouton_option, (700, 500))
bouton_exit = pygame.image.load("assets/bouton_exit.png")
bouton_exit = pygame.transform.scale(bouton_exit, (700, 500))
fond_ecran = pygame.image.load("assets/menu.png")
son = pygame.image.load("assets/son.png")
son = pygame.transform.scale(son, (150, 150))
pas_son = pygame.image.load("assets/pas_son.png")
pas_son = pygame.transform.scale(pas_son, (150, 150))
fond_ecran_option = pygame.image.load("assets/menu_option.png")
fond_ecran_option = pygame.transform.scale(fond_ecran_option, (1600, 900))
fond_ecran_commands = pygame.image.load("assets/menu_commands.png")
bouton_retour_menu = pygame.image.load("assets/bouton_retour.png")
bouton_retour_menu = pygame.transform.scale(bouton_retour_menu, (500, 300))
bouton_commands = pygame.image.load("assets/commands.png")
bouton_commands = pygame.transform.scale(bouton_commands, (300, 300))
bouton_commands2 = pygame.image.load("assets/commands2.png")
bouton_commands2 = pygame.transform.scale(bouton_commands2, (300, 300))
bouton_retour_option = pygame.image.load("assets/bouton_retour.png")
bouton_retour_option = pygame.transform.scale(bouton_retour_option, (500, 300))
bulle = pygame.image.load("assets/bulle.png")
bulle = pygame.transform.scale(bulle, (300, 300))
bouton_help = pygame.image.load("assets/bouton_help.png")
bouton_help = pygame.transform.scale(bouton_help, (200, 200))
rond_credits = pygame.image.load("assets/rond_credits.png")
rond_credits = pygame.transform.scale(rond_credits, (700, 700))
fond_ecran_help = pygame.image.load("assets/menu_help.jpg")
fond_ecran_help = pygame.transform.scale(fond_ecran_help, (1600, 900))
bouton_retour_help_option = pygame.image.load("assets/bouton_retour.png")
bouton_retour_help_option = pygame.transform.scale(bouton_retour_help_option, (500, 300))
fond_ecran_niveau = pygame.image.load("assets/menu_niveau.png")
fond_ecran_niveau = pygame.transform.scale(fond_ecran_niveau, (1600, 900))

fin_jeux = pygame.image.load("assets/fin_jeux.png")
fin_jeux = pygame.transform.scale(fin_jeux, (1100, 1100))
menu_fin_jeux = pygame.image.load("assets/menu_fin_jeux.jpg")
menu_fin_jeux = pygame.transform.scale(menu_fin_jeux, (1600, 900))

bouton_retour_menu_fin = pygame.image.load("assets/bouton_retour_menu.png")
dimension_bouton_retour_menu_width = bouton_retour_menu_fin.get_width()
dimension_bouton_retour_menu_height = bouton_retour_menu_fin.get_height()
bouton_retour_menu_fin = pygame.transform.scale(bouton_retour_menu_fin, (300, 120))

bouton_retry = pygame.image.load("assets/bouton_retry.png")
bouton_retry = pygame.transform.scale(bouton_retry, (100, 100))

bouton_menu = pygame.image.load("assets/bouton_menu.png")
bouton_menu = pygame.transform.scale(bouton_menu, (150, 150))

bouton_niveau_suivant = pygame.image.load("assets/bouton_niveau_suivant.png")
bouton_niveau_suivant = pygame.transform.scale(bouton_niveau_suivant, (150, 150))

#Niveau :
bouton_niveau1 = pygame.image.load("assets/bouton_niveau.png")
bouton_niveau1 = pygame.transform.scale(bouton_niveau1, (350, 150))
bouton2_niveau1 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau1 = pygame.transform.scale(bouton2_niveau1, (350, 150))

bouton_niveau2 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau2 = pygame.transform.scale(bouton_niveau2, (350, 150))
bouton2_niveau2 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau2 = pygame.transform.scale(bouton2_niveau2, (350, 150))

bouton_niveau3 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau3 = pygame.transform.scale(bouton_niveau3, (350, 150))
bouton2_niveau3 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau3 = pygame.transform.scale(bouton2_niveau3, (350, 150))

bouton_niveau4 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau4 = pygame.transform.scale(bouton_niveau4, (350, 150))
bouton2_niveau4 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau4 = pygame.transform.scale(bouton2_niveau4, (350, 150))

bouton_niveau5 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau5 = pygame.transform.scale(bouton_niveau5, (350, 150))
bouton2_niveau5 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau5 = pygame.transform.scale(bouton2_niveau5, (350, 150))

bouton_niveau6 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau6 = pygame.transform.scale(bouton_niveau6, (350, 150))
bouton2_niveau6 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau6 = pygame.transform.scale(bouton2_niveau6, (350, 150))

bouton_niveau7 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau7 = pygame.transform.scale(bouton_niveau7, (350, 150))
bouton2_niveau7 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau7 = pygame.transform.scale(bouton2_niveau7, (350, 150))

bouton_niveau8 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau8 = pygame.transform.scale(bouton_niveau8, (350, 150))
bouton2_niveau8 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau8 = pygame.transform.scale(bouton2_niveau8, (350, 150))

bouton_niveau9 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau9 = pygame.transform.scale(bouton_niveau9, (350, 150))
bouton2_niveau9 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau9 = pygame.transform.scale(bouton2_niveau9, (350, 150))

bouton_niveau10 = pygame.image.load("assets/bouton_niveau_off.png")
bouton_niveau10 = pygame.transform.scale(bouton_niveau10, (350, 150))
bouton2_niveau10 = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau10 = pygame.transform.scale(bouton2_niveau10, (350, 150))

bouton_infinity = pygame.image.load("assets/bouton_niveau.png")
bouton_infinity = pygame.transform.scale(bouton_infinity, (400, 200))
bouton2_niveau_infi = pygame.image.load("assets/bouton_niveau2.png")
bouton2_niveau_infi = pygame.transform.scale(bouton2_niveau_infi, (400, 200))

#Commands clavier :
commands_fleche = pygame.image.load("commands/fleche.png")
commands_fleche = pygame.transform.scale(commands_fleche, (200, 129))

commands_zqsd = pygame.image.load("commands/zqsd.png")
commands_zqsd = pygame.transform.scale(commands_zqsd, (200, 129))


commands_wasd = pygame.image.load("commands/wasd.png")
commands_wasd = pygame.transform.scale(commands_wasd, (200, 129))