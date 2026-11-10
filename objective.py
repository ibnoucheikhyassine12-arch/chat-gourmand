import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, OBJECTIVE_SIZE, OBJECTIVE_SPEED
class Objective(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("assets/objective.png")
        self.image = pygame.transform.scale(self.image, (OBJECTIVE_SIZE, OBJECTIVE_SIZE))
        self.rect = self.image.get_rect()
        self.speed = OBJECTIVE_SPEED
        self.respawn()
        
    def respawn(self):
        
        self.rect.x = random.randint(0, SCREEN_WIDTH - OBJECTIVE_SIZE)
        self.rect.y = -OBJECTIVE_SIZE
        
    def fall(self):
        self.rect.y += self.speed
        
        if self.rect.y > SCREEN_HEIGHT:
            self.respawn()
        
    
    

