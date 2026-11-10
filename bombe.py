import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOMBE_SIZE, BOMBE_SPEED

class Bombe(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        
        self.image = pygame.image.load("assets/bombe.png")
        self.image = pygame.transform.scale(self.image, (BOMBE_SIZE, BOMBE_SIZE))
        self.rect = self.image.get_rect()
        self.speed = BOMBE_SPEED
        
    def respawn(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - BOMBE_SIZE)
        self.rect.y = -BOMBE_SIZE

    def fall(self):
        self.rect.y += self.speed

        if self.rect.y > SCREEN_HEIGHT:
            self.respawn()
        
