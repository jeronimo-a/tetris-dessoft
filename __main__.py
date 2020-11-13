'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import sys
import pygame
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


	# loop principal de jogo
	while True:

		# redesenha o plano de fundo e os blocos
		SCREEN.fill(SETTINGS.bg_color) 

		#variavel tela de inicio
		screen_start = True 

		#tela de inicio
		if screen_start:
			title_font = pygame.font.SysFont(None, 100)
			title_text = title_font.render('TETRIS', True, (0,0,255))
			title_width = title_text.get_width()
			SCREEN.blit(title_text, (SETTINGS.screen_width/2 - title_width/2, SETTINGS.screen_height/3))

			description_font = pygame.font.SysFont(None, 30)
			description_text = description_font.render('Press SPACE to Start', True, (255,255,0))
			description_width = description_text.get_width()
			SCREEN.blit(description_text, (SETTINGS.screen_width/2 - description_width/2, SETTINGS.screen_height*(1 - 1/3)))

		# observa eventos
		for event in pygame.event.get():

			# evento de fechamento
			if event.type == pygame.QUIT: sys.exit()


		#for block in blocks: block.draw()

		# redesenha a tela
		pygame.display.flip()


run()

			





