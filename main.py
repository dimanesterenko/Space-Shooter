import pygame
import random
import math
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
enemyspeedY=40

check = False
bulletX = 386
bulletY = 490

score = 0

font = pygame.font.SysFont('Monospace',32,'bold')


def score_text():
    img = font.render(f"Score:{score}",True,"orange")
    screen.blit(img,(10,10))

font_gameover = pygame.font.SysFont('Monospace',64,'bold')

def gameover():
    img_go = font.render("GAME OVER", True, "white")
    screen.blit(img_go, (350, 250))


def collision():
    distance = math.sqrt(math.pow(bulletX-enemyX,2)+math.pow(bulletY-enemyY,2))
    if distance<27:
        return True


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
                if check is False:
                    check = True
                    bulletX = spaceshipX + 16
        if event.type == pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=3:
        spaceshipX=3
    elif spaceshipX>=738:
        spaceshipX=738

    enemyX+=enemyspeedX

    if enemyX<=0:
        enemyspeedX=3
        enemyY+=enemyspeedY
    if enemyX>=738:
        enemyspeedX=-3
        enemyY+=enemyspeedY

    if bulletY<=0:
        bulletY=490
        check=False

    if check:
        screen.blit(bullet_image, (bulletX, bulletY))
        bulletY-=10

    if enemyY>420:
        enemyY=2000
        gameover()


    collision_occured = collision()
    if collision_occured:
        bulletY=480
        check=False
        score+=1
        enemyX=random.randint(0,736)
        enemyY=random.randint(30,150)
    screen.blit(player_image, (spaceshipX, spaceshipY))
    screen.blit(enemy_image, (enemyX, enemyY))
    score_text()
    pygame.display.update()