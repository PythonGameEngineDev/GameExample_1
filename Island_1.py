import PyGine
from Player import Player
from HUD import HUD
from ground import ground
from houseGenerator import houseGenerator
class Island_1(PyGine.Scene) :
    def start(self):
        print("Island_1 start")
        PyGine.Game.game.setBgColor((100,0,0))

        self.addGameObject(ground())
        self.addGameObject(houseGenerator())
        pl = self.addGameObject(Player())
        self.addGameObject(HUD(pl))