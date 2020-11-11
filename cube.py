'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo que descreve os cubos que compõem os blocos do tetris

'''

import pygame
from pygame.sprite import Sprite


class Cube(Sprite):
	''' descreve os cubos que compõem os blocos '''

	def __init__(self, screen, config, block, relative_position):
		''' cria um único cubo novo '''

		# define a instância pygame.sprite.Sprite
		super(Cube, self).__init__()

		# amarra parte dos argumentos à self
		self.screen = screen
		self.config = config
		self.block = block

		# define o objeto Rect do cubo (propriedade de Sprite)
		centerx, centery = relative_position
		self.rect = pygame.Rect(cube_size, cube_size, centerx, centery)






