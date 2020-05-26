#Impotations :
import pygame
import time
from pygame.locals import *
from random import *

from image import *
from game import Game
import sys

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

game = Game()

#Bucheron random :
bucheron_random = randint(1, 100)

#Passage niveaus :
passage_niveau2 = False
passage_niveau3 = False
passage_niveau4 = False
passage_niveau5 = False
passage_niveau6 = False
passage_niveau7 = False
passage_niveau8 = False
passage_niveau9 = False
passage_niveau10 = False

#Couleurs :
white = (255, 255, 255)
red = (255, 0, 0)
noir = (0, 0, 0)
marron = (98, 55, 26)
vert_titre = (12, 50, 2)
orange = (187, 109, 28)
gris = (117, 117, 117)

#Variables :
bucheron_random = 1
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
arial_font_niveau = pygame.font.SysFont("arial", 60, True, False)
arial_font_score = pygame.font.SysFont("arial", 100, True, False)

#Commands clavier :
haut = pygame.K_w
bas = pygame.K_s
droite = pygame.K_d
gauche = pygame.K_a
attack = pygame.K_SPACE

#Timer :
timer = 30
pygame.time.set_timer(pygame.USEREVENT, 1000)

#Titre jeux :
texte_titre1 = arial_font_grand.render("T", True, vert_titre)
texte_titre2 = arial_font.render("he Last Tree", True, vert_titre)

#Musiques :
musique_menu = "assets/musique.ogg"
pygame.mixer.music.load(musique_menu)
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1, 0)

#Joystik :

joy = "rien"

nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branché(s)")

#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en crée un s'il y a en au moins un
if nb_joysticks > 0:
	mon_joystick = pygame.joystick.Joystick(0)

	mon_joystick.init() #Initialisation

'''
print("Axes :", mon_joystick.get_numaxes())
print("Boutons :", mon_joystick.get_numbuttons())
print("Trackballs :", mon_joystick.get_numballs())
print("Hats :", mon_joystick.get_numhats())
'''

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
texte_credits_remi = arial_font_credits.render("Créateur développeur :", True, noir)
texte_credits_nom_creator = arial_font_petit_credits.render("Rémi MAIGROT", True, noir)
texte_credits_nom_designer = arial_font_petit_credits.render("Damien Barthe", True, noir)
texte_credits_damien = arial_font_credits.render("Illustrations :", True, noir)
texte_credits = arial_font_brouillon.render("Credits : ", True, red)
texte_attack = arial_font_grand.render(chr(attack), True, red)
texte_retour_menu_fin = arial_font_moyen.render("Menu", True, marron)
texte_timer = arial_font_moyen.render(str(timer), True, red)

texte_niveau1 = arial_font_niveau.render("Niveau1", True, orange)
texte_niveau2 = arial_font_niveau.render("Niveau2", True, gris)
texte_niveau3 = arial_font_niveau.render("Niveau3", True, gris)
texte_niveau4 = arial_font_niveau.render("Niveau4", True, gris)
texte_niveau5 = arial_font_niveau.render("Niveau5", True, gris)
texte_niveau6 = arial_font_niveau.render("Niveau6", True, gris)
texte_niveau7 = arial_font_niveau.render("Niveau7", True, gris)
texte_niveau8 = arial_font_niveau.render("Niveau8", True, gris)
texte_niveau9 = arial_font_niveau.render("Niveau9", True, gris)
texte_niveau10 = arial_font_niveau.render("Niveau10", True, gris)
texte_infini = arial_font_niveau.render("Infini", True, orange)

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

rectCommands_fleche = commands_fleche.get_rect()
rectCommands_fleche.x = 1260
rectCommands_fleche.y = 150
rectCommands_zqsd = commands_zqsd.get_rect()
rectCommands_zqsd.x = 1260
rectCommands_zqsd.y = 350
rectCommands_wasd = commands_wasd.get_rect()
rectCommands_wasd.x = 1260
rectCommands_wasd.y = 550

rectFin_jeux = fin_jeux.get_rect()
rectFin_jeux.x = 230
rectFin_jeux.y = 0

