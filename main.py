import pygame 
import random

# criar a tela do jogo
pygame.init()

largura = 1200
altura = 800

pygame.display.set_caption("Snake Game")
TELA = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores o jogo

BGND = (0, 0, 0)
TEXTO = (255, 255, 255)
SNAKE = (255, 255, 0)
FRUTA = (0, 255, 0)

# Gerar Frutas
def gerar_fruta():
    x = round(random.randrange(0, (largura - TAMANHO) / TAMANHO * TAMANHO))
    y = round(random.randrange(0, (altura - TAMANHO) / TAMANHO * TAMANHO))
    return x, y

# Parâmetros do jogos
FPS = 60
TAMANHO = 20

# Desenhar fruta
def desenhar_fruta(cor, tamanho, fruta_x, fruta_y):
    pygame.draw.rect(TELA ,cor, [fruta_x, fruta_y, tamanho, tamanho])

# jogo
def jogo():
    running = True
    fruta_x, fruta_y = gerar_fruta()

    while running:
        TELA.fill(BGND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        desenhar_fruta(FRUTA, TAMANHO, fruta_x, fruta_y)
        pygame.display.update()
        relogio.tick(FPS)

jogo()