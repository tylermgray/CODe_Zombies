import random
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()

round_start = pygame.mixer.Sound("data/sounds/new_round.wav")
zomb_attack = pygame.mixer.Sound("data/sounds/attk1.wav")
r6_start = pygame.mixer.Sound("data/sounds/r6_start.wav")
r6_end = pygame.mixer.Sound("data/sounds/r6_end.wav")
fetch = pygame.mixer.Sound("data/sounds/fetch.wav")
start_game = pygame.mixer.Sound("data/sounds/starting.wav")
sprinter1 = pygame.mixer.Sound("data/sounds/sprinter1.wav")
growl1 = pygame.mixer.Sound("data/sounds/amb1.wav")
tranzit_start = pygame.mixer.Sound("data/sounds/tranzit_start.wav")

motd_end = pygame.mixer.Sound("data/sounds/game_over/motd.wav")
motd_end_special = pygame.mixer.Sound("data/sounds/game_over/motd_special.wav")
soe_end = pygame.mixer.Sound("data/sounds/game_over/soe.wav")
nacht_end = pygame.mixer.Sound("data/sounds/game_over/nacht.wav")


gun_1911 = pygame.mixer.Sound("data/sounds/1911.wav")

def gamestart_sound():
    
    if random.randint(0, 1) == 0:
        start_game.play()

    else:
        tranzit_start.play()


def game_over_sound():

    if random.randint(0, 6) == 0:
        motd_end.play()
    elif random.randint(0, 6) == 1:
        motd_end_special.play()
    elif random.randint(0, 6) == 2:
        soe_end.play()
    else:
        nacht_end.play()


