from random import randint

board = {7: ' ' , 8: ' ' , 9: ' ' ,
            4: ' ' , 5: ' ' , 6: ' ' ,
            1: ' ' , 2: ' ' , 3: ' ' }


#setting up the board
def displayBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

#play game, user vs computer
def play_game():
    userinput="Q"    
    while userinput =="Q":
        userinput = input("Do you want to be X or O? ")
        if userinput=="X":
            player = 'X'
            comp="O"
        elif userinput=="O":
            player="O"
            comp="X"
        else:
            userinput = "Q"
            print("Invalid data. Enter X or O ")
            
    count = 0
        
    for i in range(9):
        displayBoard(board)
        
        #users turn
        if i%2==0:
            print(f"It's your turn. Choose a space to put your {player}")

            flag_a=True
            while flag_a:
                move = int(input())        

                if board[move] == ' ':
                    board[move] = player
                    count += 1
                    flag_a=False
                
                else:
                    print(f"That place is already filled.\nChoose a different space to put your {player}")
        #computers turn        
        else:
            flag = True
            while flag:
                comp_move=randint(1,9)
                # print(comp_move)
                if board[comp_move]==" ":
                    board[comp_move]= comp
                    count+=1
                    print(f"count is {count}")
                    print(f"The computer put an {comp} in space {comp_move}")
                    flag=False 
                 
        #results
        if board[7] == board[8] == board[9] != ' ': 
            displayBoard(board)
            print(f"Game Over. {board[7]} won.")                               
            break
        elif board[4] == board[5] == board[6] != ' ': 
            displayBoard(board)
            print(f"Game Over.{board[4]} won.")               
            break
        elif board[1] == board[2] == board[3] != ' ':
            displayBoard(board)
            print(f"Game Over. {board[1]} won.")                 
            break
        elif board[1] == board[4] == board[7] != ' ':
            displayBoard(board)
            print(f"Game Over. {board[7]} won.")                
            break
        elif board[2] == board[5] == board[8] != ' ':
            displayBoard(board)
            print(f"Game Over. {board[2]} won.")                
            break
        elif board[3] == board[6] == board[9] != ' ':
            displayBoard(board)
            print(f"Game Over. {board[3]} won.")                 
            break 
        elif board[7] == board[5] == board[3] != ' ':
            displayBoard(board)
            print(f"Game Over.{board[7]} won.")                
            break
        elif board[1] == board[5] == board[9] != ' ':
            displayBoard(board)               
            print(f"Game Over. {board[1]} won.")                
            break 
            
        if count == 9:
            print("Game Over")             

play_game()
