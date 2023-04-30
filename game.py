import pygame
from Death_zone import *
from Start_zone import *
from End_zone import *
from level import *
from math import *
from saves_reader import *

FPS = 250
FramePerSecond = pygame.time.Clock()
#Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 700
#Define Colors
BLACK = (0,0,0)
GRAY =(100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = (0,0,255)

#stick man size
player = pygame.image.load("Ressources//alexis.png")
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 30
player = pygame.transform.scale(player,(PLAYER_WIDTH,PLAYER_HEIGHT))

#level
start_zone = Start_zone(PLAYER_WIDTH,PLAYER_HEIGHT).get_sz()
end_zone = End_zone(PLAYER_WIDTH,PLAYER_HEIGHT).get_ez()



def create_game(nbdz,tuplestart : tuple[int,int]= None,tupleend :tuple[int,int]= None):
    #matrice 20x20 with one start_zone one end_zone and x death_zone randomly place
    pygame.init()
    #set player position
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("test interface")
    lvl = Level(nbdz,tuplestart,tupleend)
    lvl.generate_level()
    player_pos = tuplestart
    running = True
    
    #Score 
    start_time = pygame.time.get_ticks()
    elasped_time =0
    font = pygame.font.Font(None,36)
    distance_start_end = sqrt((abs(tuplestart[0] - tupleend[0])**2)+
                              (abs(tuplestart[1] - tupleend[1])**2))
    
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Framerate
        pygame.time.Clock().tick(FPS)

        #Moving player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and player_pos[0] > 0:
            player_pos = (player_pos[0]-1, player_pos[1])
        elif keys[pygame.K_q] and player_pos[1] > 0:
            player_pos = (player_pos[0], player_pos[1]-1)
        elif keys[pygame.K_s] and player_pos[0] < lvl.get_size()[0]-1:
            player_pos = (player_pos[0]+1, player_pos[1])
        elif keys[pygame.K_d] and player_pos[1] < lvl.get_size()[1]-1:
            player_pos = (player_pos[0], player_pos[1]+1) 
        
        
        #Finished?
        
        if player_pos == tupleend:
            #Faudra save ici les infos de l'IA
            print("You won !")
            score= score +100 #bonus for finishing
            print(score)

            running = False
            
        if lvl.get_lvl()[player_pos[0]][player_pos[1]]==-1:
            print("You lost looser !!!!")
            print(score)
            running = False

        # Fill the screen with gray
        screen.fill(GRAY)
     
        
        
        
        #Draw the Level
        
        for i in range(lvl.get_size()[0]):
            for j in range(lvl.get_size()[1]):
                if lvl.get_lvl()[i][j] == 1:
                    #afficher l'image ici start_zone
                    screen.blit(start_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 0:
                    pygame.draw.rect(screen, WHITE, (j * PLAYER_WIDTH, i * PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 2:
                    #afficher l'image ici end_zone
                    screen.blit(end_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == -1:
                    #afficher l'image ici death_zone
                    screen.blit(Death_zone(PLAYER_WIDTH,PLAYER_HEIGHT).get_dz(),(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
        #Draw Player
        screen.blit(player,(player_pos[1] * PLAYER_WIDTH, player_pos[0] * PLAYER_HEIGHT))
        
        #timer update
        elapsed_time = (pygame.time.get_ticks()- start_time+1)/1000
        #Draw this Score:
        current_distance = sqrt((abs(player_pos[0] - tupleend[0])**2)+
                              (abs(player_pos[1] - tupleend[1])**2))
        score = ((distance_start_end-current_distance)/elapsed_time)*100
        score_surface = font.render(f"Score: {score} pts",True,RED)
        screen.blit(score_surface,(20,WINDOW_HEIGHT-50))
        # Update the display
        pygame.display.update()
        #FramePerSecond.tick(FPS)

    # Quit Pygame
    pygame.quit()
    
    
    
def create_game_from_save(save):
    
    lvl = read_save(save)
    #matrice 20x20 with one start_zone one end_zone and x death_zone randomly place
    pygame.init()
    #set player position
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("test interface")

    player_pos = (lvl.get_start_x(),lvl.get_start_y())
    running = True
    
    #Score 
    start_time = pygame.time.get_ticks()
    elasped_time =0
    font = pygame.font.Font(None,36)
    distance_start_end = sqrt((abs(lvl.get_start_x() - lvl.get_end_x())**2)+
                              (abs(lvl.get_start_y() - lvl.get_end_y())**2))
    
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Framerate
        pygame.time.Clock().tick(FPS)

        #Moving player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and player_pos[0] > 0:
            player_pos = (player_pos[0]-1, player_pos[1])
        elif keys[pygame.K_q] and player_pos[1] > 0:
            player_pos = (player_pos[0], player_pos[1]-1)
        elif keys[pygame.K_s] and player_pos[0] < lvl.get_size()[0]-1:
            player_pos = (player_pos[0]+1, player_pos[1])
        elif keys[pygame.K_d] and player_pos[1] < lvl.get_size()[1]-1:
            player_pos = (player_pos[0], player_pos[1]+1) 
        
        
        #Finished?
        
        if player_pos == (lvl.get_end_x(),lvl.get_end_y()):
            #Faudra save ici les infos de l'IA
            print("You won !")
            score= score +100 #bonus for finishing
            print(score)

            running = False
            
        if lvl.get_lvl()[player_pos[0]][player_pos[1]]==-1:
            print("You lost looser !!!!")
            print(score)
            running = False

        # Fill the screen with gray
        screen.fill(GRAY)
     
        
        
        
        #Draw the Level
        
        for i in range(lvl.get_size()[0]):
            for j in range(lvl.get_size()[1]):
                if lvl.get_lvl()[i][j] == 1:
                    #afficher l'image ici start_zone
                    screen.blit(start_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 0:
                    pygame.draw.rect(screen, WHITE, (j * PLAYER_WIDTH, i * PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 2:
                    #afficher l'image ici end_zone
                    screen.blit(end_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == -1:
                    #afficher l'image ici death_zone
                    screen.blit(Death_zone(PLAYER_WIDTH,PLAYER_HEIGHT).get_dz(),(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
        #Draw Player
        screen.blit(player,(player_pos[1] * PLAYER_WIDTH, player_pos[0] * PLAYER_HEIGHT))
        
        #timer update
        elapsed_time = (pygame.time.get_ticks()- start_time+1)/1000
        #Draw this Score:
        current_distance = sqrt((abs(player_pos[0] - lvl.get_end_x())**2)+
                              (abs(player_pos[1] - lvl.get_end_y())**2))
        score = ((distance_start_end-current_distance)/elapsed_time)*100
        score_surface = font.render(f"Score: {score} pts",True,RED)
        screen.blit(score_surface,(20,WINDOW_HEIGHT-50))
        # Update the display
        pygame.display.update()
        #FramePerSecond.tick(FPS)

    # Quit Pygame
    pygame.quit()
        
        
        
#TEST A DEUX JOUEUR METTRE EN PLACE POUR PLUSIEURS ET CONTROLE PLUS AU CLAVIER MAIS JUSTE DONNER
#FONCTIONNE
def twoplayer_test(save):
        
    lvl = read_save(save)
    #matrice 20x20 with one start_zone one end_zone and x death_zone randomly place
    pygame.init()
    #set player position
    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("test interface")

    player_list= []
    for i in range(0,2):
        print("ICICICICICI")
        print(i)
        player_list.append((lvl.get_start_x(),lvl.get_start_y()))
    running = True
    
    #Score 
    start_time = pygame.time.get_ticks()
    elasped_time =0
    font = pygame.font.Font(None,36)
    distance_start_end = sqrt((abs(lvl.get_start_x() - lvl.get_end_x())**2)+
                              (abs(lvl.get_start_y() - lvl.get_end_y())**2))
    
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #Framerate
        pygame.time.Clock().tick(FPS)

        #Moving player 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and player_list[0][0] > 0:
            player_list[0] = (player_list[0][0]-1, player_list[0][1])
        elif keys[pygame.K_q] and player_list[0][1] > 0:
            player_list[0] = (player_list[0][0], player_list[0][1]-1)
        elif keys[pygame.K_s] and player_list[0][0] < lvl.get_size()[0]-1:
            player_list[0] = (player_list[0][0]+1, player_list[0][1])
        elif keys[pygame.K_d] and player_list[0][1] < lvl.get_size()[1]-1:
            player_list[0] = (player_list[0][0], player_list[0][1]+1) 
        
        #Moving player 2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_list[1][0] > 0:
            player_list[1] = (player_list[1][0]-1, player_list[1][1])
        elif keys[pygame.K_LEFT] and player_list[0][1] > 0:
            player_list[1] = (player_list[1][0], player_list[1][1]-1)
        elif keys[pygame.K_DOWN] and player_list[0][0] < lvl.get_size()[0]-1:
            player_list[1] = (player_list[1][0]+1, player_list[1][1])
        elif keys[pygame.K_RIGHT] and player_list[1][1] < lvl.get_size()[1]-1:
            player_list[1] = (player_list[1][0], player_list[1][1]+1)   
        
        
        #Finished?
        for p in player_list:
            if p == (lvl.get_end_x(),lvl.get_end_y()):
                #Faudra save ici les infos de l'IA
                print("You won !")
                score= score +100 #bonus for finishing
                print(score)

            
            if lvl.get_lvl()[p[0]][p[1]]==-1:
                print("You lost looser !!!!")
                print(score)


        # Fill the screen with gray
        screen.fill(GRAY)
     
        
        
        
        #Draw the Level
        
        for i in range(lvl.get_size()[0]):
            for j in range(lvl.get_size()[1]):
                if lvl.get_lvl()[i][j] == 1:
                    #afficher l'image ici start_zone
                    screen.blit(start_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 0:
                    pygame.draw.rect(screen, WHITE, (j * PLAYER_WIDTH, i * PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == 2:
                    #afficher l'image ici end_zone
                    screen.blit(end_zone,(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
                elif lvl.get_lvl()[i][j] == -1:
                    #afficher l'image ici death_zone
                    screen.blit(Death_zone(PLAYER_WIDTH,PLAYER_HEIGHT).get_dz(),(j * PLAYER_WIDTH, i * PLAYER_HEIGHT))
        #Draw Player
        for p in player_list:
            screen.blit(player,(p[1] * PLAYER_WIDTH, p[0] * PLAYER_HEIGHT))
        
        #timer update
        elapsed_time = (pygame.time.get_ticks()- start_time+1)/1000
        #Draw this Score:
        # current_distance = sqrt((abs(player_pos[0] - lvl.get_end_x())**2)+
        #                       (abs(player_pos[1] - lvl.get_end_y())**2))
        # score = ((distance_start_end-current_distance)/elapsed_time)*100
        # score_surface = font.render(f"Score: {score} pts",True,RED)
        # screen.blit(score_surface,(20,WINDOW_HEIGHT-50))
        # Update the display
        pygame.display.update()
        #FramePerSecond.tick(FPS)

    # Quit Pygame
    pygame.quit()
    
    
    
    
    


