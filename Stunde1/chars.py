import pygame   # Module

# Bilder importieren
dinoImg = pygame.image.load("img/dino_green.png")
cactusImg   = pygame.image.load("img/cactus.png")

# Klasses Character: Was haben alle Charaktere gemeinsam?
class Character:
    # Gemeinsamkeiten aller Charaktere
    def __init__(self, x, y):
        self.x, self.y = x, y

    # helper functions
    def position(self):
        return (self.x, self.y)
    
    def image(self):
        return self.img

class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = dinoImg