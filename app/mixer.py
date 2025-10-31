# from app.sound import *
# import os
# import pygame


# class Mixer: 
    
#     def __init__(self):
#         self.queue = []
#         os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
#         pygame.init()

#     def play(self, file = "", fade = 0):
#         # if fade > 0:
#         #     pygame.mixer.fadeout(fade)

#         self.queue.append(file)

#     def listen(self):
#         while True:
#             for file in self.queue:
#                 pygame.mixer.Sound(file).play()
#                 self.queue.remove(file)

