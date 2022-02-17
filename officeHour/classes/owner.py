class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def printOwner(self):
        print(f'{self.name} is a pet owner')

    def printPetsOwned(self):
        thePets = []
        for p in self.pets:
            thePets.append(p.name)
        print(f'{self.name} owns the following pet or pets {thePets}')
    
    def addPet(self, pet):
        self.pets.append(pet) #self = the instance we are using of owner pets = an attribute of the owner that is optional in our constructor and is a empty list.  Append = adding too the end (pet) the pet instance that we want to add to the list
        self.printPetsOwned()
        return self