import random

# function to check for all occurrences of letter in word 
def getallindexes(arr, val):
    indexes = []
    i=0
    while i<len(arr):
        if arr[i] == val:
            indexes.append(i)
        i+=1
    return indexes;

def hangman():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'creditcard', 'rush', 'south']
    word = random.choice(wordslist) 
    print(word)
    
    # create array of word
    arrword=list(word)
    # create corresponding array for stars/results
    arrhangman=["*" for i in arrword]
    # # counter gives you 10 chances
    counter=0
    # checks how many stars were replaced with letters
    wincount=0
    # array of letters guessed already
    used = []
    
    while counter<10:
        letter = input("Player2: Enter a letter: ")
        letter=letter.lower()
        # In your code prevent player 2 from guessing the same letter twice.
        if letter in used:
            print("You used that letter already. Guess again")
            # if guess is in word
        elif letter in arrword:
                # replaces all indices of letter
                temparr= getallindexes(arrword, letter)
                f=0
                while f<len(temparr):
                    arrhangman[temparr[f]]=letter
                    wincount+=1
                    f+=1
                used.append(letter)
                print("Good guess!")
                print(arrhangman)
                print(f"You used these letters: {used}")
                
                # checks if you solved the whole word
                if wincount == len(arrword):
                    print(f"Congrats! You win! The word was {word}")
                    return
    
        else:
                # guess is not in word, reprompt
            used.append(letter);
            print("Nope. Try again")
            print(f"You used these letters: {used}")
            counter+=1
            print(f"You used {counter} out of 10 chances")

    print(f"You lose. The word was {word}")
    return


hangman()
