#MODULES AND GLOBALS
import random 
import sys

file1 = open(r"fiveletterwords.txt","r")  
allFiveLetterWords = file1.readlines() 


#CLASSES 
class allwords(): 
    def __init__ (self, word):
        self.word = word

    #chooses a wordle "secret" word
    def chooseSecretWord (self): 
        global allFiveLetterWords

        indNumber = random.randint(1, 5758)
        choice = allFiveLetterWords[indNumber]
        choice = choice.rstrip(choice[-1])
        self.word = choice

    #Gets guess from player's keyboard
    def getGuessFromPlayer (self):
        goodChoice = False
        while goodChoice == False:
            self.word = input ("Enter your guess:")
            self.word = self.word.lower()

            if (len(self.word) == 6): 
                if self.word[5] == " ":
                    self.word = self.word.rstrip(self.word[-1])

            if (len (self.word) != 5):
                print ("Not a valid guess!")
                continue
            elif (len(self.word) == 5):
                self.word = self.word.lower() 
                self.word = self.word + "\n"
                if (self.word in allFiveLetterWords) == False:
                    print ("Not a valid guess!")
                    continue
                self.word = self.word.rstrip(self.word[-1])
                goodChoice = True

        
    #Changes the background color of letters in each guess
    def colorLetters (self, playerGuess, secretWord): 
        for x in range (0,len(playerGuess)):
                if playerGuess[x] == secretWord[x]: #Change to green; 
                    print ("\u001b[42;1m", playerGuess[x], "\u001b[0m", end= ' ')
                elif ((playerGuess[x] in secretWord) == True): #change to yellow
                    print ("\u001b[43m", playerGuess[x], "\u001b[0m", end= ' ')
                else: #keep gray
                    print (playerGuess[x], end=' ')


#Close the five letter word dictionary
file1.close()



