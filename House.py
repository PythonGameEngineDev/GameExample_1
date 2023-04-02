import PyGine
class House(PyGine.GameObject) :
    def __init__(self,x) :
        super().__init__()
        self.transform.position = PyGine.Vector3(x,200-10,0)
        self.transform.scale = PyGine.Vector3(100,110,0)
        self.addComponent( PyGine.DrawRectComponent(self,(100,50,20)))