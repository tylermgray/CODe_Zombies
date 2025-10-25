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

gun_1911 = pygame.mixer.Sound("data/sounds/1911.wav")

def gamestart_sound():
    
    if random.randint(0, 1) == 0:
        start_game.play()

    else:
        tranzit_start.play()

