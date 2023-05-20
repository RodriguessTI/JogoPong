#Importar a biblioteca pygame
import pygame

#Importar a classe Paddle(Barra)
from paddle import Paddle
#Importar a classe Ball(bola)
from ball import Ball
#Importar a classe tijolo(Brick)
from brick import Brick

#inicializar o jogo
pygame.init()

#Definir algumas cores
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

#Pontuação
score = 0
#Vidas
lives = 3

#O jogo será executado em sua própria janela, para a qual você pode decidir um título, uma largura e uma altura
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#Esta será uma lista que conterá todos os sprites que pretendemos utilizar em nosso jogo.
all_sprites_list = pygame.sprite.Group()

#Crie a Barra
paddle = Paddle(LIGHTBLUE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

#Crie o sprite da bola
ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#criamos três linhas de tijolos e as adicionamos a um grupo chamado all_bricks.
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)
#Fim do codigo tijolos

#Adicionando a Barra(paddle) e a bola(ball) à lista de sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

#O loop continuará até que o usuário saia do jogo (por exemplo, clique no botão Fechar).
carryOn = True

#O relógio será usado para controlar a rapidez com que a tela é atualizada
clock = pygame.time.Clock()

# -------- Loop do programa principal -----------
while carryOn:
    # --- Loop de evento principal
    for event in pygame.event.get(): #O usuário fez algo
        if event.type == pygame.QUIT: #Se o usuário clicou em fechar
              carryOn = False #Sinalize que terminamos, então saímos deste loop

    #Movendo a Barra quando o uso usa as teclas de seta
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    # --- A lógica do jogo deve ir aqui
    all_sprites_list.update()

    #Verifique se a bola está quicando em alguma das 4 paredes:
    if ball.rect.x>=790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>590:
        ball.velocity[1] = -ball.velocity[1]
        #tiramos uma vida quando a bola bate na borda inferior da tela. Se o número de vidas atingir zero, exibiremos uma mensagem “ Game Over ”..
        lives -= 1
        if lives == 0:
            #Exibir mensagem de fim de jogo por 3 segundos
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Pare o jogo
            carryOn=False

    if ball.rect.y<40:
        ball.velocity[1] = -ball.velocity[1]

    #Detectar colisões entre a bola e as raquetes
    if pygame.sprite.collide_mask(ball, paddle):
      ball.rect.x -= ball.velocity[0]
      ball.rect.y -= ball.velocity[1]
      ball.bounce()

    #detectamos se a bola bate em um tijolo. Nesse caso, removemos o tijolo ( usando o matar ( ) método ) e incremente a pontuação em um.
    #Verifique se a bola colide com algum dos tijolos
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
      ball.bounce()
      score += 1
      brick.kill()
      if len(all_bricks)==0:
           #Exibir mensagem de nível concluído por 3 segundos
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)

            #Pare o jogo
            carryOn=False

    # --- O código do desenho deve ir aqui
    # Primeiro, limpe a tela para azul escuro.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Exiba a pontuação e o número de vidas na parte superior da tela
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    #Agora vamos desenhar todos os sprites de uma só vez. (Por enquanto só temos 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Vá em frente e atualize a tela com o que desenhamos.
    pygame.display.flip()

    # --- Limite a 60 quadros por segundo
    clock.tick(60)

#Depois de sair do loop principal do programa, podemos parar o mecanismo do jogo:
pygame.quit()
