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





