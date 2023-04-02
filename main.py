import PyGine
from Island_1 import Island_1
class game(PyGine.Game) :
    def __init__(self) :
        super().__init__(800,500,self)
        self.addScene(Island_1())
        self.setScene(1)
        self.fps = 60
        self.setImageLibFolder("Assets")
        

game().run()

    