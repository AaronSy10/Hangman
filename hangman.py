import random
from words import words
import string

def getword(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def play():
    word=getword(words).upper() #get word from words
    wletters=set(word) #put the letters of the word into a set
    guessedletters=set() #create a set for guessed letters
    prevletters=set() #create set for correctly guessed letters
    correctletters=set(string.ascii_uppercase) #input checker
    lives=7
    while lives>0:
        if lives==7: #life indicator
            hearts='\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f'
        elif lives==6:
            hearts='\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f'
        elif lives==5:
            hearts='\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f'
        elif lives==4:
            hearts='\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f'
        elif lives==3:
            hearts='\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f'
        elif lives==2:
            hearts='\u2764\ufe0f \u2764\ufe0f'
        elif lives==1:
            hearts='\u2764\ufe0f'
        check=all(item in guessedletters for item in wletters) #checks if the word is guessed
        if check is True: #the word is guessed
            print('\n\U0001F3C6\U0001F3C6\U0001F3C6 You won!! \U0001F3C6\U0001F3C6\U0001F3C6\n\n\n')
            playagain()
        else:
            i=1
            while i==1:
                currentword=[letter if letter in guessedletters else '_' for letter in word] #letter if the letter of the word is in guessedletter and _ for letters in the word not in guessedletters
                print('Guess the word: ',' '.join(currentword),'       Lives: ',hearts)
                print('Guessed letters: ', ' '.join(guessedletters))
                gletter=input('Guess a letter: ').upper() #get the user input for letter guess and converts it to uppercase
                if gletter in correctletters:
                    guessedletters.add(gletter) #add guessed letter to set of guessed letters
                    i+=1
                elif gletter not in correctletters: #checks if the input is from A-Z only
                    print('\nInvalid Input')
            if gletter not in word: #wrong guess
                print('\nWrong guess')
                lives-=1
            elif gletter in prevletters: #duplicate guess
                print('\nYou already guessed the letter')
                lives-=1
            print('')
            prevletters.add(gletter) #adds the letter to the used letters 

    print('\U0001F480\U0001F480\U0001F480 Game Over \U0001F480\U0001F480\U0001F480')
    print('Correct word is',word)
    playagain()

def playagain(): #for user to be able to play again
    counter=1
    while counter==1:
        digit=input('Want to play again? [1] YES [2] NO: ')
        if digit=='1':
            counter-=1
            print('\n\n\n\n\n')
            play()
        elif digit=='2':
            quit()
        else:
            print('Invalid Input')
play()