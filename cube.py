'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo que descreve os cubos que compõem os blocos do tetris

'''

import pygame
from pygame.sprite import Sprite


class Cube(Sprite):
	''' descreve os cubos que compõem os blocos '''

	def __init__(self, block, relative_position):
		''' cria um único cubo novo '''

		# define a instância pygame.sprite.Sprite
		super(Cube, self).__init__()

		# amarra parte dos argumentos à self
		self.block = block

		# rouba propriedades de block
		self.config = self.block.config
		self.screen = self.block.screen
		self.size = self.block.cube_size

		# define o objeto Rect do cubo (propriedade de Sprite)
		centerx, centery = relative_position
		self.rect = pygame.Rect(size, size, centerx, centery)






