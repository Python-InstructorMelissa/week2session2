from classes.deck import Deck
from classes.player import Player
from os import system, name

# if using CMD prompt change the word clear to cls or it won't work as that is it's command to clear
def clear():
    if name =='nt':
        _ = system('clear')
    else:
        _ = system('clear')

bicycle = Deck()

bicycle.show_cards()
clear()
game = True
while game:
    name1 = str(input("Please let us know your name player 1:  "))
    player1 = Player(name1)
    name2 = str(input("Please let us know your name player 2:  "))
    player2 = Player(name2)
    print(f"Welcome {player1.name} and {player2.name} to our game")
    game = False
