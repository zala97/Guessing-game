import random

def guessing_game ():
    numb = random.randint(0,100)
    count = 0
    while (True):
        guess = int(input ("enter a number"))
        if guess > numb:
            print ("much")
        elif guess < numb:
            print ("low")
        else:
            print("true")
        count = count + 1
        if count==3:
            print("done")
            
            break
    

    
guessing_game()