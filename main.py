import random
import re

list_of_words = ("apple", "tree", "horse", "banana", "orange", "monkey", "helicopter")
random_word = random.choice(list_of_words)
answer = " "    # store user's answer in this string.


def check_user_input(input_from_user: str) -> None:
    global answer, attempt_counter

    # checking whether an input is a letter and in our random word.
    if len(input_from_user) == 1 and input_from_user in random_word:
        answer += input_from_user   # adding correct letter to the answer
        print(f"You guessed a letter: {input_from_user}")
    elif len(input_from_user) == 1 and input_from_user not in random_word:
        print("Wrong letter!")
        attempt_counter -= 1    # reducing counter in case of a wrong letter.

    # checking whether an input is a word and is equal our random word.
    elif len(input_from_user) > 1 and input_from_user == random_word:
        print("You guessed a word! Congrats!")
        exit()
    elif len(input_from_user) == 1 and input_from_user != random_word:
        print("Wrong guess!")
        attempt_counter -= 1    # reducing counter in case of a wrong letter.


def check_word() -> None:
    # use this pattern for printing guessed letters in word covered with asterisks.
    pattern = "[^" + answer + "]"
    # replace matching characters with asterisks.
    masked_word = re.sub(pattern, "*", random_word)
    print(masked_word)

    # checking whether user guessed the word by typing letters
    if set(answer) == set(" " + random_word):
        print("You guessed a word! Congrats!")
        exit()


def start_the_game() -> None:
    while attempt_counter:
        input_from_user = input("\nEnter a letter or a word here: ")
        check_user_input(input_from_user)
        check_word()
    else:
        print("Your attempts are finished.")


if __name__ == "__main__":
    attempt_counter = int(input("How many attempts do you need? "))
    start_the_game()