rectTexte_timer = texte_timer.get_rect()
rectTexte_timer.x = 20
rectTexte_timer.y = 20

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
    fenetre.blit(fond_ecran_niveau, (0, 0))
    fenetre.blit(bouton_retour_menu, rectBouton_retour_menu)
    fenetre.blit(texte_retour_menu, rectTexte_retour_menu)
    fenetre.blit(bouton_niveau1, (90, 80))
    fenetre.blit(bouton_niveau2, (625, 80))
    fenetre.blit(bouton_niveau3, (1160, 80))
    fenetre.blit(bouton_niveau4, (90, 280))
    fenetre.blit(bouton_niveau5, (625, 280))
    fenetre.blit(bouton_niveau6, (1160, 280))
    fenetre.blit(bouton_niveau7, (90, 480))
    fenetre.blit(bouton_niveau8, (625, 480))
    fenetre.blit(bouton_niveau9, (1160, 480))
    fenetre.blit(bouton_niveau10, (625, 680))
    fenetre.blit(bouton_infinity, (1160, 680))
    fenetre.blit(texte_niveau1, (140, 120))
    fenetre.blit(texte_niveau2, (675, 120))
    fenetre.blit(texte_niveau3, (1210, 120))
    fenetre.blit(texte_niveau4, (140, 320))
    fenetre.blit(texte_niveau5, (675, 320))
    fenetre.blit(texte_niveau6, (1210, 320))
    fenetre.blit(texte_niveau7, (140, 520))
    fenetre.blit(texte_niveau8, (675, 520))
    fenetre.blit(texte_niveau9, (1210, 520))
    fenetre.blit(texte_niveau10, (675, 720))
    fenetre.blit(texte_infini, (1210, 720))

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

    if x >= 60 and x <= 460 and y >= 100 and y <= 300 :
        fenetre.blit(bouton2_niveau1, (90, 80))
        fenetre.blit(texte_niveau1, (140, 120))
    else :
        fenetre.blit(bouton_niveau1, (90, 80))
        fenetre.blit(texte_niveau1, (140, 120))

    if passage_niveau2 == True :
        if x >= 597 and x <= 997 and y >= 100 and y <= 300 :
            fenetre.blit(bouton2_niveau2, (597, 100))
            fenetre.blit(texte_niveau2, (675, 160))
        else :
            fenetre.blit(bouton_niveau2, (1000, 0))
            fenetre.blit(texte_niveau2, (675, 160))

    if passage_niveau3 == True :
        if x >= 1130 and x <= 1530 and y >= 100 and y <= 300 :
            fenetre.blit(bouton2_niveau3, (1130, 100))
            fenetre.blit(texte_niveau3, (1210, 160))
        else :
            fenetre.blit(bouton_niveau3, (1000, 0))
            fenetre.blit(texte_niveau3, (1210, 160))

    if x >= 597 and x <= 997 and y >= 400 and y <= 600 :
        fenetre.blit(bouton2_niveau_infi, (1160, 680))
        fenetre.blit(texte_infini, (1210, 720))
    else :
        fenetre.blit(bouton_infinity, (1160, 680))
        fenetre.blit(texte_infini, (1210, 720))


def niveau1() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)


def niveau2() :
    game.bucheron_H.vitesse = 9
    game.bucheron_C.vitesse = 9
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau3() :
    game.bucheron_H.vitesse = 10
    game.bucheron_C.vitesse = 10
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau4() :
    game.bucheron_H.vitesse = 11
    game.bucheron_C.vitesse = 11
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)


def niveau5() :
    game.bucheron_H.vitesse = 12
    game.bucheron_C.vitesse = 12
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau6() :
    bucheron_random = randint(1, 90)
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau7() :
    bucheron_random = randint(1, 80)
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)


def niveau8() :
    bucheron_random = randint(1, 70)
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau9() :
    bucheron_random = randint(1, 60)
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau10() :
    bucheron_random = randint(1, 50)
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def infinity() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

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
    fenetre.blit(texte_credits_nom_creator, (1130, 440))
    fenetre.blit(texte_credits_damien, (1160, 520))
    fenetre.blit(texte_credits_nom_designer, (1146, 590))

