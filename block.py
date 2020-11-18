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

	direction_map = ((0,-1),(1,0),(0,1),(-1,0))

	def __init__(self, screen, config, shape, color, odd=False):
		''' cria um único novo bloco, todo os blocos têm um cubo de origem
			a partir do qual são adicionados novos cubos, dependendo de "shape"
			que é uma lista de quatro inteiros de formato:

			shape = [cima, direita, baixo, esquerda]

			onde "cima" é a quantidade de blocos acima do bloco origem e etc. '''

		# amarra os argumentos específicos à self
		self.screen = screen 	# surface na qual ele é desenhado
		self.config = config	# configurações de jogo
		self.shape = shape		# formato do bloco (alterado para rotacioná-lo)
		self.color = color		# cor do bloco
		self.odd = odd			# se o bloco tem dois cubos "origem" (ainda não funciona)

		# propriedades pygame
		self.cubes = list()		# lista dos cubos

		# propriedades de movimento
		self.virtualy = float()		# posição vertical que varia uniformemente (center varia em múltiplos de cube_size) (é a manipulada por fora)

		# propriedades principais de posição
		self.centerx, self.centery = 0, 0			# posição do centro de rotação (centery depende de virtualy) (apenas centerx é manipulado)
		self.deltax, self.deltay = int(), int()		# center + delta = origin
		self.originx, self.originy = int(), int()	# posição do centro do cubo de oridem (para posicionamento na tela)
		self.averagex, self.averagey = int(), int()	# posição média do bloco (usada para posicionamento do próximo bloco)
		self.maximumy = dict()						# posições verticais das faces inferiores do bloco

		# propriedades principais de dimensão
		self.cube_size = int(config.screen_width * config.cube_size_coef)	# tamanho dos lados dos cubos que compõem o bloco
		self.height = int()													# altura do bloco
		self.width = int()													# largura do bloco

		# define height e width a partir de cube_size e shape
		dimensions = self.get_dimensions()
		self.height = dimensions[0]
		self.width = dimensions[1]

		# define os deltas a partir de cube_size, width e height
		deltas = self.get_deltas()
		self.deltax = deltas[0]
		self.deltay = deltas[1]

		# define origin a partir dos deltas e de center
		origin = self.get_origin_from_center()
		self.originx = origin[0]
		self.originy = origin[1]

		# define average a partir de origin e shape
		averages = self.get_average_from_origin()
		self.averagex = averages[0]
		self.averagey = averages[1]

		# variáveis secundárias (usadas para determinar center a partir de average)
		average_deltax = self.averagex - self.centerx
		average_deltay = self.averagey - self.centery

		# define maximumy a partir de originy e shape
		self.maximumy = self.get_maximumy()

		# constrói os objetos Cube
		self.cubes = self.make_cubes()

		# coloca o bloco na posição de amostragem alterando o valor de average
		self.averagex = config.block_preview_pos[0] * config.screen_width
		self.averagey = config.block_preview_pos[1] * config.screen_height

		# atualiza center a partir de average
		self.centerx = self.averagex - average_deltax
		self.centery = self.averagey - average_deltay

		# define virtualy a partir de centery
		self.virtualy = float(self.centery)

		# atualiza as posições e as posições dos cubos
		self.update()


	def __len__(self):
		''' overload da função len, retorna o número de cubos '''
		return sum(self.shape) + 1


	def make_cubes(self):
		''' constrói todos os cubos que compõem o bloco '''

		cubes = list()

		for side in range(len(self)): cubes.append(Cube(self))

		return cubes


	def update(self):
		''' atualiza as posições conforme virtualy e centerx '''

		# atualiza centery a partir de virtualy
		update_centery = (self.virtualy - self.centery) > self.cube_size
		if update_centery: self.centery += self.cube_size

		# atualiza as dimensões
		dimensions = self.get_dimensions()
		self.height = dimensions[0]
		self.width = dimensions[1]

		# atualiza os deltas a partir das dimensões
		deltas = self.get_deltas()
		self.deltax = deltas[0]
		self.deltay = deltas[1]

		# atualiza origin a partir de center e dos deltas
		origin = self.get_origin_from_center()
		self.originx = origin[0]
		self.originy = origin[1]

		# atualiza os valores de maximumy a partir de origin e shape
		self.maximumy = self.get_maximumy()

		# atualiza a posição de cada cubo com base em origin
		count = 1

		self.cubes[0].rect.centerx = self.originx
		self.cubes[0].rect.centery = self.originy

		for side in range(4):

			for multiplier in range(1, self.shape[side] + 1):
				self.cubes[count].rect.centerx = self.originx + multiplier * Block.direction_map[side][0] * self.cube_size
				self.cubes[count].rect.centery = self.originy + multiplier * Block.direction_map[side][1] * self.cube_size
				count += 1


	def get_dimensions(self):
		''' calcula os valores de height e width a partir de cube size e shape '''

		height = self.cube_size * (1 + self.shape[0] + self.shape[2])
		width = self.cube_size * (1 + self.shape[1] + self.shape[3])

		return height, width


	def get_deltas(self):
		''' calcula os valores de delta a partir de cube size, width e height '''

		# define os deltas a partir de cube_size, width e height
		deltax = (self.width - self.cube_size) / 2
		deltay = (self.height - self.cube_size) / 2
		if self.shape[3] < self.shape[1]: deltax *= -1
		if self.shape[0] < self.shape[2]: deltay *= -1

		# verifica a validade dos deltas (ou ambos múltiplos de cube_size, ou nenhum dos dois)
		deltax_multiple = deltax % self.cube_size == 0
		deltay_multiple = deltay % self.cube_size == 0
		if not deltax_multiple: deltax = (deltax // self.cube_size) * self.cube_size
		if not deltay_multiple: deltay = (deltay // self.cube_size) * self.cube_size

		return deltax, deltay


	def get_origin_from_center(self):
		''' calcula origin a partir de center e delta '''

		originx = self.centerx + self.deltax
		originy = self.centery + self.deltay

		return originx, originy


	def get_average_from_origin(self):
		''' calcula a posição média do bloco a partir de origin e shape '''

		sumx, sumy = self.originx, self.originy

		for side in range(4):

			for multiple in range(1, self.shape[side] + 1):
				sumx += self.originx + multiple * Block.direction_map[side][0]
				sumy += self.originy + multiple * Block.direction_map[side][1]

		averagex = round(sumx / len(self))
		averagey = round(sumy / len(self))

		return averagex, averagey


	def get_maximumy(self):
		''' calcula os valores de maximumy a partir de origin e shape '''

		maximumy = dict()

		xpos = round((self.originx - 0.5 * self.cube_size) / self.cube_size)

		maximumy[xpos] = self.originy + self.cube_size * (1.5 + self.shape[2])

		for side in [1,3]:
			for multiplier in range(1, self.shape[side] + 1):
				maximumy[xpos + multiplier * Block.direction_map[side][0]] = self.originy + 0.5 * self.cube_size

		return maximumy


	def draw(self):
		''' desenha todos os cubos em screen '''

		for cube in self.cubes: cube.draw()


	def spawn(self):
		''' transfere o bloco da área de demonstração para a área de jogo '''

		self.centery = int(self.config.screen_height - (self.config.block_spawn_pos[1] + 0.5) * self.cube_size)
		self.virtualy = float(self.centery)

		self.centerx = int(self.config.block_spawn_pos[0] * self.config.screen_width + 0.5 * self.cube_size)

		self.update()


	def rotate(self, direction):
		''' rotaciona o bloco mexendo na ordem dos elementos em shape '''

		if direction == 'right':
			tmp = self.shape.pop()
			self.shape.insert(0, tmp)

		elif direction == 'left':
			tmp = self.shape.pop(0)
			self.shape.append(tmp)

		self.update()








