'''
import libraries as needed
Define and intialize the variables in each function
first create a list of words to pick from
    open file to get list of words
    get random word from dictionary
create function for playing the game
    loop to keep going if tries are greater than 0 and if the word is guessed
    check if they are guessing a letter or word and make sure isalpha
    otherwise tell them not a valid guess
    append list for incorrectly guessed letters to let them know they already made that guess
    append list of words to not penalize if they guess same word
    once out of tries or guessed the word ask if they want to play again
function for drawing out a picture or text?
    make list showing different stages of drawing
    make the drawing change as tries go down
    finaly with index 0 being final drawing
Main function
    grab random word from function
    keep track of wins and losses
    keep track of used words that are pulled from the list
    loop the play function until they do not want to play
    print results of W/L after they choose to stop playing
'''

# open json and put in dictionary
def randomWord():
    import random, json
    file = open('words_dictionary.json', 'r')
    dictionary = json.load(file)
    file.close()
    # get keys from dictionary and pick random word
    return random.choice(list(dictionary.keys())).upper()

def play(word):
    word_completion = "_" * len(word) 
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 7

    print("Let's play Hangman! Good Luck!")
    #print(drawing(tries)) # testing to see if it would show up before initiating wrong guess
    print(word_completion) # show length of word
    print('\n')
    # loop to going until guessed or still have tries
    while not guessed and tries > 0:
        guess = input("Guess a letter or word: ").upper()
        # if-else to check for letter or word or invalid entry 
        if len(guess) == 1 and guess.isalpha():
            # see if letter is already guessed
            if guess in guessedLetters:
                print(f'The letter {guess} has already been tried')
            # see if there guess is in the word
            elif guess not in word:
                print(guess, 'is not in the word')
                tries -= 1
                guessedLetters.append(guess)
            # if in word index through indices to find placement of letter   
            else:
                guessedLetters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                # if no more missing letters word is complete
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print(f'You have already tried guessing the word {guess}')
            elif guess != word:
                print("That is not correct")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("That is not a valid guess.")
        
        print(drawing(tries)) # to implement drawing
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you have won!")
        return 1
    else:
        print(f'You have lost! The word was {word} Better luck next time!')

def drawing(tries):
    levels = [
             '''
                ____    ____  ______    __    __      __        ______        _______. _______  __  
                \   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____||  | 
                 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   |  | 
                  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  |  | 
                    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ |__| 
                    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|(__) 
                                                                                   
             ''',
             '''
                ____    ____  ______    __    __      __        ______        _______. _______  
                \   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|
                 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
                  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  
                    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
                    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|
             ''',
             '''
                ____    ____  ______    __    __      __        ______        _______. 
                \   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       |
                 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`
                  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    
                    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |    
                    |__|     \______/   \______/     |_______| \______/  |_______/    
             ''',
             '''
                ____    ____  ______    __    __      __        ______   
                \   \  /   / /  __  \  |  |  |  |    |  |      /  __  \  
                  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  | 
                    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | 
                    |__|     \______/   \______/     |_______| \______/  
             ''',
             '''
                ____    ____  ______    __    __      __         
                \   \  /   / /  __  \  |  |  |  |    |  |     
                  \_    _/  |  |  |  | |  |  |  |    |  |     
                    |  |    |  `--'  | |  `--'  |    |  `----.
                    |__|     \______/   \______/     |_______| 
             ''',
             '''
                ____    ____  ______    __    __     
                \   \  /   / /  __  \  |  |  |  |   
                  \_    _/  |  |  |  | |  |  |  |    
                    |  |    |  `--'  | |  `--'  |    
                    |__|     \______/   \______/    
             ''',
             '''
                ____    ____  ______     
                \   \  /   / /  __  \  
                  \_    _/  |  |  |  | 
                    |  |    |  `--'  | 
                    |__|     \______/  
             ''',
             '''
                ____    ____  
                \   \  /   / 
                  \_    _/  
                    |  |    
                    |__|    
             '''  
    ]
    return levels[tries]

def main():
    usedWords = []
    wins, losses = 0, 0
    result = 0
    if result == 1:
        wins += 1
    else:
        losses += 1
    word = randomWord()
    usedWords.append(word)
    play(word)
    while input('Do you want to play again? (Y/N): ').upper() == "Y":
        word = randomWord()
        if word in usedWords:
            word = randomWord()
            usedWords.append(word)
        else:
            usedWords.append(word)

        result = play(word)
        if result == 1:
            wins += 1
        else:
            losses += 1
    print(f'Your results:\n Win count: {wins}\n Loss count: {losses}')
    # print(usedWords) # testing to make sure randomWord is getting put in usedWords

if __name__ == '__main__':
    main()