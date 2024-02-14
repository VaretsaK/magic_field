import random

list_of_words = ("apple", "tree", "horse", "banana", "orange", "monkey", "helicopter")


# def magic_field_game(num_attempts: int):
attempt_counter = 3

# getting one random word from the list of words
random_word = random.choice(list_of_words)
answer = set()

while attempt_counter:
    input_from_user = input("\nEnter a letter of a word here: ")

    if len(input_from_user) == 1 and input_from_user in random_word:
        answer.add(input_from_user)
        print(f"You have a letter: {input_from_user}")
    elif len(input_from_user) == 1 and input_from_user not in random_word:
        print("Wrong letter!")
        attempt_counter -= 1
    elif len(input_from_user) > 1 and input_from_user == random_word:
        print("You have guessed a word! Congrats!")
        print(random_word)
    elif len(input_from_user) == 1 and input_from_user != random_word:
        print("Wrong guess!")
        attempt_counter -= 1
        break

    for letter in random_word:
        if letter in answer:
            print(letter, end="")
        else:
            print("*", end="")

# if __name__ == "__main__":
#     magic_field_game(3)