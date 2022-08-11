from tkinter import E


#a program that plays the game hangman
import random

word = ['animal', 'fruits', 'humans', 'alians', 'vegetables']

chosen_word = random.choice(word)

display = []
lives = 6
for _ in range(len(chosen_word)):
    display += '_'
    
    # display = print('_', end='')   
    # 


end_of_game = False


while end_of_game == False:
    guess = input('\n Guess a letter: ').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
        #     print('Right')
        # else:
        #     print('Wrong')
    if '_' not in display:
        end_of_game = True
        print("You win")

