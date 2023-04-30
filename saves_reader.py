import level
from level import *


def read_save(save):
    with open("Ressources/saves/"+ save,'r') as f:
        data = json.load(f)
    nbdz = 0
    for i in range(0,len(data)):
        for j in range(0,len(data[i])):
            if data[i][j] == -1:
                nbdz=nbdz+1
            elif data[i][j]==1:
                tuplestart =(i,j)
            elif data[i][j]==2:
                tupleend = (i,j)
    lvl = Level(nbdz,tuplestart,tupleend)
    lvl.generate_level_from_save(data)
    return lvl
            