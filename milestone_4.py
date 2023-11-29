import random 
word_list = ["Mango" ,"Apple","Pomgrante","Orange"," Banana"]


class Hangman :
    def __init__ (self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list()
        
def check_guess(guess):
    while True: 
        if len(guess) == 1 and guess.isalpha() == True:
            if any(guess.lower() in word.lower() for word in word_list):
                print("Good guess!", guess , "is in the word.")
                break
            else:
                print(f"Sorry, " ,guess ," is not in the word. Try again.")
                break

def ask_for_input():
    guess = input("Please input a letter?")
    list_of_guesses = []
    for guess in list_of_guesses:
        while True: 
            if len(guess) != 1 or  guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.") 
                break
            elif guess in list_of_guesses() :
                print("You already tried that letter!")  
                break
            else:
                check_guess(guess)
            
                break
    list_of_guesses = list_of_guesses + guess
    print(list_of_guesses)


    ask_for_input()