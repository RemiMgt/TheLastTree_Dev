#Impotations :
import pygame
from pygame.locals import *
from random import *

from image import *
from game import Game
import sys

pygame.init()

game = Game()

#Couleurs :
white = (255, 255, 255)
red = (255, 0, 0)
noir = (0, 0, 0)
marron = (98, 55, 26)
vert_titre = (12, 50, 2)

#Variables :
L = 1600
H = 900
stat = "menu"
arial_font = pygame.font.SysFont("arial", 70, True, False)
arial_font_grand = pygame.font.SysFont("arial", 260, True, False)
arial_font_petit = pygame.font.SysFont("arial", 38, True, False)
arial_font_moyen = pygame.font.SysFont("arial", 60, True, False)
arial_font_moyen_moins = pygame.font.SysFont("arial", 55, True, False)
arial_font_credits = pygame.font.SysFont("arial", 25, True, False)
arial_font_petit_credits = pygame.font.SysFont("arial", 30, False, True)
arial_font_brouillon = pygame.font.SysFont("arial", 85, True, False)

#Titre jeux :
texte_titre1 = arial_font_grand.render("T", True, vert_titre)
texte_titre2 = arial_font.render("he Last Tree", True, vert_titre)

#Musiques :
musique_menu = pygame.mixer.Sound("assets/musique_menu.ogg")
#musique_menu.play()

#Création de la fenetre :
pygame.display.set_caption("The Last Tree")
fenetre = pygame.display.set_mode((L,H))
pygame.display.set_icon(icon)


#textes :
texte_play = arial_font.render("Play", True, marron)
texte_option = arial_font.render("Option", True, marron)
texte_exit = arial_font.render("Exit", True, marron)
texte_retour_menu = arial_font_petit.render("Retour", True, marron)
texte_retour_option = arial_font_petit.render("Retour", True, marron)
texte_tap = arial_font_moyen_moins.render("Tap", True, marron)
texte_to = arial_font_moyen_moins.render("To", True, marron)
texte_show = arial_font_moyen_moins.render("Show", True, marron)
texte_credits_remi = arial_font_credits.render("Creator and developer :", True, noir)
texte_credits_nom_creator = arial_font_petit_credits.render("Rémi L'AIL", True, noir)
texte_credits_nom_designer = arial_font_petit_credits.render("Damien ", True, noir)
texte_credits_damien = arial_font_credits.render("Game designer :", True, noir)
texte_credits = arial_font_brouillon.render("Credits : ", True, red)

#Rect :
rectBouton_play = bouton_play.get_rect()
rectBouton_play.x = 80
rectBouton_play.y = 10
rectBouton_option = bouton_option.get_rect()
rectBouton_option.x = -30
rectBouton_option.y = 240
rectBouton_exit = bouton_exit.get_rect()
rectBouton_exit.x = -110
rectBouton_exit.y = 450
rectTexte_play = texte_play.get_rect()
rectTexte_play.x = 340
rectTexte_play.y = 220
rectTexte_option = texte_option.get_rect()
rectTexte_option.x = 190
rectTexte_option.y = 445
rectTexte_exit = texte_exit.get_rect()
rectTexte_exit.x = 160
rectTexte_exit.y = 660
rectSon = son.get_rect()
rectSon.x = 85
rectSon.y = 100
rectPas_son = pas_son.get_rect()
rectPas_son.x = 350
rectPas_son.y = 100
rectTexte_retour_menu = texte_retour_menu.get_rect()
rectTexte_retour_menu.x = 115
rectTexte_retour_menu.y = 705
rectBouton_retour_menu = bouton_retour_menu.get_rect()
rectBouton_retour_menu.x = -64
rectBouton_retour_menu.y = 580
rectBouton_commands = bouton_commands.get_rect()
rectBouton_commands.x = 70
rectBouton_commands.y = 400
rectBouton_retour_option = bouton_retour_option.get_rect()
rectBouton_retour_option.x = -64
rectBouton_retour_option.y = 580
rectTexte_retour_option = texte_retour_option.get_rect()
rectTexte_retour_option.x = 115
rectTexte_retour_option.y = 705
rectBouton_help = bouton_help.get_rect()
rectBouton_help.x = 150
rectBouton_help.y = 265
rectTexte_tap = texte_tap.get_rect()
rectTexte_tap.x = 1198
rectTexte_tap.y = 340
rectTexte_to = texte_to.get_rect()
rectTexte_to.x = 1208
rectTexte_to.y = 420
rectTexte_show = texte_show.get_rect()
rectTexte_show.x = 1175
rectTexte_show.y = 490
rectBulle = bulle.get_rect()
rectBulle.x = 1100
rectBulle.y = 300
rectBouton_retour_help_option = bouton_retour_help_option.get_rect()
rectBouton_retour_help_option.x = -64
rectBouton_retour_help_option.y = 580

