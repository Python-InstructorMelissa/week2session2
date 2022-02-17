from .trick import Trick

class Pet: # the name of the class must always be capitalized
    def __init__(self, name, gender, breed, age): # constructor function tells us or defines the attributes that each instance of the class can have
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.markings = None
        self.food = None
        self.tricks = []
    
    def printPet(self):
        print(f'{self.name} is a {self.gender} {self.breed} dog that is {self.age} old.')
        return self

    def eat(self, food):
        self.food = food.name
        print(f'{self.name} likes to eat {self.food}')
        return self

    def addMarkings(self, markings):
        self.markings = markings
        # print(f'{self.name} has the following colors or markings: {self.markings}')
        return self
    
    def printMarkings(self):
        print(f'{self.name} has the following colors or markings: {self.markings}')
        return self

    def printTricks(self):
        theTricks = [] # creates a special internal list
        for t in self.tricks: # loop through the instance list of tricks
            theTricks.append(t.trickName) # add just the name of the trick to the special internal list
        print(f"{self.name} can do the following tricks or trick: {theTricks}") # here we call the internal list as that has just the names of the tricks not the whole instance that includes the difficulty
        return self

    def addTrick(self, trick):
        self.tricks.append(trick)
        self.printTricks()
        

    def forgotTrick(self, trick):
        self.tricks.pop(trick)

    # def increasedTrick(self):
    #     print(f'{self.name} made the following accomplishment: {self.name.trick(Trick.leveledUpTrick())}')