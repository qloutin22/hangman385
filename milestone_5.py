import random 
word_list = ["Mango" ,"Apple","Pomgrante","Orange","Banana"]

class Hangman :
    def __init__ (self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    
    
    def check_guess(self, guess):
        guess = guess.lower()
        if len(guess) and guess.isalpha() == True: 
            if any(guess.lower() in word.lower() for word in word_list):
                print("Good guess!", guess , "is in the word.")
                for index, letter in enumerate(self.word):
                    if letter.lower() == guess:
                        self.word_guessed[index] = letter
                self.num_letters = self.num_letters-1
                print(self.word_guessed)
                if guess in self.word == self.word_guessed:
                    print ("You won!")
            else:
                print("Sorry," ,guess," is not in the word. Try again.")
                self.num_lives = self.num_lives -1
                print("You have", self.num_lives ,"lives left")
                if self.num_lives == 0:
                    print("You Lost!")
                

                

    
    
    def ask_for_input(self):
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
        

def play_game (word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    
    while True:
        if num_lives == 0 :
            print("You LOST!")
            print(num_lives)
            break
        if game.num_letters > 0:
            game.ask_for_input()
            print(num_lives)
        if num_lives and game.num_letters !=0 :
            print("Congradulations you have won!!!")
            print(num_lives)
            break


play_game(word_list)
