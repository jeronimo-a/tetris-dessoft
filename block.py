'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo que descreve os blocos do tetris e os cubos que os compõem

'''

import pygame
from pygame.sprite import Sprite
from cube import Cube


class Block():
	''' descreve os blocos do tetris
		todo bloco é um conjunto de cubos '''

	# propriedade estática de auxílio na hora de criação dos cubos extras
	direction_map = ((1,0), (0,1), (-1,0), (0,-1))

	def __init__(self, screen, config, shape):
		''' cria um único novo bloco, todo os blocos têm um cubo de origem
			a partir do qual são adicionados novos cubos a partir de "shape"
			que é uma tupla de quatro inteiros de formato:

			shape = (cima, direita, baixo, esquerda)

			onde "cima" é a quantidade de blocos acima do bloco origem e etc. '''

		# amarra os argumentos específicos à self
		self.screen = screen
		self.config = config
		self.shape = shape

		# calcula o tamanho dos lados do cubo
		self.cube_size = config.screen_width * config.cube_size_coef

		# renome a posição de origem
		self.centerx = self.config.block_preview_pos[0]
		self.centery = self.configblock_preview_pos[1]

		# cria os cubos adjacentes
		self.origin_cube, self.side_cubes = self.define_cubes()


	def define_cubes(self):
		''' define os cubos integrantes do bloco '''

		# define a lista de cubos
		cubes = list()

		# cria o cubo de origem
		centerx, centery = self.config.block_preview_pos
		origin = Cube(self.screen, self.cube_size, [0, 0])

		# loop de criação dos cubos adjacentes, lado por lado
		for side in range(4):

			# loop de cada cubo na direção específica
			for multiplier in range(self.shape[side]):

				# calcula a distância em pixels
				multiplier += 1
				distance = self.cube_size * multiplier

				# multiplica a componente certa por 1 ou -1 e a outra por 0
				relativex = distance * Block.direction_map[side][0]
				relativey = distance * Block.direction_map[side][1]

				# cria o cubo
				new_cube = Cube(self, relativex, relativey)

				# adiciona-o à lista de cubos
				cubes.append(new_cube)

		# retorna a lista de cubos
		return origin, cubes

















