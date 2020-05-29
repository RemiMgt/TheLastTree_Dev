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

#Statue niveau :
stat_niveau = "niveau1"

#Bucheron random :
bucheron_random = randint(1, 100)

#Passage niveaux :
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
infini = (254, 1, 144)

#Variables :
bucheron_random = 1
L = 1600
H = 900
stat = "menu"
arial_font_min = pygame.font.SysFont("arial", 20, True, False)
arial_font = pygame.font.SysFont("arial", 70, True, False)
arial_font_grand = pygame.font.SysFont("arial", 260, True, False)
arial_font_petit = pygame.font.SysFont("arial", 38, True, False)
arial_font_moyen = pygame.font.SysFont("arial", 60, True, False)
arial_font_moyen_moins = pygame.font.SysFont("arial", 55, True, False)
arial_font_credits = pygame.font.SysFont("arial", 25, True, False)
arial_font_petit_credits = pygame.font.SysFont("arial", 30, False, True)
arial_font_brouillon = pygame.font.SysFont("arial", 40, True, False)
arial_font_niveau = pygame.font.SysFont("arial", 60, True, False)
arial_font_score = pygame.font.SysFont("arial", 100, True, False)
arial_font_giant = pygame.font.SysFont("arial", 300, True, False)

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

#Bruitage click :
click = pygame.mixer.Sound("assets/bruit-clic.wav")

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
texte_credits = arial_font_brouillon.render("Credits : ", True, white)
texte_attack = arial_font_grand.render(chr(attack), True, red)
texte_retour_menu_fin = arial_font_moyen.render("Menu", True, marron)
texte_timer = arial_font_moyen.render(str(timer), True, red)
texte_nombre_kill = arial_font_moyen.render(str(game.nombre_kill), True, red)
texte_score = arial_font_moyen.render("Score", True, noir)
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
texte_infini = arial_font_niveau.render("No Time Limit", True, red)
texte_menu = arial_font_petit.render("Menu", True, marron)
texte_niveau_suivant = arial_font_petit.render("Niveau suivant", True, marron)
texte_retry = arial_font_petit.render("Recommencer", True, marron)
texte_the_end = arial_font_giant.render("THE END", True, marron)

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
    fenetre.blit(bouton_infinity, (1020, 680))
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
    fenetre.blit(texte_infini, (1085, 720))


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
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau7() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)


def niveau8() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau9() :
    fenetre.blit(game.map.image, game.map.rect)
    fenetre.blit(game.arbre.image, game.arbre.rect)
    fenetre.blit(game.player.image, game.player.rect)

def niveau10() :
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

def fin_de_jeux_gagne() :
    fenetre.blit(menu_fin_jeux, (0, 0))
    fenetre.blit(fin_jeux, rectFin_jeux)
    fenetre.blit(bouton_niveau_suivant, (360, 130))
    fenetre.blit(bouton_menu, (360, 280))
    fenetre.blit(texte_menu, (740, 460))
    fenetre.blit(texte_niveau_suivant, (655, 310))

def fin_de_jeux_perdu() :
    fenetre.blit(menu_fin_jeux, (0, 0))
    fenetre.blit(fin_jeux, rectFin_jeux)
    fenetre.blit(bouton_retry, (360, 130))
    fenetre.blit(bouton_menu, (360, 280))
    fenetre.blit(texte_menu, (740, 460))
    fenetre.blit(texte_retry, (655, 310))

def fin_jeux_infini() :
    fenetre.blit(menu_fin_jeux, (0, 0))
    fenetre.blit(fin_jeux, rectFin_jeux)
    fenetre.blit(bouton_retry, (360, 130))
    fenetre.blit(texte_nombre_kill, (790, 130))
    fenetre.blit(texte_score, (720, 30))
    fenetre.blit(bouton_menu, (360, 280))
    fenetre.blit(texte_menu, (740, 460))
    fenetre.blit(texte_retry, (655, 310))


