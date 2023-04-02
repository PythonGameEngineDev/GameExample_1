import PyGine
from houseGeneratorScript import houseGeneratorScript
class houseGenerator(PyGine.GameObject) :
    
    def __init__(self):
        super().__init__()
        self.addComponent(houseGeneratorScript(self))