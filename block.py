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

	# propriedade estática de auxílio na hora de criação dos cubos adjacentes
	direction_map = ((0,-1), (1,0), (0,1), (-1,0))

	def __init__(self, screen, config, shape, color):
		''' cria um único novo bloco, todo os blocos têm um cubo de origem
			a partir do qual são adicionados novos cubos a partir de "shape"
			que é uma tupla de quatro inteiros de formato:

			shape = (cima, direita, baixo, esquerda)

			onde "cima" é a quantidade de blocos acima do bloco origem e etc. '''

		# amarra os argumentos específicos à self
		self.screen = screen
		self.config = config
		self.shape = shape
		self.color = color

		# calcula o tamanho dos lados do cubo
		self.cube_size = round(config.screen_width * config.cube_size_coef)

		# define a posição absoluta
		self._centerx = self.config.block_preview_pos[0] * config.screen_width
		self._centery = self.config.block_preview_pos[1] * config.screen_height

		# cria os cubos
		self.cubes = self.define_cubes()

		# define a posição média dos cubos em relação ao cubo de origem
		self.averagex, self.averagey = self.relative_average_position()

		# define a posição do cubo origem
		self._originx = self._centerx - self.averagex
		self._originy = self._centery - self.averagey

		# atualiza as posições dos cubos
		self.update_position(0)
		self.update_position(1)


	def set_centerx(self, value):
		''' atualiza o valor de self.originx e as posições dos cubos ao modificar self.centerx '''

		self._centerx = value

		self.originx = self._centerx - self.averagex
		self.update_position(0)

	def set_centery(self, value):
		''' atualiza o valor de self.originy e as posições dos cubos ao modificar self.centery '''

		self._centery = value

		self.originy = self._centery - self.averagey
		self.update_position(1)

	def get_centerx(self): return self._centerx
	def get_centery(self): return self._centery

	# define centery e centerx
	centerx = property(get_centerx, set_centerx)
	centery = property(get_centery, set_centery)


	def set_originx(self, value):
		''' atualiza o valor de self._centerx e as posições dos cubos ao modificar self.originx '''

		self._originx = value

		self._centerx = self._originx + self.averagex
		self.update_position(0)

	def set_originy(self, value):
		''' atualiza o valor de self._centery e as posições dos cubos ao modificar self.originy '''

		self._originy = value

		self._centery = self._originy + self.averagey
		self.update_position(1)

	def get_originx(self): return self._originx
	def get_originy(self): return self._originy

	# define centery e centerx
	originx = property(get_originx, set_originx)
	originy = property(get_originy, set_originy)


	def update_position(self, component):
		''' atualiza as posições absolutas de todos os cubos com base em originx e originy '''

		# loop de atualização
		for cube in self.cubes:

			# para x
			if component == 0: cube.rect.centerx = self.originx + cube.relativex
			# para y
			elif component == 1: cube.rect.centery = self.originy + cube.relativey


	def define_cubes(self):
		''' define os cubos integrantes do bloco '''

		# define a lista de cubos
		cubes = set()

		# coleta de propriedades (por clareza do código)
		shape = self.shape
		color = self.color
		screen = self.screen
		cube_size = self.cube_size

		# cria o cubo de origem
		origin = Cube(self, 0, 0, color)
		cubes.add(origin)

		# loop de criação dos cubos adjacentes, lado por lado
		for side in range(4):

			# loop de cada cubo na direção específica
			for multiplier in range(shape[side]):

				# calcula a distância em pixels
				multiplier += 1
				distance = cube_size * multiplier

				# multiplica a componente certa por 1 ou -1 e a outra por 0
				relativex = distance * Block.direction_map[side][0]
				relativey = distance * Block.direction_map[side][1]

				# cria o cubo
				new_cube = Cube(self, relativex, relativey, color)

				# adiciona-o à lista de cubos
				cubes.add(new_cube)

		# retorna a lista de cubos
		return cubes


	def relative_average_position(self):
		''' retorna a posição média do bloco relativa à origem '''

		# variáveis de adição das posições x e y
		sumx = 0
		sumy = 0

		# loop de incrementação (soma)
		for cube in self.cubes:
			sumx += cube.rect.centerx
			sumy += cube.rect.centery

		# divisão das somas
		averagex = sumx / (len(self))
		averagey = sumy / (len(self))

		# retorna os valores
		return averagex, averagey


	def __len__(self):
		''' overload da função len, retorna o número de cubos '''

		return len(self.cubes) + 1


	def draw(self):
		''' desenha o bloco na tela '''

		# coleta das propriedades (por clareza do código)
		originx = self.originx
		originy = self.originy
		screen = self.screen
		cubes = self.cubes

		# loop de desenho
		for cube in cubes:
			print(cube.rect.center)
			cube.draw()

		print()

			
















