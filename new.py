import random

word_list = ["Mango", "Apple", "Pomegranate", "Orange", "Banana"]
list_of_guesses = []


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    @classmethod
    def add_letter(cls, guess):
        cls.list_of_guesses.append(guess)

    @staticmethod
    def check_guess(guess):
        guess = guess.lower()
        if len(guess) == 1 and guess.isalpha():
            if any(guess.lower() in word.lower() for word in word_list):
                print("Good guess!", guess, "is in the word.")
            else:
                print("Sorry,", guess, "is not in the word. Try again.")
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

    @staticmethod
    def ask_for_input():
        while True:
            guess = input("Please input a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in list_of_guesses:
                print("You already tried that letter!")
            else:
                Hangman.check_guess(guess)
                Hangman.add_letter(guess)  # Appending the guess here to list_of_guesses
                break

        return list_of_guesses

hangman = Hangman(word_list)
hangman.ask_for_input()
