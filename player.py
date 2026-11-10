import pygame 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, PLAYER_SPEED


class Player(pygame.sprite.Sprite):
    
    def __init__(self): 
       super().__init__()
    
    #charger l'image du chat et la redimensionner
       self.image = pygame.image.load("assets/player.png")
       self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))
        
       self.rect = self.image.get_rect()
        
       self.rect.x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
       self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE - 20
        
        
    def move_right(self):
            if self.rect.x + PLAYER_SIZE < SCREEN_WIDTH:
                self.rect.x += PLAYER_SPEED
                
    def move_left(self):
            if self.rect.x > 0:
                self.rect.x -= PLAYER_SPEED
    
    
    