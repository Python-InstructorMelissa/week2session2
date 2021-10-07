import random
class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        pirate.defend(self)
        return self

    def defend(self, pirate):
        rng = random.randint(1,2)
        if rng == 2:
            pirate.health -= round(self.strength/2)
            print(f"{self.name} defended back against {pirate.name}\nHealth: {self.health}\n{pirate.name}\nHealth: {pirate.health}")
        else:
            print(f"{self.name} failed to defend against {pirate.name}\nHealth: {self.health}\n")