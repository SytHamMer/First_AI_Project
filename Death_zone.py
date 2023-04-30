import pygame

class Death_zone():
    def __init__(self,PLAYER_WIDTH,PLAYER_HEIGHT):
        death_zone = pygame.image.load("Ressources//death_zone.png")
        death_zone = pygame.transform.scale(death_zone,(PLAYER_WIDTH,PLAYER_HEIGHT))
        self.dz = death_zone
    def get_dz(self):
        return self.dz