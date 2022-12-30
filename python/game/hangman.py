import time
import random

turns = 10

print("Hello, Let's play hangman! You will have " + str(turns) + " turns!")

print("")

# delay
time.sleep(0.5)

# set of words to guess from
wordList = ["apple", "awesome", "orange", "magic", "orchestra", "steak", "weakness", "battlefield", "valley", "ban", "senior", "promise", "suppress", "revolution", "stock", "member", "evaluate", "eavesdrop", "population", "hesitate", "shatter", "height", "drill", "coma", "use", "reconcile", "rain", "heaven", "score", "literacy", "swarm", "offer", "tolerate", "define"]
word = random.choice(wordList)
raw_inport = 0
guesses = ''

# loop till no turns are remaining
while turns > 0:         
    wrong = 0             

    for char in word:      
        if char in guesses:    
            print(char),    
        else:
            print("_"),     
            wrong += 1    
    print("")        
    print("you have guessed: " + guesses)
    # print("\n")

    if wrong == 0:        
        print("You won :)")  
        print("the word was " + word)
        break              

    print("")

    guess = ''
    if len(guess) < 1:
        guess = input("Guess a character or enter the correct word: ")[0]

    guesses += guess                    

    if guess not in word:  
        turns -= 1        
 
        print("Wrong")    
 
        print("You have", + turns, ' turns left!') 
 
        if turns == 0:           
    
            print("You Lose :(")
            print("the word was " + word)
