import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("images/bg.png")
player_image = pygame.image.load("images/arcade.png")
enemy_image = pygame.image.load("images/enemy.png")
bullet_image = pygame.image.load("images/bullet.png")
spaceshipX=370
spaceshipY=480
changeX=0
enemyX=random.randint(0,738)
enemyY=random.randint(30,150)
enemyspeedX=3
enemyspeedY=10

check=False
bulletX=370
bulletY=480

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -5
            if event.key == pygame.K_RIGHT:
                changeX = 5
            if event.key == pygame.K_SPACE:
                check=True

        if event.type == pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=3:
        spaceshipX=3
    elif spaceshipX>=738:
        spaceshipX=738


    if enemyX<=0:
        enemyspeedX=3
        enemyY+=enemyspeedY
    if enemyX>=738:
        enemyspeedX=-3
        enemyY+=enemyspeedY
    enemyX+=enemyspeedX
    if check is True:
        screen.blit(bullet_image, (bulletX, bulletY))

    screen.blit(player_image, (spaceshipX, spaceshipY))
    screen.blit(enemy_image, (enemyX, enemyY))

    pygame.display.update()