def commands() :
    x, y = pygame.mouse.get_pos()
    fenetre.blit(fond_ecran_commands, (0, 0))
    fenetre.blit(bouton_retour_option, rectBouton_retour_option)
    fenetre.blit(texte_retour_option, rectTexte_retour_option)
    fenetre.blit(commands_fleche, rectCommands_fleche)
    fenetre.blit(commands_zqsd, rectCommands_zqsd)
    fenetre.blit(commands_wasd, rectCommands_wasd)

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

def fin_de_jeux() :
    fenetre.blit(menu_fin_jeux, (0, 0))
    fenetre.blit(fin_jeux, rectFin_jeux)
    fenetre.blit(bouton_retour_menu_fin, (670, 450))
    fenetre.blit(texte_retour_menu_fin, (715, 475))

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

    #print(timer)

    #print(game.score)
    x, y = pygame.mouse.get_pos()
    game.arbre.rect.x = game.map.rect.x + 1490
    game.arbre.rect.y = game.map.rect.y + 1490

    if stat == "niveau1" or stat == "niveau2" or stat == "niveau3" or stat == "niveau4" or stat == "niveau5" or stat == "niveau6" or stat == "niveau7" or stat == "niveau8" or stat == "niveau9" or stat == "niveau10" or stat == "infinity":
        #Player :
        fenetre.blit(game.player.image, game.player.rect)
        #Déplacements player :
        '''Clavier : '''
        if game.pressed.get(haut) == True and game.map.rect.y < -10:
            game.player.move_haut()
            game.player.animation_haut()
        if game.pressed.get(bas) == True and game.map.rect.y > -2080:
            game.player.move_bas()
            game.player.animation_bas()
        if game.pressed.get(droite) == True and game.map.rect.x > -1380:
            game.player.move_droite()
            game.player.animation_droite()
        if game.pressed.get(gauche) == True and game.map.rect.x < 0:
            game.player.move_gauche()
            game.player.animation_gauche()

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

    if stat == "niveau4" :
        niveau4()

    if stat == "niveau5" :
        niveau5()

    if stat == "niveau6" :
        niveau6()

    if stat == "niveau7" :
        niveau7()

    if stat == "niveau8" :
        niveau8()

    if stat == "niveau9" :
        niveau9()

    if stat == "niveau10" :
        niveau10()

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

    if stat == "fin_jeux" :
        fin_de_jeux()

    if stat == "niveau1" or stat == "niveau2" or stat == "niveau3" or stat == "infinity" :
        fenetre.blit(texte_timer, rectTexte_timer)
        texte_timer = arial_font_moyen.render(str(timer), True, red)
        if game.GAME_OVER == False :
            if bucheron_random == 40 :
                game.ajout_bucheron_H()
            if bucheron_random == 50 :
                game.ajout_bucheron_C()

    #Projectile :
    for projectile in game.all_projectile :
        projectile.move()
        #projectile.move_player()
    for bucheron_H in game.all_bucheron_H :
        bucheron_H.move_player()
        bucheron_H.move()
    for bucheron_C in game.all_bucheron_C :
        bucheron_C.move_player()
        bucheron_C.move()
    game.all_projectile.draw(fenetre)
    game.all_bucheron_H.draw(fenetre)
    game.all_bucheron_C.draw(fenetre)

    if game.nombre_kill_restant == 0 :
        print("Gagné !")
        #Changer texte en perdu
        stat = "fin_jeux"
        pygame.mixer.music.unpause()

    if game.GAME_OVER == True :
        print("Perdu !")
        #Changer texte en gagner
        stat = "fin_jeux"
        pygame.mixer.music.unpause()

    if stat == "commands" :
        texte_attack = arial_font_grand.render(chr(attack), True, red)
        fenetre.blit(texte_attack, (10, 10))
        #print(chr(attack))

    #Flip :
    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == JOYAXISMOTION :
            game.pressed[event.axis] = True
            game.pressed[event.value] = True

        if event.type == JOYAXISMOTION :
            if event.axis == 1 and event.value < 0 and game.map.rect.y < -10 :
                game.player.move_haut_joy()
            if event.axis == 1 and event.value > 0 and game.map.rect.y > -2080 :
                game.player.move_bas_joy()
            if event.axis == 0 and event.value < 0 and game.map.rect.x < 0 :
                game.player.move_gauche_joy()
            if event.axis == 0 and event.value > 0 and game.map.rect.x > -1380 :
                game.player.move_droite_joy()

        if event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        if event.type == pygame.QUIT :
            print("Fermeture du projet")
            boucle = False
            pygame.quit()
            sys.exit()

        if event.type == JOYBUTTONDOWN:
            print(event.button)
            game.pressed[event.button] = True
            if event.button == 0 and stat == "niveau1" :
                game.ajout_projectile(game.player.direction)
        if event.type == JOYBUTTONUP :
            game.pressed[event.button] = False

        if event.type == pygame.USEREVENT :
            timer -= 1


        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                print("Fermeture du projet")
                boucle = False
                pygame.quit()
                sys.exit()
            if event.key == attack and stat == "niveau1" :
                game.ajout_projectile(game.player.direction)
            if event.key == attack and stat == "niveau2" :
                game.ajout_projectile(game.player.direction)
            if event.key == attack and stat == "niveau3" :
                game.ajout_projectile(game.player.direction)
            if event.key == attack and stat == "infinity" :
                game.ajout_projectile(game.player.direction)

            if stat == "commands" :
                attack = pygame.key.get_pressed()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if stat == "option" :
                if x >= 95 and x <= 238 and y >= 122 and y <= 234 :
                    pygame.mixer.music.unpause()
                if x >= 352 and x <= 497 and y >= 92 and y <= 250 :
                    pygame.mixer.music.pause()
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
                if x >= 60 and x <= 460 and y >= 100 and y <= 300 :
                    timer = 30
                    pygame.mixer.music.pause()
                    stat = "niveau1"
                if passage_niveau2 == True :
                    if x >= 1130 and x <= 1530 and y >= 100 and y <= 300 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau2"
                if passage_niveau3 == True :
                    if x >= 597 and x <= 997 and y >= 100 and y <= 300 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau3"
                if x >= 597 and x <= 997 and y >= 400 and y <= 600 :
                    timer = 30
                    pygame.mixer.music.pause()
                    stat = "infinity"
            elif stat == "commands" or stat == "help":
                if x >= 72 and x <= 292 and y >= 677 and y <= 778 :
                    stat = "option"
                if x >= 1260 and x <= 1460 and y >= 150 and y <= 279 :
                    rectCommands_fleche.x = 1290
                    rectCommands_fleche.y = 130
                    rectCommands_zqsd.x = 1260
                    rectCommands_zqsd.y = 350
                    rectCommands_wasd.x = 1260
                    rectCommands_wasd.y = 550
                    haut = pygame.K_UP
                    bas = pygame.K_DOWN
                    droite = pygame.K_RIGHT
                    gauche = pygame.K_LEFT
                if x >= 1260 and x <= 1460 and y >= 350 and y <= 479 :
                    rectCommands_zqsd.x = 1290
                    rectCommands_zqsd.y = 330
                    rectCommands_fleche.x = 1260
                    rectCommands_fleche.y = 150
                    rectCommands_wasd.x = 1260
                    rectCommands_wasd.y = 550
                    haut = pygame.K_w
                    bas = pygame.K_s
                    droite = pygame.K_d
                    gauche = pygame.K_a
                if x >= 1260 and x <= 1460 and y >= 550 and y <= 679 :
                    haut = pygame.K_z
                    bas = pygame.K_s
                    droite = pygame.K_d
                    gauche = pygame.K_q
                    rectCommands_wasd.x = 1290
                    rectCommands_wasd.y = 530
                    rectCommands_fleche.x = 1260
                    rectCommands_fleche.y = 150
                    rectCommands_zqsd.x = 1260
                    rectCommands_zqsd.y = 350
            elif stat == "fin_jeux" :
                if x >= 681 and x <= 960 and y >= 460 and y <= 560 :
                    game.GAME_OVER = False
                    stat = "menu"
                    game.map.rect.x = -1050
                    game.map.rect.y = -700
                    game.player.rect.x = 740
                    game.player.rect.y = 380

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
