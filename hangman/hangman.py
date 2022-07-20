import random
from english_words import english_words_lower_alpha_set
from PyDictionary import PyDictionary

def game_play(challenging=False):

    if challenging is False:
        chosen = random.choice(list(english_words_lower_alpha_set))
    else:
        print("This is the CHALLENGING MODE!")
        print("You have only 5 chances rather den 10")
        print("And you can't use any command")
        print("You won't even be notify if you had only 3 chances left")
        print("Good luck")
        print()
        chosen = random.choice([x for x in english_words_lower_alpha_set if len(x) > 8])

    shown = len(chosen) * "_"
    time_remaining = 10 if challenging is False else 5
    guesses = set()
    time_use = 0
    hints = ["Show definition", "Uncover some letter"]

    while True:
        if time_remaining == 0:
            print(shown)
            print("Time out sorry! The answer is {}".format(chosen))
            return

        print(shown)
        if challenging is False:
            print(f"OH NO YOU HAVE ONLY {time_remaining} CHANCES LEFT\n" if time_remaining <= 3 else "", end="")
        guess = input("Enter your guess: ").lower()

        if guess.startswith("!"):
            if challenging is False:
                guess = guess.replace("!", "")
                if guess == "gup":
                    sure = input("Are you sure u want to give up [y/n] >> ")

                    if sure.lower() == "y":
                        print("The answer is {}".format(chosen))
                        print("Damn Game Over")
                        return
                    else:
                        print("Game continue\n")
                        continue
                elif guess == "tried":
                    listy = list(guesses)
                    listy.sort()
                    print(" ".join(listy))

                    continue
                elif guess == "help":
                    print("""This is a hangman game!!!!!
Everytime you start you get a chance of 10,
if you guess 10 letter and got none correct den sorry u lose
but if you guess like 1 letter after 9 failure den your chance get update and you get 10 CHANCES AGAIN

there are some awesome COMMANDS that you can use to help u

Command manual
gup - short for give up (You get it)
tried - will return all the letter you tried
help - will show you how to play the game
left - will show how many times you left
hints - still in process
""")
                    continue
                elif guess == "left":
                    print(time_remaining)
                    print()
                    continue
                elif guess == "hint":

                    if hints == []:
                        print("No hints left\n")

                    for index, x in enumerate(hints):
                        print(f"{index + 1}. {x}")

                    choose = input("Enter the hints: ")

                    if choose.isalpha():
                        print("Only number can be use")

                    elif int(choose) > len(hints) or int(choose) < 1:
                        print("Unknown hints")

                    else:

                        chosen_hint = hints.pop(hints.index(hints[int(choose) - 1]))

                        if chosen_hint.startswith("Show "):
                            dictionary = PyDictionary(chosen)

                            print(dictionary.getMeanings().get(chosen))
                        elif chosen_hint.startswith("Uncover"):

                            unknown = []

                            for index, x in enumerate(shown):
                                if x == "_":
                                    unknown.append(index)

                            chosen_to_reveal = chosen[random.choice(unknown)]
                            guesses.add(chosen_to_reveal)

                            shown = ""
                            for x in chosen:

                                if x in guesses:
                                    shown += x
                                    continue
                                shown += "_"

                    print()
                    continue
            else:
                print("No command can be use CHALLENGING")
                continue

        if guess.isnumeric():
            print("Pls a ENGLISH letter\n")
            continue
        elif len(guess) != 1:
            print("Pls ONLY 1 LETTER\n")
            continue
        print()

        time_use += 1
        if guess in chosen and guess not in guesses:

            time_remaining = 10 if challenging is False else 5
            guesses.add(guess)

            shown = ""
            for x in chosen:

                if x in guesses:
                    shown += x
                    continue
                shown += "_"

            if shown == chosen:
                print(shown)
                print("YOU GUESS IT by using {} guesses".format(time_use))
                return
        else:
            guesses.add(guess)
            time_remaining -= 1

if "__main__" == __name__:
    game_play()
