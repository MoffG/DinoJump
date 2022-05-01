import pygame               # Module
# from random import choice   # Module

# Bilder importieren
dinoImgList   = [pygame.image.load("img/dino_1.png"), pygame.image.load("img/dino_1.png"), pygame.image.load("img/dino_2.png"), pygame.image.load("img/dino_2.png")]
cactusImg = pygame.image.load("img/cactus.png")

# Klasses Character: Was haben alle Charaktere gemeinsam?
class Character:
    # __init__(self): 
    def position(self):
        return (self.x, self.y)
    
    def img(self):
        return self.img


class Player(Character):
    def __init__(self):
        self.x = 600
        self.y = 400

        self.img = dinoImgList[2]

        