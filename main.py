import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("images/bg.png")
player_image = pygame.image.load("images/arcade.png")
spaceshipX=370
spaceshipY=480
changeX=0


running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1
            if event.key == pygame.K_RIGHT:
                changeX = 1

    spaceshipX+=changeX

    screen.blit(player_image, (spaceshipX, spaceshipY))
    pygame.display.update()