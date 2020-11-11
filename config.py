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
		self.screen_height = 600
		self.screen_width = 400

		# configurações dos blocos
		self.cube_size_coef = 1/16	# fração da largura da tela


