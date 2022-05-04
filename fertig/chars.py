import pygame   # Module

# Bilder importieren
dinoImgList = [pygame.image.load("img/dino_back_leg.png"), pygame.image.load("img/dino_front_leg.png")]
dinoDuckImgList = [pygame.image.load("img/dino_duck_back_leg.png"), pygame.image.load("img/dino_duck_front_leg.png")]
cactusImg   = pygame.image.load("img/cactus.png")
birdImgList = [pygame.image.load("img/bird_down.png"), pygame.image.load("img/bird_up.png")]

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

    def characterRect(self, inflateX, inflateY):
        return self.image().get_rect(topleft=(self.position())).inflate(self.inflateX, self.inflateY)


class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.currentImg = 0
        self.img = dinoImgList[self.currentImg]

        self.jumpvar = -11
        self.duckvar = False
        self.startY = y

        # Wie viele Pixel vom exakten Bild sollen weniger angezeigt werden als Kollisionsföäche
        self.inflateX, self.inflateY = -40, -10
        self.rect = self.characterRect(self.inflateX, self.inflateY)
    
    def nextAnimation(self):
        if self.currentImg == 0:
            self.currentImg += 1
        else:
            self.currentImg -= 1
        
        if not self.duckvar:
            self.img = dinoImgList[self.currentImg]
        else: 
            self.img = dinoDuckImgList[self.currentImg]

    def calculateY(self):
        if self.jumpvar >= -10:
            n = 1
            if self.jumpvar < 0:
                n = -1
            self.y -= (self.jumpvar**2)*0.9*n
            self.jumpvar -= 1
        
        self.rect = self.characterRect(self.inflateX, self.inflateY)

    def setJump(self):
        if self.jumpvar == -11:
            self.jumpvar = 10
    
    def setDuck(self):
        self.jumpvar = -11
        self.duckvar = True
        self.y = self.startY + 35
    
    def normalize(self):
        self.y = self.startY
        self.duckvar = False
    
    def stop(self):
        self.jumpvar = -12

# Gegner:
# Klasse Gegner bündelt nochmal alle Eigenschaften, die beide Arten von Gegner gemeinsam haben
class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def calculateX(self, speed):
        self.x -= speed
        self.rect = self.characterRect(self.inflateX, self.inflateY)
    
    def generate(self, startPos):
        self.x = startPos


class Cactus(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = cactusImg

        self.inflateX, self.inflateY = -40, -10
        self.rect = self.characterRect(self.inflateX, self.inflateY)
    

class Bird(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.currentImg = 0
        self.img = birdImgList[self.currentImg]

        self.inflateX, self.inflateY = -40, -40
        self.rect = self.characterRect(self.inflateX, self.inflateY)

    def nextAnimation(self):
        if self.currentImg == 0:
            self.currentImg += 1
        else:
            self.currentImg -= 1

        self.img = birdImgList[self.currentImg]
    
        
