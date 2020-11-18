'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import sys
import pygame

from functions import *

from block import Block
from config import Config
from random import randint


# roda o jogo
def run():

	# construção das configurações
	SETTINGS = Config()

	# inicialização do pygame
	pygame.init()

	# criação da janela do jogo e configuração do título
	SCREEN = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
	pygame.display.set_caption('TETRIS')

	# bandeira d estado de jogo (0: tela de início, 1: jogo, 2: fim de jogo)
	STATE = 0

	# blocos
	BLOCKS = [Block(SCREEN, SETTINGS, [1, 2, 0, 0] , [255,125,0])]

	# loop principal de jogo
	while True:

		# impede que STATE fique maior que 2
		STATE %= 3

		# redesenha o plano de fundo e os blocos
		SCREEN.fill(SETTINGS.bg_color)  

		# tela de inicio
		if STATE == 0:

			title_font = pygame.font.SysFont(None, 100)
			title_text = title_font.render('TETRIS', True, (0,0,255))
			title_width = title_text.get_width()
			SCREEN.blit(title_text, (SETTINGS.screen_width/2 - title_width/2, SETTINGS.screen_height/3))

			description_font = pygame.font.SysFont(None, 30)
			description_text = description_font.render('Press SPACE to Start', True, (255,255,0))
			description_width = description_text.get_width()
			SCREEN.blit(description_text, (SETTINGS.screen_width/2 - description_width/2, SETTINGS.screen_height*(1 - 1/3)))

			spawn = True

		# tela de jogo
		elif STATE == 1:

			main_block = BLOCKS[0]

			if spawn: main_block.spawn(); spawn = False

			if main_block.minimuny[main_block.originx] < SETTINGS.screen_height:
				main_block.virtualy += SETTINGS.block_speed

			main_block.update()
			main_block.draw()

		# tela de fim de jogo
		elif STATE == 2: pass

		# observa eventos
		for event in pygame.event.get():

			if event.type == pygame.QUIT: sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE and STATE == 0: STATE = 1
				elif event.key == pygame.K_DOWN and STATE == 1: main_block.rotate('left')
				elif event.key == pygame.K_UP and STATE == 1: main_block.rotate('right')
				elif event.key == pygame.K_LEFT and STATE == 1: main_block.centerx -= main_block.cube_size
				elif event.key == pygame.K_RIGHT and STATE == 1: main_block.centerx += main_block.cube_size

		# redesenha a tela
		pygame.display.flip()


run()

			





