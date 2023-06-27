import pygame

w = pygame.display.set_mode((1279,720))
class Sprite():
    image = pygame.image.load('assets/capy.jpg').convert()
    speed =1
    x =100
    y =100

Player = Sprite()

game = True
while game:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        Player.x += Player.speed
    if keys[pygame.K_LEFT]:
        Player.x -= Player.speed
    if keys[pygame.K_UP]:
        Player.y -= Player.speed
    if keys[pygame.K_DOWN]:
        Player.y += Player.speed
    w.fill((0,0,0))
    w.blit(Player.image, (Player.x, Player.y))
    pygame.display.update()

pygame.quit()



