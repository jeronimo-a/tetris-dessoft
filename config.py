'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo de configurações gerais

'''

class Config():
	''' molde das configurações de jogo '''

	def __init__(self):
		''' cria uma nova instância de configuração '''

		# configurações da janela
		self.screen_height = 700
		self.screen_width = 700
		self.bg_color = (0, 0, 0)

		# configurações dos blocos
		self.cube_size_coef = 3/70				# fração da largura da tela
		self.block_preview_pos = [6/7, 1/4]		# fração do tamanho da tela (posição de amostragem do próximo bloco)
		self.block_spawn_pos = [1/2, 18]		# [fraçao da arena, altura em relacao ao chão da arena (blocos)]
		self.block_speed = 1/4

		# configuração de texto
		self.score_position = [1 - self.block_preview_pos[0], self.block_preview_pos[1]]

		# configurações do grid
		self.grid_width = 10
		self.grid_height = 20
		self.line_thickness = 4
		self.top_border = self.screen_height / 7
		self.left_border = self.screen_width / 3.5
		self.right_border = self.screen_width / 1.4
		self.block_limit = self.grid_height - 5
		self.block_limit_line = self.screen_height - self.block_limit * self.cube_size_coef * self.screen_width

		# formas dos blocos
		self.shapes = [
			[0,2,1,0],
			[1,2,0,0],
			[0,1,0,2],
			[0,2,0,1],
			[0,1,0,1],
			[0,1,0,1],
			[1,1,0,0],
			[0,0,1,1]
		]






