'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import pygame
from config import Config
from block import Block

# construção das configurações
SETTINGS = Config()

# inicialização do pygame
pygame.init()

# criação da janela do jogo e configuração do título
SCREEN = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
pygame.display.set_caption('TETRIS')

# bandeira do loop principal do programa
ACTIVE = True

# estado do programa (0 para tela de início, 1 para jogo, 2 para fim de jogo)
STATE = 0

# loop principal de jogo
while ACTIVE:

	# tela de início
	if STATE == 0:

		# definindo título
		title_font = pygame.font.SysFont('arial', 48, bold=True)
		tilte_text = font.render('TETRIS', True, (0,0,255))





