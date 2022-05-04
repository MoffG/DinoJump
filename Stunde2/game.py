import pygame   # Module
import chars    # File chars.py

# Bilder importieren
background = pygame.image.load("img/background.png")
floor = pygame.image.load("img/floor.png")
gameIcon = pygame.image.load("img/game_icon.png")

cactusImg   = pygame.image.load("img/cactus.png")

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

    window.blit(player.image(), player.position())
    window.blit(cactusImg, (1000, 380))

    #                       [Anzuzeigender Text],     [antialias], [Farbe in RGB], [Position]
    window.blit(font.render(f"Score: {currentScore}", True,        (0, 0, 0)),     (10, 10))


# main loop
gameIsRunning = True
speed = 10
animationCounter = 0
while gameIsRunning:
    # Game beenden, wenn man auf X klickt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameIsRunning = False
    
    # Jeden 2. Durchlauf (% 2) führe die Funktion nextAnimation() aus
    if animationCounter % 4 == 0:
        player.nextAnimation()
        animationCounter = 0 

    animationCounter += 1
    
    bgMove = moveSurface(bgMove, -int((speed/4)), -4096)
    flMove = moveSurface(flMove, -speed, -4096)

    speed += 0.05
    currentScore += int(speed/10)

    drawGame()
    pygame.display.update()