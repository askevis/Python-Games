import random

#picks a random word from a txt file
def pickRandWord():
        with open("C:/Users/denni/Desktop/lexicon.txt") as word_file:
            words = word_file.read().split()
            # TODO use filter()
            random_word = random.choice(words)
            while len(random_word) < 5:
                print("trying to find word")
                random_word = random.choice(words)
            print(random_word)
            return random_word

def guess(word,hidden):
      incorrect = list('______')
      win = False
      mistakes = 0
      while win != True:
        print(*hidden, sep='')
        print("Incorrect letters :", *incorrect, sep='')
        guesss = input("Please guess a letter : ")
        isunique = True
        for i in range(1, len(hidden)):
            if hidden[i-1] == guesss :
                print("This letter has already been chosen")
                isunique = False
                break
        for i in range(1, len(incorrect)):
            if incorrect[i-1] == guesss :
                print("This letter has already been chosen")
                isunique = False
                break
        if isunique == False:
            continue
        tempcorrect = False
        for i in range(1, len(word)+1):
            if word[i-1] == guesss:
                hidden[i-1] = guesss
                tempcorrect = True

        if tempcorrect == False:
            incorrect[mistakes] = guesss
            mistakes = mistakes + 1
            print("Incorrect!")
        else:
            print("Correct!")
        victory = False
        counter = 0
        for i in range(1, len(hidden)):
            if hidden[i]=='_':
                counter=counter +1
        if counter == 0:
            win = True
            print("You guessed the word! It was: ",*hidden, sep='')
        if mistakes == 6:
            win = True
            print("HANGED!")

print("Welcome to Hangman :")
gameon = True
while gameon == True:
 play = input("Play?(Y/y for yes N/n for no): ")
 if play=='Y' or play == 'y':
    word = pickRandWord()
    word = list(word)
    hidden = list('')
    for i in word:
        hidden.append('_')
    guess(word,hidden)

 elif play=='N' or play == 'n':
    print("Thank you for playing!")
    gameon = False
 else:
    print("Please enter Y/y or N/n")

