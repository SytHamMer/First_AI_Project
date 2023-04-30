import pygame

class End_zone():
    def __init__(self,PLAYER_WIDTH,PLAYER_HEIGHT):
        end_zone = pygame.image.load("Ressources//end_zone.png")
        end_zone = pygame.transform.scale(end_zone,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.ez = end_zone
        
    def get_ez(self):
        return self.ez