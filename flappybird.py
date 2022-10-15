import pygame
import os
import random

TELA_LARGURRA= 500
TELA_ALTURA= 800

IMAGEM_CANO= pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs','pipe.png')))
IMAGEM_CHAO= pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs','base.png')))
IMAGEM_BKGROUNG= pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs','bg.png')))
IMAGEM_PASSARO=[
    pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.patch.join('imgs', 'bird3.png'))),
]

pygmae.font.init()
FONTE = pygame.font.sysfont('Arial', 50)

Class PASSARO:
IMG = IMAGEM_PASSARO
ROTACAO = 25
VELOCIDA = 20
TEMPO= 5

def __init__(self, x,y):
    self.x = x
    self.y = y
    self.angulo = 0
    self. velocidade = 0
    self.altura = self.y
    self.tempo = 0
    self.contagem = 0
    self.imagem = IMG[0]

def pular(self):
    self.velocidade= -10.5
    self.tempo= 0
    self.altura = self.y
#calculo de deslocamento
def mover (self):
    self.tempo += 1
    deslocamento = 1.5 * (self.tempo**2) + self.deslocamneto * self.tempo

#restringir
    if deslocamento > 16:
        deslocamento= 16
    elif deslocamento < 0:
        deslocamento -=2

    self.y += deslocamento