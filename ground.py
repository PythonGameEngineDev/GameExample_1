import PyGine
class ground(PyGine.Overlay) :
    def __init__(self) :
        super().__init__()
        self.transform.position = PyGine.Vector3(0,350,0)
        self.transform.scale = PyGine.Vector3(800,300,0)
        self.addComponent( PyGine.DrawRectComponent(self,(0,100,0)) )

