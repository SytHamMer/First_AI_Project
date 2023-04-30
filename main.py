import game
import level
import saves_reader
from level import *
if __name__ == "__main__":
    
   #saves_reader.read_save("save_0.json")

   #game.create_game(75,(0,0),(19,19))
   game.create_game_from_save("save_0.json")