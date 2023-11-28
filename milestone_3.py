import random

word_list = ["Mango" ,"Apple","Pomgrante","Orange"," Banana"]

word =random.choice(word_list)

guess = input("Please input a letter?")

while True: 
    guess = input("Please input a letter?")
    
    if len(guess) == 1 and guess.isalpha() == True:
        if any(guess.lower() in word.lower() for word in word_list):
            print("Good guess!", guess , "is in the word.")
        else:
            print(f"Sorry, " ,guess ," is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")