import wordclasses
import sys

#edit counter so it actually ends the game!!
#MAIN GAME LOOP        
def main():
    counter = 1
    welcome = "Welcome to wordle! Guess what 5 letter word I'm thinking of..."
    print (welcome)

    gameOver = False
    wordle = wordclasses.allwords("YYYYY")
    wordle.chooseSecretWord()
    alreadyGuessed = ["XXXXX"]
    guess = wordclasses.allwords("XXXXX")

    while gameOver == False: 
        while (guess.word in alreadyGuessed) == True:
            guess.getGuessFromPlayer()

        if guess.word == wordle.word:
            print ("You win!!! The secret word was", wordle.word)
            gameOver = True
            sys.exit()
        elif guess.word != wordle.word: 
            if counter == 6:
                print ("Game over! The word was", wordle.word, "\n Better luck next time!")
                sys.exit()
            alreadyGuessed.append(guess)
            guess.colorLetters(guess.word, wordle.word)
            alreadyGuessed[counter] = guess.word 
            # print (alreadyGuessed, sep = '\n') 
            counter += 1
            print ("Guesses remaining:", (7 - counter))





if __name__ == "__main__":
    main()

