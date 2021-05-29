import random

# import game class
from game import *

# user interface to start or exit the game
def get_user_menu_choice(object):
    flag=True
    while flag:
        menu_choice=input('''
Menu:
(g) Play a new game
(x) Show results and exit  ''').lower()
        if menu_choice=="g":
            object.play()
        elif menu_choice=="x":
            print_results(object)
            flag=False
        else:
            print ("Invalid entry. Try again. ")
    
# prints results of all wins/losses stored in game's dict
def print_results(object):
    for k,v in object.results.items():
        print(f"{k} {v} time(s)") 

def main():
    new_game=Game()
    get_user_menu_choice(new_game)

main()
