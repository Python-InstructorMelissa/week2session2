import random
class Ninja:

    def __init__( self , name, strength ):
        self.name = name
        self.strength = strength
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print(f"{self.name} deals an attack on {pirate.name}")
        pirate.defend(self)
        return self

    def defend(self, pirate):
        rng = random.randint(1,2)
        if rng == 2:
            pirate.health -= round(self.strength/2)
            # print(f"{self.name} defended back against {pirate.name}\n{self.name}'s Health: {self.health}\n{pirate.name}'s Health: {pirate.health}")
            print(f"{self.name} defended against {pirate.name}\n")
        else:
            # print(f"{self.name} failed to defend against {pirate.name}\nHealth: {self.health}\n")
            print(f"{self.name} failed to defend against {pirate.name}\n")