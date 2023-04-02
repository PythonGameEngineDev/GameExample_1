import PyGine
from Money import Money
import pygame
class Player(PyGine.GameObject) :
    def start(self) :
        self.transform.position = PyGine.Vector3(100,200,0)
        

        sp = self.addComponent(PyGine.SpriteComponent(self,"melting.png"))
        self.transform.scale = PyGine.Vector3(50,100,0)
        self.tracked = True
        self.money = 10
        self.counter = 0
        
    def update(self,dt) :
        
        if self.counter > 100 :
            self.money += 1
            self.counter = 0
        speed = 1
        if PyGine.KeyListener.getPressed_Hold(pygame.K_LSHIFT):
            speed = 2

        if PyGine.KeyListener.getPressed_Hold(ord("d")):
            self.transform.position.x += speed

        if PyGine.KeyListener.getPressed_Hold(ord("q")):
            self.transform.position.x -= speed

        if(PyGine.KeyListener.getPressed_Click(ord("s"))):
            self.dropMoney()
        
        self.counter += 1

    def dropMoney(self) :
        if self.money > 0 :
            self.money -= 1
            PyGine.Game.game.instanciate(Money(self.transform.position.x))
            print("dropMoney")
        else :
            print("No more money")