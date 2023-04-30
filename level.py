from Death_zone import *
from Start_zone import *
from End_zone import *
import numpy as np
import pygame
import random
import os
import json

class Level():
    def __init__(self,nbdz,tuplestart : tuple[int,int]= None,tupleend :tuple[int,int]= None):
        #end and start give
        self.nbdz =nbdz
        if tuplestart == None:    
            self.start_x = 0
            self.start_y = 0
        else:
            self.start_x = tuplestart[0]
            self.start_y = tuplestart[1]
        if tupleend == None:
            self.end_x = self.get_size()[0]-1
            self.end_y = self.get_size()[1]-1
        else:
            self.end_x = tupleend[0]
            self.end_y = tupleend[1]
        self.size =(20,20)
        self.lvl = np.zeros(self.get_size())
        
        
    def get_size(self):
        return self.size
        
    def get_nbdz(self):
        return self.nbdz
    def get_start_x(self):
        return self.start_x
    def get_start_y(self):
        return self.start_y
    def get_end_x(self):
        return self.end_x
    def get_end_y(self):
        return self.end_y
    def get_lvl(self):
        return self.lvl


    def can_be_place(self,x,y):
        lvl = self.get_lvl()
        #not next to start
        res = True
        #Out of index error to solve !!!
        # if lvl[x-1,y+1] !=1 or lvl[x,y+1] !=1 or lvl[x+1,y+1] !=1 or lvl[x-1,y-1] !=1 or lvl[x,y-1] !=1 or lvl[x+1,y-1] !=1 or lvl[x-1,y] != 1 or lvl[x+1,y]!=1:
        #     res = False
        #     return res
        # elif lvl[x-1,y+1] !=1 or lvl[x,y+1] !=1 or lvl[x+1,y+1] !=1 or lvl[x-1,y-1] !=1 or lvl[x,y-1] !=1 or lvl[x+1,y-1] !=1 or lvl[x-1,y] != 1 or lvl[x+1,y]!=1:
        #     res = False
        #     return res
        #ajouter cas ligne complète
        # else:
        return res
    
    def generate_level(self):
        #1 equal start
        self.get_lvl()[self.get_start_x(),self.get_start_y()] = 1
        #2 equal end
        self.get_lvl()[self.get_end_x(),self.get_end_y()] = 2 
        print(self.get_lvl())
        #-1 equal dead_zone
        i=0
        while i< self.get_nbdz():
            randx =  random.randint(0,19)
            randy = random.randint(0,19)
            if self.get_lvl()[randx,randy]==0 and self.can_be_place(randx,randy):
                #rajouter vérification pour éviter configuration bloqué
                self.get_lvl()[randx,randy] = -1
                i=i+1
        #print(self.get_lvl())
        self.save()
        
    def generate_level_from_save(self,tab_save):
    #Recreate the level as the save 
        
        for i in range(0,len(tab_save)):
            for j in range(0,len(tab_save[0])):
                self.get_lvl()[i,j] = tab_save[i][j]
        print(self.get_lvl())
                
        
    def save(self):
        cpt = 0
        folder = 'Ressources//saves'
        for path in os.listdir(folder):
            if os.path.isfile(os.path.join(folder,path)):
                cpt = cpt+1
        
        name = 'Ressources//saves//save_'+str(cpt)+'.json'
        json_lvl = self.get_lvl().tolist()
        with open(name,'w') as f:
            json.dump(json_lvl,f)
            
        
        


        