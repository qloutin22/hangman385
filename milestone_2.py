import random 
word_list = ["Mango" ,"Apple","Pomgrante","Orange"," Banana"]

word =random.choice(word_list)

print(word)

guess = input("Please input a letter?")
if len(guess) == 1 and guess.isalpha() == True :
    print("Good Guess")
else:
    print("Ooops Invalid input")