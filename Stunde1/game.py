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

# Chars erstellen
player = chars.Player(200, 375)

# Alle Grafiken einzeichnen
def drawGame():
    # Zeichne in unser Fenster: [Bild], Position als Tupel (x, y)
    window.blit(background, (0,  0))
    window.blit(floor, (0, 0))

    window.blit(player.image(), player.position())
    window.blit(cactusImg, (1000, 380))



# main loop
gameIsRunning = True
while gameIsRunning:
    # Game beenden, wenn man auf X klickt
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            gameIsRunning = False
    

    drawGame()
    pygame.display.update()