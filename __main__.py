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

	# bloco de jogo
	DEMO_BLOCK = make_random_block(SCREEN, SETTINGS)

	# cubos dos blocos já depositados
	CUBES = list()

	# posições máximas em função de x
	MAXIMUMY = get_starting_maximumy(SETTINGS)

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
			
			# definição dos textos
			font = pygame.font.SysFont(None, 72)
			text = font.render('TETRIS', True, (255, 255, 255))
			font2 = pygame.font.SysFont(None, 36)
			text2 = font2.render('Next Block', True, (255, 255, 255))

			# insere os textos na tela de jogo
			text_width = SETTINGS.screen_width/2 - text.get_width()/2
			text_height = SETTINGS.screen_height/24
			SCREEN.blit(text, (text_width, text_height))
			SCREEN.blit(text2, (530, 300))

			# criação do bloco novo caso necessário
			if spawn:
				new_block = make_random_block(SCREEN, SETTINGS)
				MAIN_BLOCK = DEMO_BLOCK
				DEMO_BLOCK = new_block
				MAIN_BLOCK.spawn()
				spawn = False

			# colisões e consequências
			for xpos in MAIN_BLOCK.maximumy.keys():
				if MAIN_BLOCK.maximumy[xpos] >= SETTINGS.screen_height:
					spawn = True
					CUBES += MAIN_BLOCK.cubes

			# atualização da posição do bloco ativo
			if not spawn: MAIN_BLOCK.virtualy += SETTINGS.block_speed

			# atualiza as propriedades do bloco principal
			MAIN_BLOCK.update()

			# desenha os blocos na tela
			MAIN_BLOCK.draw()
			DEMO_BLOCK.draw()

			# desenha os cubos estáticos
			for cube in CUBES: cube.draw()

			# constrói e desenha o grid
			grid_builder(SCREEN, SETTINGS)

		# tela de fim de jogo
		elif STATE == 2: pass

		# observa eventos
		for event in pygame.event.get():

			if event.type == pygame.QUIT: sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE and STATE == 0: STATE = 1
				elif event.key == pygame.K_DOWN and STATE == 1: MAIN_BLOCK.rotate('left')
				elif event.key == pygame.K_UP and STATE == 1: MAIN_BLOCK.rotate('right')
				elif event.key == pygame.K_LEFT and STATE == 1: MAIN_BLOCK.centerx -= MAIN_BLOCK.cube_size
				elif event.key == pygame.K_RIGHT and STATE == 1: MAIN_BLOCK.centerx += MAIN_BLOCK.cube_size

		# redesenha a tela
		pygame.display.flip()

run()

			





