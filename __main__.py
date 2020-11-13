'''
Projeto final de Design de Software

Grupo: Felipe Schiavinato, Jerônimo Afrange e Sarah Pimenta

Módulo principal

'''

import sys
import pygame
from block import Block
from config import Config
from random import randint

# para teste --- --- ---- ---- -- ---- ----
shapes = []
colors = []
positions = []
for i in range(100):

	shape = [0, 0, 0, 0]
	for _ in range(4):
		if sum(shape) <= 4: shape[randint(0, 3)] += randint(0, 1)
		else: break
	
	shapes.append(shape)

	color = []
	for _ in range(3):
		color.append(randint(0, 255))
	colors.append(color)

	position = []
	position.append(randint(0, 600))
	position.append(randint(0, 400))

	positions.append(position)
# ---- ---- -------- --- -- ------ --- ----

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
	blocks = []
	for i in range(len(shapes)):
		block = Block(SCREEN, SETTINGS, shapes[i], colors[i])
		blocks.append(block)
		block.centerx = positions[i][0]
		block.centery = positions[i][1]


	# loop principal de jogo
	while True:
		#variavel tela de inicio
		screen_start = True 

		#tela de inicio
		if screen_start:
			title_font = pygame.font.SaysFont(None, 48)
			title_text = title_font.render('TETRIS', True, (0,0,255))

		else:

		# observa eventos
		for event in pygame.event.get():

			# evento de fechamento
			if event.type == pygame.QUIT: sys.exit()

		# redesenha o plano de fundo e os blocos
		SCREEN.fill(SETTINGS.bg_color)
		for block in blocks: block.draw()

		# redesenha a tela
		pygame.display.flip()


run()

			





