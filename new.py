import random

word_list = ["Mango", "Apple", "Pomgrante", "Orange", "Banana"]
list_of_guesses = []


class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.list_of_guesses:
            print("You already tried that letter!")
            return False
        else:
            self.list_of_guesses.append(guess)
            if guess in self.word.lower():
                print("Good guess!", guess, "is in the word.")
                for i in range(len(self.word)):
                    if guess == self.word[i].lower():
                        self.word_guessed[i] = self.word[i]
                return True
            else:
                self.num_lives -= 1
                print("Sorry,", guess, "is not in the word. Try again.")
                return False

    def ask_for_input(self):
        while self.num_lives > 0 and '_' in self.word_guessed:
            print(" ".join(self.word_guessed))
            print(f"Lives left: {self.num_lives}")
            guess = input("Please input a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            else:
                self.check_guess(guess)

        if '_' not in self.word_guessed:
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(f"Sorry, you ran out of lives. The word was: {self.word}")


hangman = Hangman(word_list)
hangman.ask_for_input()
