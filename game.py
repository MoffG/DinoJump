import pygame   # Module
import chars    # File chars.py

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
player = chars.Player(200, 420)

# Alle Grafiken einzeichnen
def drawGame():
    # Zeichne in unser Fenster: [Bild], Position als Tupel (x, y)
    window.blit(background, (0, 0))
    window.blit(floor, (0, 0))

    window.blit(player.image(), player.position())

    #                       [Anzuzeigender Text],     [antialias], [Farbe in RGB], [Position]
    window.blit(font.render(f"Score: {currentScore}", True,        (0, 0, 0)),     (10, 10))


# main loop
gameIsRunning = True
while gameIsRunning:
    # Game beenden, wenn man auf X klickt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameIsRunning = False
    

    drawGame()
    pygame.display.update()