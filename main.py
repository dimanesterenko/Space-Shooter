import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

mixer.music.load("audio/background.wav")
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)


background = pygame.image.load("images/bg.png")
player_image = pygame.image.load("images/arcade.png")

bullet_image = pygame.image.load("images/bullet.png")
spaceshipX=370
spaceshipY=480
changeX=0

enemy_image=[]
enemyX=[]
enemyY=[]
enemyspeedX=[]
enemyspeedY=[]

num_of_enemies=10
for x in range(num_of_enemies):
    enemy_image.append(pygame.image.load("images/enemy.png"))
    enemyX.append(random.randint(0,738))
    enemyY.append(random.randint(30,150))
    enemyspeedX.append(-1)
    enemyspeedY.append(40)

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
    pass


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
                    laserSound=mixer.Sound("audio/laser.wav")
                    laserSound.play()
                    check = True
                    bulletX = spaceshipX + 16
        if event.type == pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=3:
        spaceshipX=3
    elif spaceshipX>=738:
        spaceshipX=738
    for i in range(num_of_enemies):
        if enemyY[i] > 420:
            for j in range(num_of_enemies):
                enemyY[i] = 2000
            gameover()
            break
        enemyX[i]+=enemyspeedX[i]
        if enemyX[i]<=0:
            enemyspeedX[i]=3
            enemyY[i]+=enemyspeedY[i]
        if enemyX[i]>=738:
            enemyspeedX[i]=-3
            enemyY[i]+=enemyspeedY[i]

        distance = math.sqrt(math.pow(bulletX - enemyX[i], 2) + math.pow(bulletY - enemyY[i], 2))
        if distance < 27:
            explSound=mixer.Sound("audio/explosion.wav")
            explSound.play()
            bulletY = 480
            check = False
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(30, 150)
        screen.blit(enemy_image[i], (enemyX[i], enemyY[i]))

    if bulletY<=0:
        bulletY=490
        check=False

    if check:
        screen.blit(bullet_image, (bulletX, bulletY))
        bulletY-=10




    screen.blit(player_image, (spaceshipX, spaceshipY))
    score_text()
    pygame.display.update()