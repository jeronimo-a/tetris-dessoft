import pygame

#Seting up pygame
pygame.init()

#Window variables
win_width = 400
win_height = 600

#Seting up window
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('TETRIS')

#Starting data structure
game = True

#Writing Title
title_font = pygame.font.SysFont('arial', 48, bold=True)
tilte_text = font.render('TETRIS', True, (0,0,255))