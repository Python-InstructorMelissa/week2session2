"""
LIne 9-10 = Importing the 2 class files
line 12 & 14 = 1 ninja instance and 1 pirate instance have been created
- line 15 ninja michelangelo is calling the attack method and attacking the pirate jack sparrow
- line 16 = Pirate jack sparrow is calling the show stats method
This file is how we will play our game
"""

from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo", 20)

jack_sparrow = Pirate("Jack Sparrow", 10)

janeDoe = Ninja("Jane Doe", 15)

johnSmith = Pirate("John Smith", 10)

melissa = Ninja("Melissa", 10)

# jack_sparrow.show_stats()
# michelangelo.show_stats()
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# jack_sparrow.attack(janeDoe)

pPlayers = []
nPlayers = []
teamNinja = []
teamPirates = []

nPlayers.append(michelangelo)
pPlayers.append(jack_sparrow)
nPlayers.append(janeDoe)
pPlayers.append(johnSmith)
nPlayers.append(melissa)

teamNinja.append(michelangelo.name)
teamPirates.append(jack_sparrow.name)
teamNinja.append(janeDoe.name)
teamPirates.append(johnSmith.name)
teamNinja.append(melissa.name)

# print(teamNinja)
# print(teamPirates)

def totalNinjaHealth(arr):
    nHealth = 0
    for n in arr:
        nHealth += n.health
    print(f"Team Ninja current health total: {nHealth}")
    return nHealth

# totalNinjaHealth(nPlayers)

def totalPirateHealth(arr):
    pHealth = 0
    for p in arr:
        pHealth += p.health
    print(f"Team Pirate current health total: {pHealth}")
    return pHealth

# totalPirateHealth(pPlayers)


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

# loop(nPlayers, pPlayers)

def gamePlay(arr01, arr02, arr03, arr04):
    print(f"Team Ninja Players: {arr01}\n")
    print(f'Team Pirates Players: {arr02}\n')
    nHealth = totalNinjaHealth(nPlayers)
    pHealth = totalPirateHealth(pPlayers)
    if nHealth > 0 and pHealth > 0:
        # print(f"Ninja Health: {nHealth}\nPirate Health: {pHealth}")
        if nHealth == pHealth:
            for p in arr04:
                for n in arr03:
                    p.attack(n)
                    nHealth = totalNinjaHealth(nPlayers)
                    pHealth = totalPirateHealth(pPlayers)
                # print(f"Ninja Health: {nHealth}\nPirate Health: {pHealth}")
            print(f"Ninja Health: {nHealth}\nPirate Health: {pHealth}\n")
        if nHealth > pHealth and pHealth > 0:
            for n in arr03:
                for p in arr04:
                    n.attack(p)
                    nHealth = totalNinjaHealth(nPlayers)
                    pHealth = totalPirateHealth(pPlayers)
            print(f"Ninja Health: {nHealth}\nPirate Health: {pHealth}\n")
        if pHealth > nHealth and nHealth > 0:
            for p in arr04:
                for n in arr03:
                    p.attack(n)
                    nHealth = totalNinjaHealth(nPlayers)
                    pHealth = totalPirateHealth(pPlayers)
            print(f"Ninja Health: {nHealth}\nPirate Health: {pHealth}\n")
        if nHealth > pHealth and pHealth < 0:
            print("The Ninja's Win!")
        if pHealth > nHealth and nHealth < 0:
            print("The Pirates Win!")
    if nHealth == 0:
        print("The Pirates Won!")
        return 0
    if pHealth == 0:
        print("The Ninjas Won!")
        return 0
    else:
        print("No one was left standing!")

gamePlay(teamNinja, teamPirates, nPlayers, pPlayers)
print("Round 1 Complete\n")
# gamePlay(teamNinja, teamPirates, nPlayers, pPlayers)
# print("Round 2 Complete\n")
# gamePlay(teamNinja, teamPirates, nPlayers, pPlayers)
# print("Round 3 Complete\n")
# gamePlay(teamNinja, teamPirates, nPlayers, pPlayers)
# print("Round 4 Complete\n")
# gamePlay(teamNinja, teamPirates, nPlayers, pPlayers)
# print("Round 5 Complete")

# nHealth = totalNinjaHealth(nPlayers)
# pHealth = totalPirateHealth(pPlayers)