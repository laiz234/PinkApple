import pygame
from random import randrange

branco=(255,255,255)
preto=(0,0,0)
rosa=(255,62,150)
azulClaro=(0,245,255)
roxo=(178,58,238)

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado com sucesso")

largura=320
altura=280
# tamanho=10
placar = 40

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("PINK APPLE")
font = pygame.font.SysFont(None, 15)

def texto (msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY, tamanho):
    for XY in CobraXY:
        pygame.draw.rect(fundo, azulClaro, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y, tamanho):
    pygame.draw.rect(fundo, rosa, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    tamanho=10
    pos_x=randrange(0,largura-tamanho,10)
    pos_y=randrange(0,altura-tamanho-placar,10)
    maca_x=randrange(0,largura-tamanho,10)
    maca_y=randrange(0,altura-tamanho-placar,10)
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        sair = True
                        fimdejogo = False
                        tamanho=10
                        pos_x=randrange(0,largura-tamanho,10)
                        pos_y=randrange(0,altura-tamanho-placar,10)
                        maca_x=randrange(0,largura-tamanho,10)
                        maca_y=randrange(0,altura-tamanho-placar,10)
                        velocidade_x=0
                        velocidade_y=0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
            fundo.fill(preto)
            texto("Game Over!", rosa, 50, 60, 30)
            texto("Pontuação Final: "+str(pontos),azulClaro, 30, 70, 80)
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto("Novo Jogo:(N)", roxo, 30, 46, 125)
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto("Sair:(S)", roxo, 29, 195, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0
                    velocidade_x=-tamanho    
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y=0
                    velocidade_x=tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x=0
                    velocidade_y=-tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x=0
                    velocidade_y=tamanho
 
        fundo.fill(preto)
        pos_x+=velocidade_x
        pos_y+=velocidade_y

        if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0,largura-tamanho,10)
                maca_y = randrange(0,altura-tamanho-placar,10)
                CobraComp += 1
                pontos += 1

##      if pos_x > largura:
##           pos_x = 0
##      if pos_x < 0:
##           pos_x=largura-tamanho
##      if pos_y > altura:
##           pos_y = 0
##      if pos_y < 0:
##           pos_y = altura-tamanho
        if pos_x + tamanho > largura:
            fimdejogo = True
        if pos_x < 0:
            fimdejogo = True
        if pos_y + tamanho > altura-placar:
            fimdejogo = True
        if pos_y < 0:
            fimdejogo = True


        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComp:
            del CobraXY[0]
            
        if any(Bloco == altura and largura for Bloco in CobraXY[:-1]):
            fimdejogo = True

        pygame.draw.rect(fundo, roxo, [0, altura-placar, largura, placar])
        texto("Pontuação:"+str(pontos), preto, 25, 15, altura-30)
        cobra(CobraXY, tamanho)
        maca(maca_x, maca_y, tamanho)
        pygame.display.update()
        relogio.tick(10)

        
jogo()
pygame.quit()

