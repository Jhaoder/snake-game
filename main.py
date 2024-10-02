import pygame 
import random

# criar a SCREEN do jogo
pygame.init()

LARGURA = 1200
ALTURA = 800

pygame.display.set_caption("Snake Game")
SCREEN = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()

# Cores o jogo

BGND = (0, 0, 0)
TEXT = (255, 255, 255)
SNAKE_COLOR = (255, 255, 0)
FRUIT_COLOR = (0, 255, 0)

# Gerar FRUIT_COLORs
def gerar_fruit():
    x = round(random.randrange(0, (LARGURA - SIZE) / SIZE * SIZE))
    y = round(random.randrange(0, (ALTURA - SIZE) / SIZE * SIZE))
    return x, y

# Parâmetros do jogos
FPS = 60
SIZE = 20

# Pârametros da cobrinha
def draw_snake(size, pos):
    pygame.draw.rect(SCREEN, SNAKE_COLOR, [pos[0], pos[1], SIZE, SIZE] )

# Desenhar FRUIT_COLOR
def desenhar_fruit(cor, tamanho, FRUIT_COLOR_x, FRUIT_COLOR_y):
    pygame.draw.rect(SCREEN ,cor, [FRUIT_COLOR_x, FRUIT_COLOR_y, tamanho, tamanho])

# jogo
def jogo():
    running = True
    fruit_x, fruit_y = gerar_fruit()

    while running:
        SCREEN.fill(BGND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        desenhar_fruit(FRUIT_COLOR, SIZE, fruit_x, fruit_y)
        pygame.display.update()
        relogio.tick(FPS)

jogo()