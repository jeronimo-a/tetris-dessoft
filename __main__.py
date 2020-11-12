'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import sys
import pygame
from config import Config
from block import Block

# roda o jogo
def run():

	# construção das configurações
	SETTINGS = Config()

	# inicialização do pygame
	pygame.init()

	# criação da janela do jogo e configuração do título
	SCREEN = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
	pygame.display.set_caption('TETRIS')

	# define uns blocos para teste
	block1 = Block(SCREEN, SETTINGS, [0, 1, 2, 0], [225, 225, 50])
	block2 = Block(SCREEN, SETTINGS, [0, 3, 0, 0], [255, 125, 125])
	block2.centery -= 2 * SETTINGS.cube_size_coef * SETTINGS.screen_width

	# loop principal de jogo
	while True:

		# observa eventos
		for event in pygame.event.get():

			# evento de fechamento
			if event.type == pygame.QUIT: sys.exit()

		# redesenha o plano de fundo e o bloco
		SCREEN.fill(SETTINGS.bg_color)
		block1.draw()
		block2.draw()

		# redesenha a tela
		pygame.display.flip()


run()

			





