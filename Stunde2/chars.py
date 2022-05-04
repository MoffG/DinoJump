import pygame   # Module

# Bilder importieren
dinoImgList = [pygame.image.load("img/dino_back_leg.png"), pygame.image.load("img/dino_front_leg.png")]
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
        self.currentImg = 0
        self.img = dinoImgList[self.currentImg]
    
    def nextAnimation(self):
        if self.currentImg == 0:
            self.currentImg += 1
        else:
            self.currentImg -= 1
        
        self.img = dinoImgList[self.currentImg]