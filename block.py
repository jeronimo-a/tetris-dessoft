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

		# propriedade de utilidade
		self.is_dead = False

		# propriedades de movimento
		self.virtualy = float()		# posição vertical que varia uniformemente (center varia em múltiplos de cube_size) (é a manipulada por fora)
		self.ylocked = False		# caso True, o bloco não é atualizada a posição y do bloco

		# propriedades principais de posição
		self.centerx, self.centery = 0, 0			# posição do centro de rotação (centery depende de virtualy) (apenas centerx é manipulado)
		self.deltax, self.deltay = int(), int()		# center + delta = origin
		self.originx, self.originy = int(), int()	# posição do centro do cubo de oridem (para posicionamento na tela)
		self.averagex, self.averagey = int(), int()	# posição média do bloco (usada para posicionamento do próximo bloco)
		self.grid_positions = list()				# posições de todos os cubos no grid

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

		# constrói os objetos Cube
		self.cubes = self.make_cubes()

		# constrói a lista de posições grid
		for _ in self.cubes: self.grid_positions.append([0,0])

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
		self.is_dead = (self.virtualy - self.centery) > 2 * self.cube_size
		update_centery = (self.virtualy - self.centery) > self.cube_size
		if update_centery and not self.ylocked: self.centery += self.cube_size

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

		# atualiza a posição do bloco de origem no grid
		gridx = int((self.originx - self.config.left_border) / self.cube_size)
		gridy = int((self.originy - self.config.top_border) / self.cube_size)
		self.grid_positions[0] = [gridx, gridy]

		# atualiza a posição de cada cubo com base em origin
		count = 1

		self.cubes[0].rect.centerx = self.originx
		self.cubes[0].rect.centery = self.originy

		for side in range(4):

			for multiplier in range(1, self.shape[side] + 1):
				grid_deltax = multiplier * Block.direction_map[side][0]
				grid_deltay = multiplier * Block.direction_map[side][1]
				self.grid_positions[count][0] = gridx + grid_deltax
				self.grid_positions[count][1] = gridy + grid_deltay
				self.cubes[count].rect.centerx = self.originx + grid_deltax * self.cube_size
				self.cubes[count].rect.centery = self.originy + grid_deltay * self.cube_size
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


	def draw(self):
		''' desenha todos os cubos em screen '''

		for cube in self.cubes: cube.draw()


	def spawn(self):
		''' transfere o bloco da área de demonstração para a área de jogo '''

		self.centery = int(self.config.screen_height - (self.config.block_spawn_pos[1] + 0.5) * self.cube_size)
		self.virtualy = float(self.centery)

		self.centerx = int(self.config.block_spawn_pos[0] * self.config.screen_width + 0.5 * self.cube_size)

		self.update()


	def rotate(self, direction, bitmap):
		''' rotaciona o bloco mexendo na ordem dos elementos em shape '''

		if direction == 'right':
			tmp = self.shape.pop()
			self.shape.insert(0, tmp)
			self.update()
			if self.overlapping(bitmap):
				self.rotate('left', bitmap)

		elif direction == 'left':
			tmp = self.shape.pop(0)
			self.shape.append(tmp)
			self.update()
			if self.overlapping(bitmap):
				self.rotate('right', bitmap)


	def canMoveDown(self, bitmap):
		''' retorna um bool a partir da posição do bloco e do bitmap do grid '''

		if self.getMaximumGridY() == self.config.grid_height - 1: return False

		for grid_pos in self.grid_positions:
			blocked = bitmap[grid_pos[1] + 1][grid_pos[0]]
			if blocked: return False

		return True


	def canMoveLeft(self, bitmap):
		''' retorna um bool a partir da posição do bloco e do bitmap do grid '''

		if self.getMinimumGridX() <= 0: return False

		for grid_pos in self.grid_positions:
			blocked = bitmap[grid_pos[1]][grid_pos[0] - 1]
			if blocked: return False

		return True


	def canMoveRight(self, bitmap):
		''' retorna um bool a partir da posição do bloco e do bitmap do grid '''

		if self.getMaximumGridX() >= self.config.grid_width - 1: return False

		for grid_pos in self.grid_positions:
			blocked = bitmap[grid_pos[1]][grid_pos[0] + 1]
			if blocked: return False

		return True


	def getMinimumGridX(self):
		''' retorna a posição x no grid mínima do bloco '''

		minimumx = self.grid_positions[0][0]

		for grid_pos in self.grid_positions[1:]:
			if grid_pos[0] < minimumx: minimumx = grid_pos[0]

		return minimumx


	def getMaximumGridX(self):
		''' retorna a posição x no grid mínima do bloco '''

		maximux = self.grid_positions[0][0]

		for grid_pos in self.grid_positions[1:]:
			if grid_pos[0] > maximux: maximux = grid_pos[0]

		return maximux


	def getMaximumGridY(self):
		''' retorna a posição x no grid mínima do bloco '''

		maximumy = self.grid_positions[0][1]

		for grid_pos in self.grid_positions[1:]:
			if grid_pos[1] > maximumy: maximumy = grid_pos[1]

		return maximumy


	def overlapping(self, bitmap):
		''' verifica se um bloco está na mesma posição que outro '''

		for grid_pos in self.grid_positions:

			try: overlap = bitmap[grid_pos[1]][grid_pos[0]]
			except: continue

			if overlap: return True

		return  False








