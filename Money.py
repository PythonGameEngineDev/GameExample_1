import PyGine
class Money(PyGine.GameObject) :
    Count = 0
    def __init__(self,x) :
        super().__init__()
        self.transform.position = PyGine.Vector3(x,300-10,0)
        self.counter = 0        
    def start(self) :
        Money.Count += 1
        self.addComponent( PyGine.DrawRectComponent(self,(100,0,100)) )
        self.transform.scale = PyGine.Vector3(10,10,0)
        print("Money start",Money.Count)


    def update(self,dt) :
        self.counter += 1
        if self.counter > 100 :
            Money.Count -= 1
            self.destroy = True