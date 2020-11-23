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

			# definição e inserção dos textos
			build_startscreen_texts(SCREEN, SETTINGS)

			spawn = True

		# tela de jogo
		elif STATE == 1:

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

			# definição e inserção dos textos
			build_gamescreen_texts(SCREEN, SETTINGS)

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

			





