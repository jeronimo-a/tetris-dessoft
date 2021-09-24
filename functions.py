'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo de funções utilizadas recorrentemente

Refatoração em Desenvolvimento Colaborativo Ágil 2021.2

Grupo: Giancarlo Ruggiero, Jerônimo Afrange e Maria Eduarda Torres

'''

import sys
import pygame

from random import randint, choice
from block import Block

def make_random_block(screen, config):
	''' faz um bloco com características aleatórias '''

	r, g, b = 0, 0, 0

	while sum([r,g,b]) < 255:
		r, g, b = randint(0,255), randint(0,255), randint(0,255)

	color = (r, g, b)
	
	shape = choice(config.shapes)

	block = Block(screen, config, shape, color)

	return block


def get_starting_maximumy(config):
	''' define o dicionário dos valores máximos de y iniciais '''

	maximumy = dict()
	blocks = round(1 / config.cube_size_coef)
	cube_size = round(config.screen_width * config.cube_size_coef)

	for xpos in range(blocks): maximumy[xpos] = config.screen_height

	return maximumy


def grid_builder(screen, config):

	block_size = (config.right_border - config.left_border) / 10
	v = 1

	y = block_size
	while y <= config.screen_height * 6/7:
		pygame.draw.line(screen, (200,200,200), (config.left_border, config.top_border + y), (config.right_border, config.top_border + y), v)
		y += block_size

	z = block_size
	while z <= config.screen_width * 3/7:
		pygame.draw.line(screen, (200,200,200), (config.left_border + z, config.screen_height), (config.left_border + z, config.top_border), v)
		z += block_size

	pygame.draw.line(screen, (0,0,255), (config.left_border, config.block_limit_line), (config.right_border, config.block_limit_line), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.left_border, config.screen_height), (config.left_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.right_border, config.screen_height), (config.right_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.left_border, config.top_border), (config.right_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.left_border, config.screen_height), (config.right_border, config.screen_height), config.line_thickness)


def build_gamescreen_texts(screen, config, score):

	# definição dos textos
	font = pygame.font.SysFont(None, 72)
	text = font.render('TETRIS', True, (255, 255, 255))
	font2 = pygame.font.SysFont(None, 36)
	text2 = font2.render('Próximo bloco', True, (255, 255, 255))
	text3 = font2.render('Pontuação', True, (255, 255, 255))
	text4 = font2.render(str(score), True, (255, 255, 255))

	# insere os textos na tela de jogo
	text_width = config.screen_width/2 - text.get_width()/2
	text_height = config.screen_height/24
	screen.blit(text, (text_width, text_height))
	screen.blit(text2, (config.screen_width * config.block_preview_pos[0] - text2.get_width()/2, config.screen_height * config.block_preview_pos[1] * 4/3))
	screen.blit(text3, (config.screen_width * config.score_position[0] - text3.get_width()/2, config.screen_height * config.score_position[1] * 4/3))
	screen.blit(text4, (config.screen_width * config.score_position[0] - text4.get_width()/2, config.screen_height * config.score_position[1] * 4/3 + text3.get_height()))


def build_startscreen_texts(screen, config, highscore):

	title_font = pygame.font.SysFont(None, 200)
	title_text = title_font.render('TETRIS', True, (255,255,255))
	title_width = title_text.get_width()
	screen.blit(title_text, (config.screen_width/2 - title_width/2, config.screen_height/3))

	description_font = pygame.font.SysFont(None, 50)
	description_text = description_font.render('Aperte ESPAÇO para Jogar', True, (255,255,255))
	description_width = description_text.get_width()
	screen.blit(description_text, (config.screen_width/2 - description_width/2, config.screen_height * (1 - 1/3)))

	highscore_font = description_font
	highscore_text = highscore_font.render('Recorde:', True, (255,255,255))
	score_text = highscore_font.render(str(highscore), True, (255,255,255))
	highscore_width = highscore_text.get_width()
	highscore_height = highscore_text.get_height()
	score_width = score_text.get_width()
	screen.blit(highscore_text, (config.screen_width/2 - highscore_width/2, config.screen_height * (1 - 1/5)))
	screen.blit(score_text, (config.screen_width/2 - score_width/2, config.screen_height * (1 - 1/5) + highscore_height))


def build_bitmap(settings):
	''' constrói uma lista de listas que representa a matrix do grid '''

	bitmap = list()

	for _ in range(settings.grid_height):
		line = list()

		for _ in range(settings.grid_width):
			line.append(False)

		bitmap.append(line)

	return bitmap

def build_gameoverscreen_texts(screen, config, highscore):
    	
		font = pygame.font.SysFont(None, 72)
		description_font = pygame.font.SysFont(None, 36)
		text = font.render('Game Over', True, (255, 255, 255))
		font = pygame.font.SysFont(None, 36)
		text2 = font.render('Aperte ESPAÇO para reiniciar', True, (255, 255, 255))

		text_width = config.screen_width/2 - text.get_width()/2
		text2_width = config.screen_width/2 - text2.get_width()/2
		text_height = config.screen_height/4
		screen.blit(text, (text_width, text_height))
		screen.blit(text2, (text2_width, config.screen_height/2))

		description_font = pygame.font.SysFont(None, 50)
		highscore_font = description_font
		highscore_text = highscore_font.render('Recorde:', True, (255,255,255))
		score_text = highscore_font.render(str(highscore), True, (255,255,255))
		highscore_width = highscore_text.get_width()
		highscore_height = highscore_text.get_height()
		score_width = score_text.get_width()
		screen.blit(highscore_text, (config.screen_width/2 - highscore_width/2, config.screen_height * (1 - 1/5)))
		screen.blit(score_text, (config.screen_width/2 - score_width/2, config.screen_height * (1 - 1/5) + highscore_height))


def catch_events(event_manager, state, new_game):

	for event in pygame.event.get():

		if event.type == pygame.QUIT: return True, state, new_game

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_SPACE and state == 0: state = 1
			if event.key == pygame.K_SPACE and state == 2: state = 1; new_game = True 
			elif event.key == pygame.K_DOWN and state == 1: event_manager.down_down()
			elif event.key == pygame.K_UP and state == 1: event_manager.up_down()
			elif event.key == pygame.K_LEFT and state == 1: event_manager.left_down()
			elif event.key == pygame.K_RIGHT and state == 1: event_manager.right_down()

	return False, state, new_game





