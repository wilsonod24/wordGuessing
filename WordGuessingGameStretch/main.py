import random
import os

#validation of user input
def isValid(x):
    try:
        x = eval(x)
        if (x >= 1) and (x <= 4):
            valid = True
        else:
            valid = False
    except:
        valid = False
    return valid

def validInput(x, y):
     #num = 0
     #try:
         #num = int(x)
     #except:
         #pass

     if x.lower == y.lower():
            return True

     if len(x) > 1:
         return False
     else:
         return True


#set initialization
movies = ["Back to the Future", "The Wolf of Wall Street", "Ferris Bueller's Day Off", "A Nightmare on Elm Street", "Rocky", "SuperBad","Fast and the Furious"]
shows = ["Rick and Morty", "The Office", "Greys Anatomy", "Breaking Bad", "The Sopranos", "That 70s Show", "The Mandalorian", "Invincible", "The Boys"]
sports = ["Badminton", "Soccer", "Football", "Bowling", "Track and Field", "Baseball", "Snowboarding", "Skiing", "Shuffleboarding"]
games = ["The Last of us", "Fortnite", "Super Mario World", "Mario Cart", "Halo", "Mortal Kombat", "PUBG", "Double Dragon"]


def main():
    #Variable initialization
    category, valid, correctAns, userProgress, gameOver, guesses, takenGuesses = 0, 0, 0, 0, 0, 7, 1
    correctLetters, incorrectLetters, catChosen = "", "", 0

    #Getting user input
    print("Choose a category for the game:")
    print("\n\t1: Movies\n\t2: TV Shows\n\t3: Sports\n\t4: Video Games")
    category = input()

    #running validation
    valid = isValid(category)

    #while loop for getting input when not valid input
    while not valid:
        print("Incorrect entry. Please enter a number 1-4 inclusive: ", end="")
        valid = isValid(input())

    #selecting category and phrase with random int
    category = eval(category)
    if category == 1:
        correctAns = random.choice(movies)
        catChosen = "Name of a Movie"
    elif category == 2:
        correctAns = random.choice(shows)
        catChosen = "Name of a Show"
    elif category == 3:
        correctAns = random.choice(sports)
        catChosen = "Name of a Sport"
    else:
        correctAns = random.choice(games)
        catChosen = "Name of a Video Game"
    userProgress = []
    userProgress += "_" * len(correctAns)
    win = False

    while (not gameOver and not win):
        os.system('cls')

        print("Category: ",catChosen)
        print("\n\tGuesses remaining: ",guesses,"\n")
        for y in range(0, len(userProgress)):
            if correctAns[y] == " ":
                print(" ", end="")
            else:
                print(userProgress[y], end="")
        print("\nCharacters in answer: ",correctLetters, "\nIncorrect Characters: ",incorrectLetters)




        print("\nPlease guess a letter in the word/phrase, guess the phrase, or 0 to end game: ",end="")
        userInput = input()

        if userInput.lower() == correctAns.lower():
            print("YOU WIN!\nIt took you",takenGuesses,"guesses.")
            win = True
            break

        #assigning true/false to valid
        valid = validInput(userInput, correctAns)

        #checking if valid
        while not valid:
            print("Invalid input or incorrect guess. Please enter a character or 0: ",end="")
            userInput = input()
            valid = validInput(userInput, correctAns)
            if userInput.lower() == correctAns.lower():
                print("YOU WIN!\nIt took you",takenGuesses,"guesses.")
                win = True
                break

        #ending game if user enters 0
        if userInput == "0":
            print("The correct answer was: ",correctAns)
            gameOver == True
            break

        lowerInput = userInput.lower()
        lowerAns = correctAns.lower()
        charNum = lowerAns.find(lowerInput)

        #INSERT HERE Code to check if input is in the phrase
        if lowerInput not in lowerAns:
            if (lowerInput not in incorrectLetters) and userInput not in correctAns:
                guesses -= 1
                incorrectLetters += userInput
                print("Sorry,",userInput,"is not in the word/phrase.")
            elif userInput in incorrectLetters:
                print("You have already entered this letter.")

        elif win:
            break

        else:
            if userInput not in correctLetters:
                correctLetters += (userInput*(correctAns.count(userInput.lower()))+ userInput*(correctAns.count(userInput.upper())))
                print(userInput,"is in the word/phrase", (correctAns.count(userInput.lower())+correctAns.count(userInput.upper())) ,"times!")
                for i in range(0,len(userProgress)):
                    if lowerInput in lowerAns[i]:
                        userProgress[i] = lowerInput
                #userProgress[charNum] = userInput
            else:
                print("You have already entered this letter.")


        takenGuesses += 1

        #running out of guesses
        if guesses == 0:
            print("You have run out of guesses. The correct answer was",correctAns,"\n-----------------------GAME OVER-----------------------")
            gameOver = True



main()