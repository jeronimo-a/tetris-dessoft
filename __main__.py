'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import os
import sys
import json
import pygame

from functions import *

from block import Block
from config import Config
from random import randint

# roda o jogo
def run():

	with open('highscore.json') as json_file:
		DATA = json.load(json_file)

	try: HIGHSCORE = int(DATA['highscore'])
	except:
		print('here')
		DATA['highscore'] = 0
		HIGHSCORE = DATA['highscore']

	# construção das configurações
	SETTINGS = Config()

	# inicialização do pygame
	pygame.init()

	# criação da janela do jogo e configuração do título
	SCREEN = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
	pygame.display.set_caption('TETRIS')

	# bandeira d estado de jogo (0: tela de início, 1: jogo, 2: fim de jogo)
	STATE = 0

	# pontuação da rodada
	SCORE = 0

	# bloco de jogo
	DEMO_BLOCK = make_random_block(SCREEN, SETTINGS)

	# bitmap das posições do grid ocupadas (guarda os cubes dos blocos já depositados no fundo)
	BITMAP = build_bitmap(SETTINGS)

	# posições máximas em função de x
	MAXIMUMY = get_starting_maximumy(SETTINGS)

	# loop principal de jogo
	while True:

		quitting = False

		# impede que STATE fique maior que 2
		STATE %= 3

		# redesenha o plano de fundo e os blocos
		SCREEN.fill(SETTINGS.bg_color)  

		# tela de inicio
		if STATE == 0:

			# definição e inserção dos textos
			build_startscreen_texts(SCREEN, SETTINGS, HIGHSCORE)

			spawn = True


			new_game = False

		# tela de jogo
		elif STATE == 1:
			
			if new_game:
				SCORE = 0
				DEMO_BLOCK = make_random_block(SCREEN, SETTINGS)
				BITMAP = build_bitmap(SETTINGS)
				new_game = False 

			# definição e inserção dos textos
			build_gamescreen_texts(SCREEN, SETTINGS, SCORE)

			# criação do bloco novo caso necessário
			if spawn:
				new_block = make_random_block(SCREEN, SETTINGS)
				MAIN_BLOCK = DEMO_BLOCK
				DEMO_BLOCK = new_block
				MAIN_BLOCK.spawn()
				spawn = False

			# colisões e consequências
			if not MAIN_BLOCK.canMoveDown(BITMAP):
				MAIN_BLOCK.ylocked = True

			# possibilita a retomagem do movimento caso seja possível
			if MAIN_BLOCK.canMoveDown(BITMAP) and MAIN_BLOCK.ylocked:
				MAIN_BLOCK.ylocked = False

			# verifica se o bloco ainda está vivo
			if MAIN_BLOCK.is_dead: spawn = True

			# atualização da posição do bloco ativo
			if not spawn: MAIN_BLOCK.virtualy += SETTINGS.block_speed * (SCORE + 300) / 300

			# atualiza as propriedades do bloco
			MAIN_BLOCK.update()

			# adição dos cubos do bloco ativo à lista dos cubos, alteração do bitmap e verificação de pontuação/fim de jogo
			if spawn:

				# adiciona os cubos do bloco ao bitmap
				count = 0
				for grid_pos in MAIN_BLOCK.grid_positions:
					BITMAP[grid_pos[1]][grid_pos[0]] = MAIN_BLOCK.cubes[count]
					count += 1

				# verifica se há linhas completas
				complete_lines = list()
				count = 0
				for line in BITMAP:
					if all(line): complete_lines.append(count)
					count += 1

				# remove as linhas completas
				for line in complete_lines:
					BITMAP[line] = [False] * SETTINGS.grid_width
					new_line = BITMAP.pop(line)
					BITMAP.insert(0, new_line)

				# atualiza a posição dos cubos
				empty = True
				for line in range(len(BITMAP)):
					for col in range(len(BITMAP[line])):
						cube = BITMAP[line][col]
						if not cube: continue
						empty = False
						cube.grid_pos = [col, line]
						cube.update()

				# verifica se houve game over
				game_over = any(BITMAP[SETTINGS.grid_height - SETTINGS.block_limit - 1])
				if game_over: STATE = 2
				else:
					SCORE += int(len(MAIN_BLOCK.cubes) * (SCORE + 300) / 300)
					SCORE += int(len(complete_lines) ** 2 * 10 * (SCORE + 300) / 300)
					if empty: SCORE = int(SCORE * 1.1 * (SCORE + 300) / 300)

			# desenha os blocos na tela
			MAIN_BLOCK.draw()
			DEMO_BLOCK.draw()

			# desenha os cubos estáticos
			for line in BITMAP:
				for cube in line:
					if cube: cube.draw()

			# constrói e desenha o grid
			grid_builder(SCREEN, SETTINGS)

		# tela de fim de jogo
		elif STATE == 2:

			if SCORE > HIGHSCORE:
				DATA['highscore'] = SCORE
				HIGHSCORE = SCORE

			build_gameoverscreen_texts(SCREEN, SETTINGS, HIGHSCORE)



		# observa eventos
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				quitting = True
				break

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE and STATE == 0: STATE = 1
				if event.key == pygame.K_SPACE and STATE == 2: STATE = 1; new_game = True 
				elif event.key == pygame.K_DOWN and STATE == 1: MAIN_BLOCK.rotate('left', BITMAP)
				elif event.key == pygame.K_UP and STATE == 1: MAIN_BLOCK.rotate('right', BITMAP)
				elif event.key == pygame.K_LEFT and STATE == 1 and MAIN_BLOCK.canMoveLeft(BITMAP): MAIN_BLOCK.centerx -= MAIN_BLOCK.cube_size
				elif event.key == pygame.K_RIGHT and STATE == 1 and MAIN_BLOCK.canMoveRight(BITMAP): MAIN_BLOCK.centerx += MAIN_BLOCK.cube_size

		# redesenha a tela
		pygame.display.flip()

		if quitting: break

	with open('highscore.json','w') as json_file:
		json.dump(DATA, json_file)

run()

			





