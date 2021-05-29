#class and methods for RockPaperScissors
class Game():
    def __init__(self):
        self.results={"You Won":0,"You Lost":0,"You Tied":0}

    def get_user_item(self):
        flag=True
        while flag:
            choice=input('''
Select (r)ock, (p)aper or (s)cissors:  ''')
            if choice == "r":
                return "r"
            elif choice=="p":
                return "p"
            elif choice=="s":
                return "s"
            else:
                print("Invalid entry. Try again. ")

    def get_computer_item(self):
        return random.choice(["r","p","s"])
    
    def get_game_result(self,user_item,computer_item):
        if user_item==computer_item:
            self.results["You Tied"]+=1
            return "It's a tie"
        elif user_item=="r" and computer_item == "p" or user_item == "s" and computer_item == "r" or user_item == "p" and computer_item == "s":
            self.results["You Lost"]+=1
            return("You Lost")
        elif user_item == "r" and computer_item == "s" or user_item == "s" and computer_item == "p" or user_item == "p" and computer_item == "r":
            self.results["You Won"]+=1
            return("You Won")
        else:
            return("ERROR")
 
    def play(self):
        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        result=self.get_game_result(user_item,computer_item)
        print(f"You chose {user_item}. The computer chose {computer_item}. {result}! ")
