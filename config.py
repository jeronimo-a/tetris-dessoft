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
		self.screen_width = 600
		self.bg_color = (50, 50, 50)

		# configurações dos blocos
		self.cube_size_coef = 1/24				# fração da largura da tela
		self.block_preview_pos = [1/2, 1/2]		# fração do tamanho da tela (posição de amostragem do próximo bloco)


