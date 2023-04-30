import game
import level
import numpy as np
class Qlearning:
    UP = 1
    RIGHT =2
    DOWN = 3
    LEFT = 4
    actions = [UP,RIGHT,LEFT,DOWN]
    def __init__(self,lvl):
        #Only for actions (UP,RIGHT,DOWN,LEFT)
        self.Qtable = np.zeros(lvl.get_nbzones(),4)