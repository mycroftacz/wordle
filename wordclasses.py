"""WORDLE"""
#MODULES AND GLOBALS
import random 
import sys

file1 = open(r"fiveletterwords.txt","r") #Import the file (give file path) #second r might not be necessary 
allFiveLetterWords = file1.readlines() #Read each line and save it as a list of strings



#CLASSES 
class allwords(): 
    def __init__ (self, word):
        self.word = word

    def chooseSecretWord (self): 
        global allFiveLetterWords

        indNumber = random.randint(1, 5758)
        choice = allFiveLetterWords[indNumber]
        choice = choice.rstrip(choice[-1])
        self.word = choice

    def getGuessFromPlayer (self): #add protection against special characters
        goodChoice = False
        while goodChoice == False:
            self.word = input ("Enter your guess:")
            self.word = self.word.lower()
            
            if (len (self.word) != 5):
                print ("Not a valid guess!")
                continue
            elif (len(self.word) == 5):
                self.word = self.word.lower() #FIX THIS SO IT FORCES USER TO PICK A VALID WORD
                self.word = self.word + "\n"
                if (self.word in allFiveLetterWords) == False:
                    print ("Not a valid guess!")
                    continue
                self.word = self.word.rstrip(self.word[-1])
                goodChoice = True

        

    def colorLetters (self, playerGuess, secretWord): # can this accomodate all the logic of the game? Add ANSI colors!
        for x in range (0,len(playerGuess)):
                if playerGuess[x] == secretWord[x]: #Change to green; "String index out of range?"
                    print ("\u001b[42;1m", playerGuess[x], "\u001b[0m", end= ' ')
                elif ((playerGuess[x] in secretWord) == True): #change to yellow
                    print ("\u001b[43m", playerGuess[x], "\u001b[0m", end= ' ')
                else: #keep gray
                    print (playerGuess[x], end=' ')


#is this code right? 
file1.close()


""" NOTES
class secretWord():
    #Constructor
    def __init__ (self, secretWord):
        self.secretWord = secretWord

    # This is the template for a function (next two lines)
    #def method (self, parameter):
    #   self.parameter = parameter

    def chooseSecretWord (self, secretWord): #Returns secret word choice
        global allFiveLetterWords

        indNumber = random.randint(1, 5758)
        choice = allFiveLetterWords[indNumber]
        self.secretWord = choice
    
    def printSecretWord (self, secretWord):
        print (secretWord)

"""
