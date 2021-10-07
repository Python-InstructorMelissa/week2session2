import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        ninja.defend(self)
        return self

    def defend(self, ninja):
        rng = random.randint(1,2)
        if rng == 2:
            ninja.health -= round(self.strength/2)
            print(f"{self.name} defended back against {ninja.name}\nHealth: {self.health}\n{ninja.name}\nHealth: {ninja.health}")
        else:
            print(f"{self.name} failed to defend against {ninja.name}\nHealth: {self.health}\n")