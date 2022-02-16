from datetime import datetime
from os import system, name

from messages import *


def clear():
    if name  =='nt':
        _ = system('clear')
    else:
        _ = system('clear')

playing = True
now = datetime.now()
currentTime = now.strftime("%H:%M")
while playing:
    clear()
    message = print(f'{welcome}')
    message = print(f'The current time is {currentTime}EST')
    mesage = input(f'\nWould you like to play a game?\n\ny or n\n')
    if message[0] == 'n':
        message = print({noGame})
        playing = False
    else:
        message = print({yesGame})
        clear()
        playing = False