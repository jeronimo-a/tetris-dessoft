'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo de funções utilizadas recorrentemente

'''

import sys
import pygame

from random import randint
from block import Block

def make_random_block(screen, config):
	''' faz um bloco com características aleatórias '''

	color = (randint(0,255), randint(0,255), randint(0,255))
	shape = [0, 0, 0, 0]

	while sum(shape) < 5 and max(shape) < 2:

		shape[randint(0,3)] += randint(0,1)

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

	pygame.draw.line(screen, (255,0,0), (config.left_border, config.screen_height), (config.left_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.right_border, config.screen_height), (config.right_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.left_border, config.top_border), (config.right_border, config.top_border), config.line_thickness)
	pygame.draw.line(screen, (255,0,0), (config.left_border, config.screen_height), (config.right_border, config.screen_height), config.line_thickness)


def build_gamescreen_texts(screen, config):

	# definição dos textos
	font = pygame.font.SysFont(None, 72)
	text = font.render('TETRIS', True, (255, 255, 255))
	font2 = pygame.font.SysFont(None, 36)
	text2 = font2.render('Next Block', True, (255, 255, 255))

	# insere os textos na tela de jogo
	text_width = config.screen_width/2 - text.get_width()/2
	text_height = config.screen_height/24
	screen.blit(text, (text_width, text_height))
	screen.blit(text2, (config.screen_width * config.block_preview_pos[0] - text2.get_width()/2, config.screen_width * config.block_preview_pos[1] * 4/3))


def build_startscreen_texts(screen, config):

	title_font = pygame.font.SysFont(None, 200)
	title_text = title_font.render('TETRIS', True, (255,255,255))
	title_width = title_text.get_width()
	screen.blit(title_text, (config.screen_width/2 - title_width/2, config.screen_height/3))

	description_font = pygame.font.SysFont(None, 50)
	description_text = description_font.render('Press SPACE to Start', True, (255,255,255))
	description_width = description_text.get_width()
	screen.blit(description_text, (config.screen_width/2 - description_width/2, config.screen_height*(1 - 1/3)))





