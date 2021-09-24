'''
Refatoração em Desenvolvimento Colaborativo Ágil 2021.2

Grupo: Giancarlo Ruggiero, Jerônimo Afrange e Maria Eduarda Torres

Classe que lida com eventos de jogo (inputs do usuário)

'''

class EventManager():

	def __init__(self, bitmap, main_block=None):

		self.bitmap = bitmap
		self.main_block = main_block

	def set_main_block(self, main_block): self.main_block = main_block

	def down_down(self): self.main_block.rotate('left', self.bitmap)
	def up_down(self): self.main_block.rotate('right', self.bitmap)

	def left_down(self):
		if self.main_block.canMoveLeft(self.bitmap):
			self.main_block.centerx -= self.main_block.cube_size

	def right_down(self):
		if self.main_block.canMoveRight(self.bitmap):
			self.main_block.centerx += self.main_block.cube_size




