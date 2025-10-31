import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()


# Round Sounds
round_change = "data/sounds/new_round.wav"
de_change00 = "data/sounds/de_start.wav"
de_change01 = "data/sounds/de_end.wav"
de_change02 = "data/sounds/de_change2.wav"
de_change03 = "data/sounds/de_change1.wav"
soe_change = "data/sounds/soe_round.wav"
round_end = "data/sounds/round_end.wav"

rounds = [round_change, de_change00, de_change01, de_change02, de_change03, soe_change, round_end]

# Round 6 Sounds
r6_start = "data/sounds/r6_start.wav"
r6_end = "data/sounds/r6_end.wav"
fetch = "data/sounds/fetch.wav"

# Zombie Sound Effects =============================

# Ambs
zomb_amb00 = "data/sounds/zombie/zomb_amb/amb00.wav"
zomb_amb01 = "data/sounds/zombie/zomb_amb/amb01.wav"
zomb_amb02 = "data/sounds/zombie/zomb_amb/amb02.wav"
zomb_amb03 = "data/sounds/zombie/zomb_amb/amb03.wav"
zomb_amb04 = "data/sounds/zombie/zomb_amb/amb04.wav"
zomb_amb05 = "data/sounds/zombie/zomb_amb/amb05.wav"

zomb_amb = [zomb_amb00, zomb_amb01, zomb_amb02, zomb_amb03, zomb_amb04, zomb_amb05]

# Attacks 
zomb_attk00 = "data/sounds/zombie/zomb_attacks/zmb_attk00.wav"
zomb_attk01 = "data/sounds/zombie/zomb_attacks/zmb_attk01.wav"
zomb_attk02 = "data/sounds/zombie/zomb_attacks/zmb_attk02.wav"
zomb_attk03 = "data/sounds/zombie/zomb_attacks/zmb_attk03.wav"
zomb_attk04 = "data/sounds/zombie/zomb_attacks/zmb_attk04.wav"
zomb_attk05 = "data/sounds/zombie/zomb_attacks/zmb_attk05.wav"
zomb_attk06 = "data/sounds/zombie/zomb_attacks/zmb_attk06.wav"
zomb_attk07 = "data/sounds/zombie/zomb_attacks/zmb_attk07.wav"
zomb_attk08 = "data/sounds/zombie/zomb_attacks/zmb_attk08.wav"
zomb_attk09 = "data/sounds/zombie/zomb_attacks/zmb_attk09.wav"
zomb_attk10 = "data/sounds/zombie/zomb_attacks/zmb_attk10.wav"
zomb_attk11 = "data/sounds/zombie/zomb_attacks/zmb_attk11.wav"
zomb_attk12 = "data/sounds/zombie/zomb_attacks/zmb_attk12.wav"
zomb_attk13 = "data/sounds/zombie/zomb_attacks/zmb_attk13.wav"
zomb_attk14 = "data/sounds/zombie/zomb_attacks/zmb_attk14.wav"
zomb_attk15 = "data/sounds/zombie/zomb_attacks/zmb_attk15.wav"

zomb_attk = [zomb_attk00, zomb_attk01, zomb_attk02, zomb_attk03, zomb_attk04, zomb_attk05, zomb_attk06, zomb_attk07, zomb_attk08, zomb_attk09, zomb_attk10, zomb_attk11, zomb_attk12, zomb_attk13, zomb_attk14, zomb_attk15]

# Behind
zomb_behind00 = "data/sounds/zombie/zomb_behind/behind00.wav"
zomb_behind01 = "data/sounds/zombie/zomb_behind/behind01.wav"
zomb_behind02 = "data/sounds/zombie/zomb_behind/behind02.wav"
zomb_behind03 = "data/sounds/zombie/zomb_behind/behind03.wav"
zomb_behind04 = "data/sounds/zombie/zomb_behind/behind04.wav"

zomb_behind = [zomb_behind00, zomb_behind01, zomb_behind02, zomb_behind03, zomb_behind04]

