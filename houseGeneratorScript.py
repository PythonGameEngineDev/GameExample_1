import PyGine
import random
from House import House
class houseGeneratorScript(PyGine.Component) :
    def start(self):
        for i in range(0,1000) :
            PyGine.Game.game.instanciate(House(random.randint(-100000,100000))) 