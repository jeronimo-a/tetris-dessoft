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
		self.block_preview_pos = [3/4, 1/4]		# fração do tamanho da tela (posição de amostragem do próximo bloco)
		self.block_spawn_pos = [1/2, 24]		# [fraçao da arena, altura em relacao ao chão da arena (blocos)]
		self.block_speed = 1/6