def the_end() :
    fenetre.blit(menu_end, (0, 0))
    fenetre.blit(texte_the_end, (120, 100))
    fenetre.blit(bouton_menu, (360, 480))
    fenetre.blit(texte_menu, (740, 660))

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
    print(stat)

    if stat == "menu" or stat == "jeux" or stat == "option" or stat == "commands" or stat == "help" : 
        timer = -100

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
        bouton_niveau2 = pygame.transform.scale(bouton_niveau2, (350, 150))
        bouton_niveau3 = pygame.transform.scale(bouton_niveau3, (350, 150))
        bouton_niveau4 = pygame.transform.scale(bouton_niveau4, (350, 150))
        bouton_niveau5 = pygame.transform.scale(bouton_niveau5, (350, 150))
        bouton_niveau6 = pygame.transform.scale(bouton_niveau6, (350, 150))
        bouton_niveau7 = pygame.transform.scale(bouton_niveau7, (350, 150))
        bouton_niveau8 = pygame.transform.scale(bouton_niveau8, (350, 150))
        bouton_niveau9 = pygame.transform.scale(bouton_niveau9, (350, 150))
        bouton_niveau10 = pygame.transform.scale(bouton_niveau10, (350, 150))
        jeux()

    if stat == "niveau1" :
        stat_niveau = "niveau1"
        bucheron_random = randint(1, 100)
        niveau1()
    if stat == "niveau2" :
        stat_niveau = "niveau2"
        bucheron_random = randint(1, 100)
        niveau2()
    if stat == "niveau3" :
        stat_niveau = "niveau3"
        bucheron_random = randint(1, 100)
        niveau3()
    if stat == "niveau4" :
        stat_niveau = "niveau4"
        bucheron_random = randint(1, 100)
        niveau4()
    if stat == "niveau5" :
        stat_niveau = "niveau5"
        bucheron_random = randint(1, 100)
        niveau5()
    if stat == "niveau6" :
        stat_niveau = "niveau6"
        bucheron_random = randint(1, 90)
        niveau6()
    if stat == "niveau7" :
        stat_niveau = "niveau7"
        bucheron_random = randint(1, 80)
        niveau7()
    if stat == "niveau8" :
        stat_niveau = "niveau8"
        bucheron_random = randint(1, 70)
        niveau8()
    if stat == "niveau9" :
        stat_niveau = "niveau9"
        bucheron_random = randint(1, 60)
        niveau9()
    if stat == "niveau10" :
        stat_niveau = "niveau10"
        bucheron_random = randint(1, 50)
        niveau10()
    if stat == "infinity" :
        stat_niveau = "infinity"
        bucheron_random = randint(1, 40)
        infinity()
    if stat == "fin_jeux_infinity" :
        fin_jeux_infini()
    if stat == "option" :
        option()
    if stat == "exit" :
        exit_game()
    if stat == "commands" :
        commands()
    if stat == "help" :
        help()
    if stat == "fin_jeux_gagne" :
        fin_de_jeux_gagne()
    if stat == "fin_jeux_perdu" :
        fin_de_jeux_perdu()
    if stat == "the_end" :
        the_end()

    if stat == "niveau1" or stat == "niveau2" or stat == "niveau3" or stat == "niveau4" or stat == "niveau5" or stat == "niveau6" or stat == "niveau7" or stat == "niveau8" or stat == "niveau9" or stat == "niveau10" :
        game.player.image = pygame.transform.scale(game.player.image, (120, 120))
        fenetre.blit(texte_timer, rectTexte_timer)
        texte_timer = arial_font_moyen.render(str(timer), True, red)
        if game.GAME_OVER == False :
            if bucheron_random == 40 :
                game.ajout_bucheron_H()
            if bucheron_random == 30 :
                game.ajout_bucheron_C()

    if stat == "infinity" :
        texte_nombre_kill = arial_font_moyen.render(str(game.nombre_kill), True, red)
        game.player.image = pygame.transform.scale(game.player.image, (120, 120))
        fenetre.blit(texte_nombre_kill, (20, 20))
        if game.GAME_OVER == False :
            if bucheron_random == 40 :
                game.ajout_bucheron_H()
            if bucheron_random == 30 :
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

    if timer == 0 :
        print("Gagné !")
        game.all_bucheron_C.empty()
        game.all_bucheron_H.empty()
        game.all_projectile.empty()
        #Changer texte en perdu
        stat = "fin_jeux_gagne"
        pygame.mixer.music.unpause()

    if stat_niveau == "infinity" :
        if game.GAME_OVER == True :
            timer = -5
            game.nombre_kill = 0
            stat = "fin_jeux_infinity"
            pygame.mixer.music.unpause()

    if game.GAME_OVER == True :
        if stat_niveau != "infinity" :
            timer = -5
            print("Perdu !")
            stat = "fin_jeux_perdu"
            pygame.mixer.music.unpause()

    if stat == "commands" :
        texte_attack = arial_font_grand.render(chr(attack), True, red)
        fenetre.blit(texte_attack, (10, 10))
        #print(chr(attack))

    #Textes et boutons UP :
    if passage_niveau2 == True :
        bouton_niveau2 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau2 = arial_font_niveau.render("Niveau2", True, orange)
    if passage_niveau3 == True :
        bouton_niveau3 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau3 = arial_font_niveau.render("Niveau3", True, orange)
    if passage_niveau4 == True :
        bouton_niveau4 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau4 = arial_font_niveau.render("Niveau4", True, orange)
    if passage_niveau5 == True :
        bouton_niveau5 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau5 = arial_font_niveau.render("Niveau5", True, orange)
    if passage_niveau6 == True :
        bouton_niveau6 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau6 = arial_font_niveau.render("Niveau6", True, orange)
    if passage_niveau7 == True :
        bouton_niveau7 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau7 = arial_font_niveau.render("Niveau7", True, orange)
    if passage_niveau8 == True :
        bouton_niveau8 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau8 = arial_font_niveau.render("Niveau8", True, orange)
    if passage_niveau9 == True :
        bouton_niveau9 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau9 = arial_font_niveau.render("Niveau9", True, orange)
    if passage_niveau10 == True :
        bouton_niveau10 = pygame.image.load("assets/bouton_niveau.png")
        texte_niveau10 = arial_font_niveau.render("Niveau10", True, orange)

    if stat == "fin_jeux_gagne" :
        if stat_niveau == "niveau10" :
                stat = "the_end"

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

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(event.button)
            #click.play()
            if stat == "the_end" :
                if x >= 598 and x <= 995 and y >= 615 and y <= 756 :
                    stat = "menu"
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
                if x >= 90 and x <= 440 and y >= 79 and y <= 230 :
                    timer = 30
                    pygame.mixer.music.pause()
                    stat = "niveau1"
                if passage_niveau2 == True :
                    if x >= 627 and x <= 974 and y >= 80 and y <= 223 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau2"
                if passage_niveau3 == True :
                    if x >= 1159 and x <= 1512 and y >= 80 and y <= 223 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau3"
                if passage_niveau4 == True :
                    if x >= 91 and x <= 438 and y >= 280 and y <= 427 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau4"
                if passage_niveau5 == True :
                    if x >= 627 and x <= 974 and y >= 279 and y <= 424 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau5"
                if passage_niveau6 == True :
                    if x >= 1159 and x <= 1512 and y >= 280 and y <= 427 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau6"
                if passage_niveau7 == True :
                    if x >= 90 and x <= 442 and y >= 476 and y <= 627 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau7"
                if passage_niveau8 == True :
                    if x >= 625 and x <= 974 and y >= 476 and y <= 627 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau8"
                if passage_niveau9 == True :
                    if x >= 1159 and x <= 1512 and y >= 476 and y <= 627 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau9"
                if passage_niveau10 == True :
                    if x >= 625 and x <= 974 and y >= 680 and y <= 826 :
                        timer = 30
                        pygame.mixer.music.pause()
                        stat = "niveau10"
                if x >= 1019 and x <= 1568 and y >= 680 and y <= 830 :
                    game.nombre_kill = 0
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
            elif stat == "fin_jeux_gagne" :
                    if stat_niveau == "niveau1" :
                        passage_niveau2 = True
                    if stat_niveau == "niveau2" :
                        passage_niveau3 = True
                    if stat_niveau == "niveau3" :
                        passage_niveau4 = True
                    if stat_niveau == "niveau4" :
                        passage_niveau5 = True
                    if stat_niveau == "niveau5" :
                        passage_niveau6 = True
                    if stat_niveau == "niveau6" :
                        passage_niveau7 = True
                    if stat_niveau == "niveau7" :
                        passage_niveau8 = True
                    if stat_niveau == "niveau8" :
                        passage_niveau9 = True
                    if stat_niveau == "niveau9" :
                        passage_niveau10 = True
                    game.GAME_OVER = False
                    game.map.rect.x = -1050
                    game.map.rect.y = -700
                    game.player.rect.x = 740
                    game.player.rect.y = 380
                    if x >= 586 and x <= 1016 and y >= 420 and y <= 540 :
                        stat = "menu"
                    if x >= 586 and x <= 1016 and y >= 270 and y <= 388 :
                        game.GAME_OVER = False
                        game.map.rect.x = -1050
                        game.map.rect.y = -700
                        game.player.rect.x = 740
                        game.player.rect.y = 380
                        pygame.mixer.music.pause()
                        timer = 30
                        if stat_niveau == "niveau1" :
                            stat = "niveau2"
                        if stat_niveau == "niveau2" :
                            stat = "niveau3"
                        if stat_niveau == "niveau3" :
                            stat = "niveau4"
                        if stat_niveau == "niveau4" :
                            stat = "niveau5"
                        if stat_niveau == "niveau5" :
                            stat = "niveau6"
                        if stat_niveau == "niveau6" :
                            stat = "niveau7"
                        if stat_niveau == "niveau7" :
                            stat = "niveau8"
                        if stat_niveau == "niveau8" :
                            stat = "niveau9"
                        if stat_niveau == "niveau9" :
                            stat = "niveau10"
            elif stat == "fin_jeux_perdu" or stat == "fin_jeux_infinity":
                    game.GAME_OVER = False
                    game.map.rect.x = -1050
                    game.map.rect.y = -700
                    game.player.rect.x = 740
                    game.player.rect.y = 380
                    if x >= 586 and x <= 1016 and y >= 420 and y <= 540 :
                        stat = "menu"
                    if x >= 586 and x <= 1016 and y >= 270 and y <= 388 :
                        timer = 30
                        pygame.mixer.music.pause()
                        game.nombre_kill = 0
                        stat = stat_niveau

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