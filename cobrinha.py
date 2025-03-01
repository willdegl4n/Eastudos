import pygame
from pygame.locals import *

import random

import time

WINDOWS_WIDTH = 600
WINDOWS_HEIGTH = 600
POS_INICIAL_X = WINDOWS_WIDTH / 2
POS_INICIAL_Y = WINDOWS_HEIGTH / 2
BLOCK = 10 

pontos = 0
velocidade = 10
creditos = 'SQL Dicas - Administração e Engenharia de Dados'

pygame.font.init()
fonte = pygame.font.SysFont('arial', 15, True, True) #negrito e italico
fonte_rodape = pygame.font.SysFont('arial', 15) #negrito e italico
#pygame.font.get_fonts() #verifica as fontes instaladas

def colisao(pos1, pos2):
    return pos1 == pos2

def verifica_margens(pos):
    if 0 <= pos[0] < WINDOWS_WIDTH and 0 <= pos[1] < WINDOWS_HEIGTH:
        return False
    else:
        return True
    
def gera_pos_aleatoria():
    x = random.randint(0, WINDOWS_WIDTH)
    y = random.randint(0, WINDOWS_HEIGTH)

    if (x,y) in obstaculo_pos:
        gera_pos_aleatoria()

    return x // BLOCK * BLOCK, y // BLOCK * BLOCK

def game_over():
    fonte = pygame.font.SysFont('arial', 60, True, True)
    gameOver = 'GAMER OVER'
    text_over = fonte.render(gameOver, True, (255,255,255))
    window.blit(text_over,(110,250))
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()

pygame.init()
window = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGTH))
pygame.display.set_caption('Jogo da Cobrinnha - SQL Dicas')

cobra_pos = [(POS_INICIAL_X, POS_INICIAL_Y),(POS_INICIAL_X + BLOCK, POS_INICIAL_Y),(POS_INICIAL_X + 2 * BLOCK, POS_INICIAL_Y)]
cobra_surface = pygame.Surface((BLOCK,BLOCK))
cobra_surface.fill((53,59,75))
direcao = K_LEFT

obstaculo_pos = []
obstaculo_surface = pygame.Surface((BLOCK,BLOCK))
obstaculo_surface.fill((0,0,0))

maca_surface = pygame.Surface((BLOCK,BLOCK))
maca_surface.fill((255,0,0))
maca_pos = gera_pos_aleatoria()

while True:
    pygame.time.Clock().tick(velocidade)
    window.fill((83,83,236))

    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (255,255,255))

    mensagem2 = f'{creditos}'
    rodape = fonte_rodape.render(mensagem2, True, (255,255,255))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                if evento.key == K_UP and direcao == K_DOWN:
                    continue
                elif evento.key == K_DOWN and direcao == K_UP:
                    continue
                elif evento.key == K_LEFT and direcao == K_RIGHT:
                    continue
                elif evento.key == K_RIGHT and direcao == K_LEFT:
                    continue
                else:
                    direcao = evento.key

    window.blit(rodape,(5,580))

    window.blit(maca_surface,maca_pos)
    
    if (colisao(cobra_pos[0],maca_pos)):
        cobra_pos.append((-10,-10))
        maca_pos = gera_pos_aleatoria()
        obstaculo_pos.append(gera_pos_aleatoria())
        pontos += 1
        if pontos % 5 == 0:
            velocidade += 2

    for pos in obstaculo_pos:
        if colisao(cobra_pos[0],pos):
            game_over()
        window.blit(obstaculo_surface,pos)

    for pos in cobra_pos:
        window.blit(cobra_surface,pos)
    
    for item in range(len(cobra_pos)-1,0,-1):
        if colisao(cobra_pos[0],cobra_pos[item]):
            game_over()
        cobra_pos[item] = (cobra_pos[item-1])

    if verifica_margens(cobra_pos[0]):
        game_over()

    if direcao == K_RIGHT:
        cobra_pos[0] = cobra_pos[0][0] + BLOCK, cobra_pos[0][1] #movimenta para direita
    
    elif direcao == K_LEFT:
        cobra_pos[0] = cobra_pos[0][0] - BLOCK, cobra_pos[0][1] #movimenta para esquerda
    
    elif direcao == K_UP:
        cobra_pos[0] = cobra_pos[0][0] , cobra_pos[0][1] - BLOCK #movimenta para cima
    
    elif direcao == K_DOWN:
        cobra_pos[0] = cobra_pos[0][0] , cobra_pos[0][1] + BLOCK #movimenta para baixo

    window.blit(texto,(520,10))
    
    pygame.display.update()

    # obrigado pela atenção, esse foi só um exercicio guiado de Python
    # usando a biblioteca pyGAME.
    # Até a proxima...

#    SQL Dicas 
