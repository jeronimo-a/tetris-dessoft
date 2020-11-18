# ===== Inicialização =====
# ----- Importa e inicia pacotes
import os
import sys
import pygame
def main():
    pygame.init()

    WIDTH = 700
    HEIGHT = 700

    # ----- Gera tela principal
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tela de Jogo")

    # ----- Inicia estruturas de dados
    game = True

    # ----- Inicia assets
    font = pygame.font.SysFont(None, 72)
    text = font.render('TETRIS', True, (255, 255, 255))
    font2 = pygame.font.SysFont(None, 36)
    text2 = font2.render('Next Shape', True, (255, 255, 255))

    def grid_builder(x):
        y = x
        while y<=600:
            pygame.draw.line(window, (200,200,200), (200, 100+y), (500, 100+y), 1)
            y+=x
        z = x
        while z <= 300:
            pygame.draw.line(window, (200,200,200), (200+z, 700), (200+z, 100), 1)
            z+=x
    block_size = 30

    # ===== Loop principal =====
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        text_wdt = (WIDTH/2) - (text.get_width()/2)
        text_hgt = (HEIGHT/24)

        window.blit(text, (text_wdt, text_hgt))
        window.blit(text2, (530, 300))

        grid_builder(block_size)
        pygame.draw.line(window, (255,0,0), (200, 700), (200, 100), 4)
        pygame.draw.line(window, (255,0,0), (500, 700), (500, 100), 4)
        pygame.draw.line(window, (255,0,0), (200, 100), (500, 100), 4)
        pygame.draw.line(window, (255,0,0), (200, 700), (500, 700), 4)
        
        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

if __name__ == "__main__":
    main()