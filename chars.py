import pygame               # Module
# from random import choice   # Module

# Bilder importieren
dinoImgList = [pygame.image.load("img/dino_1.png"), pygame.image.load("img/dino_2.png")]
cactusImg   = pygame.image.load("img/cactus.png")

# Klasses Character: Was haben alle Charaktere gemeinsam?
class Character:
    # Änderung: Character
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
        self.img = dinoImgList[0]
    
    def nextAnimation(self):
        pass

        