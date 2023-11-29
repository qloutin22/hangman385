# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:46:08 2023

@author: quannal
"""

import random 
word_list = ["Mango" ,"Apple","Pomgrante","Orange"," Banana"]
list_of_guesses = []

class Hangman :
    def __init__ (self,word_list,num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = set(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
        
    @classmethod
    def add_letter(guess, list_of_guesses):
        for guess in list_of_guesses:
            list_of_guesses.apprend(guess)
        return print(set((list_of_guesses.append(guess))))
    
    @staticmethod
    def check_guess(guess):
        guess = guess.lower()
        if len(guess) and guess.isalpha() == True: 
            if any(guess.lower() in word.lower() for word in word_list):
                print("Good guess!", guess , "is in the word.")
            else:
                print("Sorry," ,guess," is not in the word. Try again.")
        return list_of_guesses.append(guess)
    print(list_of_guesses)
    
    @staticmethod
    def ask_for_input():
        guess = str(input("Please input a letter?"))
        while True: 
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
                break
            elif guess in list_of_guesses:
                print("You already tried that letter!") 
                break
            else:
                Hangman.check_guess(guess)
        return list_of_guesses.append(guess)
        print(list_of_guesses.append(guess))
hangman = Hangman(word_list)
hangman.ask_for_input()