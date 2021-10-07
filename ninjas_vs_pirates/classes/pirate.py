import random

class Pirate:

    def __init__( self , name, strength ):
        self.name = name
        self.strength = strength
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print(f"{self.name} deals and attack on {ninja.name}")
        ninja.defend(self)
        return self

    def defend(self, ninja):
        rng = random.randint(1,2)
        if rng == 2:
            ninja.health -= round(self.strength/2)
            # print(f"{self.name} defended back against {ninja.name}\nHealth: {self.health}\n{ninja.name}\nHealth: {ninja.health}")
            print(f"{self.name} defended against {ninja.name}\n")
        else:
            # print(f"{self.name} failed to defend against {ninja.name}\nHealth: {self.health}\n")
            print(f"{self.name} failed to defend against {ninja.name}\n")