# Death
zomb_death00 = "data/sounds/zombie/zomb_death/death00.wav"
zomb_death01 = "data/sounds/zombie/zomb_death/death01.wav"
zomb_death02 = "data/sounds/zombie/zomb_death/death02.wav"
zomb_death03 = "data/sounds/zombie/zomb_death/death03.wav"
zomb_death04 = "data/sounds/zombie/zomb_death/death04.wav"
zomb_death05 = "data/sounds/zombie/zomb_death/death05.wav"
zomb_death06 = "data/sounds/zombie/zomb_death/death06.wav"
zomb_death07 = "data/sounds/zombie/zomb_death/death07.wav"
zomb_death08 = "data/sounds/zombie/zomb_death/death08.wav"
zomb_death09 = "data/sounds/zombie/zomb_death/death09.wav"
zomb_death10 = "data/sounds/zombie/zomb_death/death10.wav"

zomb_death = [zomb_death00, zomb_death01, zomb_death02, zomb_death03, zomb_death04, zomb_death05, zomb_death06, zomb_death07, zomb_death08, zomb_death09, zomb_death10]

# Sprint
zomb_sprint01 = "data/sounds/zombie/zomb_sprint/sprint01.wav"
zomb_sprint02 = "data/sounds/zombie/zomb_sprint/sprint02.wav"
zomb_sprint03 = "data/sounds/zombie/zomb_sprint/sprint03.wav"
zomb_sprint04 = "data/sounds/zombie/zomb_sprint/sprint04.wav"
zomb_sprint05 = "data/sounds/zombie/zomb_sprint/sprint05.wav"
zomb_sprint06 = "data/sounds/zombie/zomb_sprint/sprint06.wav"
zomb_sprint07 = "data/sounds/zombie/zomb_sprint/sprint07.wav"
zomb_sprint08 = "data/sounds/zombie/zomb_sprint/sprint08.wav"
zomb_sprint09 = "data/sounds/zombie/zomb_sprint/sprint09.wav"

zomb_sprint = [zomb_sprint01, zomb_sprint02, zomb_sprint03, zomb_sprint04, zomb_sprint05, zomb_sprint06, zomb_sprint07, zomb_sprint08, zomb_sprint09]

# Taunts
zomb_taunt00 = "data/sounds/zombie/zomb_taunts/taunt00.wav"
zomb_taunt01 = "data/sounds/zombie/zomb_taunts/taunt01.wav"
zomb_taunt02 = "data/sounds/zombie/zomb_taunts/taunt02.wav"
zomb_taunt03 = "data/sounds/zombie/zomb_taunts/taunt03.wav"
zomb_taunt04 = "data/sounds/zombie/zomb_taunts/taunt04.wav"
zomb_taunt05 = "data/sounds/zombie/zomb_taunts/taunt05.wav"
zomb_taunt06 = "data/sounds/zombie/zomb_taunts/taunt06.wav"

zomb_taunt = [zomb_taunt00, zomb_taunt01, zomb_taunt02, zomb_taunt03, zomb_taunt04, zomb_taunt05, zomb_taunt06]

# Gun Sounds
gun_1911 = "data/sounds/1911.wav"

# Start Game Sounds
kino_start = "data/sounds/kino_start.wav"
tranzit_start = "data/sounds/tranzit_start.wav"

# End Game Sounds
de_game_over = "data/sounds/game_over/de_game_over.wav"
motd_game_over = "data/sounds/game_over/motd.wav"
motd_game_over_special = "data/sounds/game_over/motd_special.wav"
soe_game_over = "data/sounds/game_over/soe.wav"
nacht_game_over = "data/sounds/game_over/nacht.wav"

game_over_sounds = [de_game_over, motd_game_over, motd_game_over_special, soe_game_over, nacht_game_over]  

def play_sound(file):
    pygame.mixer.Sound(file).play()


def gamestart_sound():
    
    if random.randint(0, 1) == 0:
        #start_game.play()
        return kino_start
    else:
        #tranzit_start.play()
        return tranzit_start

# def game_over_sound():

#     if random.randint(0, 6) == 0:
#         #motd_end.play()
#         return motd_end
#     elif random.randint(0, 6) == 1:
#         #motd_end_special.play()
#         return motd_end_special
#     elif random.randint(0, 6) == 2:
#         #soe_end.play()
#         return soe_end
#     else:
#         #nacht_end.play()
#         return nacht_end


def random_zomb_sound(sound_list):
    return random.choice(sound_list)




def play_random_zomb_sound(sound_list):
    sound_file = random.choice(sound_list)
    pygame.mixer.Sound(sound_file).play()



