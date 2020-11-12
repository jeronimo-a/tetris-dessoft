'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo que descreve os cubos que compõem os blocos do tetris

'''

import pygame
from pygame.sprite import Sprite


class Cube(Sprite):
	''' descreve os cubos que compõem os blocos '''

	def __init__(self, block, relativex, relativey, color):
		''' cria um único cubo novo '''

		# define a instância pygame.sprite.Sprite
		super(Cube, self).__init__()

		# amarra os argumentos à self
		self.block = block
		self.color = color
		self.relativex = relativex
		self.relativey = relativey

		# rouba propriedades de block
		self.config = self.block.config
		self.screen = self.block.screen
		self.size = self.block.cube_size

		# define o objeto Rect do cubo (propriedade de Sprite)
		self.rect = pygame.Rect(0, 0, block.cube_size, block.cube_size)


	def draw(self):
		''' desenha o cubo na tela '''

		pygame.draw.rect(self.screen, self.color, self.rect)












