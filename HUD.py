import PyGine
class HUD(PyGine.Overlay) :
    def __init__(self,pl) :
        super().__init__()
        self.transform.position = PyGine.Vector3(0,0,0)
        self.addComponent( PyGine.TextComponent(self,"Money: 0",(0,0,0)) )
        self.player = pl

    def update(self,dt) :
        pass
        self.getComponent(PyGine.TextComponent).setText("Money: " + str(self.player.money))