"""
LIne 9-10 = Importing the 2 class files
line 12 & 14 = 1 ninja instance and 1 pirate instance have been created
- line 15 ninja michelangelo is calling the attack method and attacking the pirate jack sparrow
- line 16 = Pirate jack sparrow is calling the show stats method
This file is how we will play our game
"""

from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

janeDoe = Ninja("Jane Doe")

johnSmith = Pirate("John Smith")

jack_sparrow.show_stats()
michelangelo.show_stats()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# jack_sparrow.attack(janeDoe)

pPlayers = []
nPlayers = []
nPlayers.append(michelangelo)
pPlayers.append(jack_sparrow)
nPlayers.append(janeDoe)
pPlayers.append(johnSmith)



def loop(arr01, arr02):
    game = True
    while game:
        for n in arr01:
            if n.health < 0:
                arr01.remove(n)
                if len(arr01) == 0:
                    print(f"The Pirates Won!")
                    game = False
                    return 0
            else:
                for p in arr02:
                    n.attack(p)
        for p in arr02:
            if p.health < 0:
                arr02.remove(p)
                if len(arr02) == 0:
                    print(f"Ninja's Won!")
                    game = False
                    return 0
            else:
                for n in arr01:
                    p.attack(n)

loop(nPlayers, pPlayers)