rectBouton_niveau1 = bouton_niveau1.get_rect()
rectBouton_niveau1.x = 60
rectBouton_niveau1.y = 100
rectBouton_niveau2 = bouton_niveau2.get_rect()
rectBouton_niveau2.x = 597
rectBouton_niveau2.y = 100
rectBouton_niveau3 = bouton_niveau3.get_rect()
rectBouton_niveau3.x = 1130
rectBouton_niveau3.y = 100
rectBouton_infinity = bouton_infinity.get_rect()
rectBouton_infinity.x = 597
rectBouton_infinity.y = 400


#Fonction du menu:
def menu() :
    x, y = pygame.mouse.get_pos()
    fenetre.blit(fond_ecran, (0, 0))
    fenetre.blit(texte_titre1, (60, 20))
    fenetre.blit(texte_titre2, (250, 70))
    fenetre.blit(bouton_play, rectBouton_play)
    fenetre.blit(bouton_option, rectBouton_option)
    fenetre.blit(bouton_exit, rectBouton_exit)
    fenetre.blit(texte_play, rectTexte_play)
    fenetre.blit(texte_option, rectTexte_option)
    fenetre.blit(texte_exit, rectTexte_exit)

    if x >= 264 and x <= 594 and y >= 173 and y <= 337 :
        rectBouton_play.x = 100
        rectBouton_play.y = -10
        rectTexte_play.x = 365
        rectTexte_play.y = 200
    else :
        rectBouton_play.x = 80
        rectBouton_play.y = 10
        rectTexte_play.x = 340
        rectTexte_play.y = 220
    if x >= 158 and x <= 459 and y >= 414 and y <= 570 :
        rectBouton_option.x = -10
        rectBouton_option.y = 230
        rectTexte_option.x = 215
        rectTexte_option.y = 435
    else :
        rectBouton_option.x = -30
        rectBouton_option.y = 240
        rectTexte_option.x = 190
        rectTexte_option.y = 445
    if x >= 78 and x <= 376 and y >= 626 and y <= 780 :
        rectBouton_exit.x = -90
        rectBouton_exit.y = 440
        rectTexte_exit.x = 185
        rectTexte_exit.y = 650
    else :
        rectBouton_exit.x = -110
        rectBouton_exit.y = 450
        rectTexte_exit.x = 160
        rectTexte_exit.y = 660

def jeux() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.player.image, game.player.rect)
    fenetre.blit(bouton_retour_menu, rectBouton_retour_menu)
    fenetre.blit(texte_retour_menu, rectTexte_retour_menu)
    fenetre.blit(bouton_niveau1, rectBouton_niveau1)
    fenetre.blit(bouton_niveau2, rectBouton_niveau2)
    fenetre.blit(bouton_niveau3, rectBouton_niveau3)
    fenetre.blit(bouton_infinity, rectBouton_infinity)

    if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
        rectBouton_retour_menu.x = -39
        rectBouton_retour_menu.y = 555
        rectTexte_retour_menu.x = 140
        rectTexte_retour_menu.y = 680
    else :
        rectBouton_retour_menu.x = -64
        rectBouton_retour_menu.y = 580
        rectTexte_retour_menu.x = 115
        rectTexte_retour_menu.y = 705

def niveau1() :
    pass

def niveau2() :
    pass

def niveau3() :
    pass

def infinity() :
    pass

def option() :
    fenetre.blit(fond_ecran_option, (0, 0))
    fenetre.blit(son, rectSon)
    fenetre.blit(pas_son, rectPas_son)
    fenetre.blit(bouton_retour_menu, rectBouton_retour_menu)
    fenetre.blit(texte_retour_menu, rectTexte_retour_menu)
    fenetre.blit(bouton_commands, rectBouton_commands)
    fenetre.blit(bulle, rectBulle)
    fenetre.blit(bouton_help, rectBouton_help)
    fenetre.blit(texte_tap, rectTexte_tap)
    fenetre.blit(texte_to, rectTexte_to)
    fenetre.blit(texte_show, rectTexte_show)
    fenetre.blit(texte_credits, (1130, 100))
    fenetre.blit(rond_credits, (900, 180))
    fenetre.blit(texte_credits_remi, (1110, 370))
    fenetre.blit(texte_credits_nom_creator, (1170, 440))
    fenetre.blit(texte_credits_damien, (1150, 520))
    fenetre.blit(texte_credits_nom_designer, (1192, 590))

def commands() :
    x, y = pygame.mouse.get_pos()
    fenetre.blit(fond_ecran_commands, (0, 0))
    fenetre.blit(bouton_retour_option, rectBouton_retour_option)
    fenetre.blit(texte_retour_option, rectTexte_retour_option)

    if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
        rectBouton_retour_option.x = -39
        rectBouton_retour_option.y = 555
        rectTexte_retour_option.x = 140
        rectTexte_retour_option.y = 680
    else :
        rectBouton_retour_option.x = -64
        rectBouton_retour_option.y = 580
        rectTexte_retour_option.x = 115
        rectTexte_retour_option.y = 705

