import pygame
from random import randint

BLACK = (0, 0, 0)
class Ball(pygame.sprite.Sprite):
    #Esta classe representa uma bola. Deriva da classe "Sprite" em Pygame.

    def __init__(self, color, width, height):
        #Chame o construtor da classe pai (Sprite)
        super().__init__()

        #Passe na cor do carro, e sua posição x e y, largura e altura.
        #Defina a cor de fundo e defina-a como transparente
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #Desenhe a bola (um retângulo!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        #Busca o objeto retângulo que tem as dimensões da imagem.
        self.rect = self.image.get_rect()

    #O método update() desta classe será chamado para cada quadro do loop do programa principal. Ele se move ( altera as coordenadas ( x, y ) da bola usando seu vetor de velocidade.
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
        #Detecta quando a bola bate / colide com uma ou duas Barras. Se isso acontecer, faremos com que salte usando uma nova direção aleatória.
