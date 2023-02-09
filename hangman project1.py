# steps breaking down

import random
import time

# Initial Steps to invite in the game:
print("\nWelcome to Hangman game by Muhammad Soliman\n")
name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(1)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(1)


# The parameters we require to execute the game, using Global
def main():
    # count is how many tries
    global count
    # to display the graph for the hangman on every wrong guess
    global display
    # the chossen random word
    global word

    global already_guessed
    global length
    global play_game
    # Random guessed word from this list
    words_to_guess = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
    # choose a random word
    word = random.choice(words_to_guess)

    length = len(word)
    # the count of the tries so we can increase the and decress the tries as much as we want
    count = 0
    # the display pf the guessed and non guessed words
    display = '_' * length
    # for the letter that already guessed so the play don't reguess over the same letter
    already_guessed = []
    play_game = ""

# A loop to re-execute the game when the first round ends which includes the input to play again or not

def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()

# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    # limit the number of chances to 6
    limit = 6
    # input player Guessed letter
    guess = input("This is the Hangman Word: " + display + " Enter your guess:")
    guess = guess.strip()
    # function  to limit the wrong inputs as an invalid entery
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2:
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")


        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()