def help() :
    fenetre.blit(fond_ecran_help, (0, 0))
    fenetre.blit(bouton_retour_help_option, rectBouton_retour_help_option)
    fenetre.blit(texte_retour_option, rectTexte_retour_option)

    if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
        rectBouton_retour_help_option.x = -39
        rectBouton_retour_help_option.y = 555
        rectTexte_retour_option.x = 140
        rectTexte_retour_option.y = 680
    else :
        rectBouton_retour_help_option.x = -64
        rectBouton_retour_help_option.y = 580
        rectTexte_retour_option.x = 115
        rectTexte_retour_option.y = 705

def exit_game() :
    print("Fermeture du projet !")
    boucle = False
    pygame.quit()
    sys.exit()


#Fps :
#clock = pygame.time.Clock(60)

#Boucle de jeux :
boucle = True
while boucle == True :
    x, y = pygame.mouse.get_pos()

    #if stat == "niveau1" or stat == "niveau2" or stat == "niveau3" :
    #Player :
    fenetre.blit(game.player.image, game.player.rect)
    #Déplacements player :
    if game.pressed.get(pygame.K_z) == True :
        print("Haut")
        game.player.move_haut()
    if game.pressed.get(pygame.K_s) == True :
        game.player.move_bas()
    if game.pressed.get(pygame.K_d) == True :
        game.player.move_droite()
    if game.pressed.get(pygame.K_q) == True :
        game.player.move_gauche()

    if stat == "menu" :
        menu()

    if stat == "jeux" :
        jeux()

    if stat == "niveau1" :
        niveau1()

    if stat == "niveau2" :
        niveau2()

    if stat == "niveau3" :
        niveau3()

    if stat == "infinity" :
        infinity()

    if stat == "option" :
        option()

    if stat == "exit" :
        exit_game()

    if stat == "commands" :
        commands()

    if stat == "help" :
        help()

    #Fps :

    #Flip :
    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        if event.type == pygame.QUIT :
            print("Fermeture du projet")
            boucle = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                print("Fermeture du projet")
                boucle = False
                pygame.quit()
                sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if stat == "option" :
                if x >= 95 and x <= 238 and y >= 122 and y <= 234 :
                    pygame.mixer.unpause()
                if x >= 352 and x <= 497 and y >= 92 and y <= 250 :
                    pygame.mixer.pause()
                if x >= 83 and x <= 365 and y >= 502 and y <= 607 :
                    stat = "commands"
                if x >= 148 and x <= 348 and y >= 265 and y <= 460 :
                    stat = "help"
                if x >= 90 and x <= 311 and y >= 660 and y <= 770 :
                    stat = "menu"
            elif stat == "menu" :
                if x >= 264 and x <= 594 and y >= 173 and y <= 337 :
                    stat = "jeux"
                if x >= 158 and x <= 459 and y >= 414 and y <= 570 :
                    stat = "option"
                if x >= 78 and x <= 376 and y >= 626 and y <= 780 :
                    stat = "exit"
            elif stat == "jeux" :
                if x >= 90 and x <= 311 and y >= 660 and y <= 770 :
                    stat = "menu"
            elif stat == "commands" or stat == "help":
                if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
                    stat = "option"

        '''Effet bouton option '''
        if stat == "option" :
            if x >= 95 and x <= 238 and y >= 122 and y <= 234 :
                rectSon.x = 60
                rectSon.y = 75
                son = pygame.transform.scale(son, (200, 200))
            else :
                rectSon.x = 85
                rectSon.y = 100
                son = pygame.transform.scale(son, (150, 150))
            if x >= 352 and x <= 497 and y >= 92 and y <= 250 :
                rectPas_son.x = 325
                rectPas_son.y = 75
                pas_son = pygame.transform.scale(pas_son, (200, 200))
            else :
                rectPas_son.x = 350
                rectPas_son.y = 100
                pas_son = pygame.transform.scale(pas_son, (150, 150))
            if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
                rectBouton_retour_menu.x = -39
                rectBouton_retour_menu.y = 555
                rectTexte_retour_menu.x = 140
                rectTexte_retour_menu.y = 680
            else :
                rectBouton_retour_menu.x = -64
                rectBouton_retour_menu.y = 580
                rectTexte_retour_menu.x = 115
                rectTexte_retour_menu.y = 705
            if x >= 83 and x <= 365 and y >= 502 and y <= 607 :
                rectBouton_commands.x = 60
                rectBouton_commands.y = 370
                bouton_commands = pygame.transform.scale(bouton_commands, (350, 350))
            else :
                rectBouton_commands.x = 70
                rectBouton_commands.y = 400
                bouton_commands = pygame.transform.scale(bouton_commands, (300, 300))
            if x >= 148 and x <= 348 and y >= 265 and y <= 460 :
                rectBouton_help.x = 140
                rectBouton_help.y = 250
                bouton_help = pygame.transform.scale(bouton_help, (250, 250))
            else :
                rectBouton_help.x = 150
                rectBouton_help.y = 265
                bouton_help = pygame.transform.scale(bouton_help, (200, 200))