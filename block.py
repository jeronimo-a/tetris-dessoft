'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo que descreve os blocos do tetris

'''

import pygame

class Bloco(pygame.sprite.Sprite):
	''' descreve os blocos do tetris
		todo bloco é um conjunto de cubos '''

	def __init__(self, config, shape):
		''' cria um único novo bloco, todo os blocos têm um cubo de origem
			a partir do qual são adicionados novos cubos a partir de "shape"
			que é uma tupla de quatro inteiros de formato:

			shape = (cima, direita, baixo, esquerda)

			onde cima é a quantidade de blocos acima do bloco origem e etc. '''

		# amarra os argumentos específicos à self
		self.config = config
		self.shape = shape







