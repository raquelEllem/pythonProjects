import random
from turtle import clear

import hangman_lists as hg

word_choice = random.choice(hg.word_list)
print(hg.logo)

display = []
for _ in range(len(word_choice)):
    display += "_"
print(f"{' '.join(display)}")

win = False
lives = 6
while lives >= 0 and win is not True:
    guess = input("Guess a letter: ".lower())
    for i, letter in enumerate(word_choice):
        if guess == letter:
            display[i] = letter
    print(f"{' '.join(display)}")
    if guess not in word_choice:
        print(hg.stages[lives])
        lives -= 1
        if lives < 0:
            print("You lose.")
    if '_' not in display:
        print("You win!")
        win = True
print(word_choice)
