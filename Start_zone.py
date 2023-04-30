import pygame

class Start_zone():
    def __init__(self,PLAYER_WIDTH,PLAYER_HEIGHT):
        start_zone = pygame.image.load("Ressources//start_zone.png")
        start_zone = pygame.transform.scale(start_zone,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.sz = start_zone
        
    def get_sz(self):
        return self.sz