import pygame               # Module
import chars                # File chars.py
from random import choice   # Module

# Bilder importieren
background = pygame.image.load("img/background.png")
floor = pygame.image.load("img/floor.png")
gameIcon = pygame.image.load("img/game_icon.png")

# Fenstereinstellungen
pygame.init()
pygame.display.set_caption("Google Dinosaur Game - Clon")
pygame.display.set_icon(gameIcon)

window = pygame.display.set_mode((1536, 768))

# Score
currentScore = 0
font = pygame.font.SysFont("Cascadia Code", 45)

# Chars erstellen
player = chars.Player(200, 410)
bird = chars.Bird(-300, 200)
cactus = chars.Cactus(-300, 400)
# Gegner generieren
def generateEnemy():
    if cactus.position()[0] < -300:
        startPos = choice(range(2000, 4000, 500))
        cactus.generate(startPos)
    if bird.position()[0] < -300:
        startPos = choice(range(3500, 6000, 500))
        bird.generate(startPos)

# Alle Grafiken einzeichnen
bgMove = 0
flMove = 0
def moveSurface(var, speed, end):
    if var >= end:
        return var + speed
    return 0

def drawGame():
    # Zeichne in unser Fenster: [Bild], Position als Tupel (x, y)
    window.blit(background, (bgMove,  0))
    window.blit(floor, (flMove, 0))

    if gameLost:
        pygame.draw.rect(window, (0,255,0), player.rect)
        pygame.draw.rect(window, (255,0,0), cactus.rect)
        pygame.draw.rect(window, (255,0,0), bird.rect)

    window.blit(player.image(), player.position())
    window.blit(cactus.image(), cactus.position())    
    window.blit(bird.image(), bird.position())


    #                       [Anzuzeigender Text],     [antialias], [Farbe in RGB], [Position]
    window.blit(font.render(f"Score: {currentScore}", True,        (0, 0, 0)),     (10, 10))


# main loop
gameIsRunning = True
gameLost = False
speed = 10
animationCounter = 0
while gameIsRunning:
    # Game beenden, wenn man auf X klickt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameIsRunning = False
    
    # Gedrückte Taste entgegennehmen und auswerten
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player.setJump()
        elif event.key == pygame.K_DOWN:
            player.setDuck()
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            player.normalize()

    # Prüfung der Kollision
    collideCactus = player.rect.colliderect(cactus.rect)
    collideBird = player.rect.colliderect(bird.rect)
    if collideCactus or collideBird:
        speed = 0
        animationCounter = 1
        gameLost = True
        player.stop()

    player.calculateY()
    cactus.calculateX(speed)
    bird.calculateX(speed)

    # Jeden 2./4. Durchlauf (% 2/% 4) führe die Funktion nextAnimation() aus
    if animationCounter % 2 == 0:
        player.nextAnimation()
        if animationCounter % 4 == 0:
            bird.nextAnimation()
            animationCounter = 0

    animationCounter += 1
    
    bgMove = moveSurface(bgMove, -(speed/4), -4096)
    flMove = moveSurface(flMove, -speed, -4096)

    speed += 0.05
    currentScore += int(speed/10)

    generateEnemy()

    drawGame()
    pygame.display.update()