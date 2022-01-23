import random
import time
print("\nBe prepared to hang an innocent dude\n")
name = input("Enter your name here,contestant: ")
print("Hey " + name + "Try not to kill him")
time.sleep(2)
print("Time to play champ!\nMake sure that no one in your house witnesses you killing an innocent person!")
time.sleep(3)
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["johnny","Banana","Loyola","Dean","Pattarai","Discord","Coding","President","Avengers","Itachi","Eminem"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
def play_loop():
    global play_game
    play_game = input("Do You want to kill another person? y = yes, n = no \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("Do You want to kill another person? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Hope you had a great time champ! Happy Killing!")
        exit()
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Mystery word " + display + " Enter your answer here,hope you don't kill him...\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip())>= 2 or guess <= "9":
        print("I asked for an alphabet not some random number or character...what's wrong with you?\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("Go for another letter,this ain't it.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("  |====== \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong, you still have " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("  |====== \n"
                  "  ||    || \n"
                  "  ||    || \n"
                  "  ||      \n"
                  "  ||     \n"
                  "  ||      \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong, you still have " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("  |======= \n"
                 "  ||     || \n"
                 "  ||     ||\n"
                 "  ||     ||\n"
                 "  ||      \n"
                 "  ||      \n"
                 "  ||      \n"
                 "__||__\n")
           print("Wrong, you still have " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("  |======= \n"
                  "  ||     || \n"
                  "  ||     ||\n"
                  "  ||     || \n"
                  "  ||     o \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong, this is your " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("  |======= \n"
                  "  ||     || \n"
                  "  ||     ||\n"
                  "  ||     || \n"
                  "  ||      O Ayayo Konnutaneyyyy:((""\n"
                  "  ||     /|\ \n"
                  "  ||     / \ \n"
                  "__||__\n")
            print("Duh...Hes's gone""\n")
            print("The correct word is:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Welldone champ, you saved him")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()