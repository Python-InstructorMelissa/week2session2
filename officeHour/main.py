from classes.food import Food
from classes.owner import Owner
from classes.pet import Pet
from classes.trick import Trick

# Use a for loop when you know there is a possibility that more than one answer could be returned

# Creating instances of our Pet class
copper = Pet('Copper', 'Male', 'Beagle', '1 year')
bear = Pet('Bear', 'Male', 'Shepherd Mix', '7 years')
roxy = Pet('Roxy Mae', 'Female', 'Red nose Pit Shepherd mix', '1.5 years')
lucy = Pet('Lucy', 'Female', 'Chawinnie', '5 years')

# Creating instances of Owners
melissa = Owner('Melissa')

# Creating an instance of Food
beneful = Food('Beneful')

# Creating trick instances
jump = Trick('Jumping Bricks', 2)
sit = Trick('Sit when told', 2)
speak = Trick('Bark on command', 1)
dance = Trick('Dance when asked', 9)
paw = Trick('Give 5 or shake hands', 5)

# Using our methods
copper.printPet()
bear.printPet()

melissa.addPet(copper)
melissa.addPet(bear)

roxy.eat(beneful)

roxy.addMarkings('Tan/White with a white spot')
roxy.printPet().printMarkings()

bear.addTrick(sit)
bear.addTrick(speak)
bear.addTrick(jump)

sit.leveledUpTrick(4)
# bear['sit'].increasedTrick(4)