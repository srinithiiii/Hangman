import random

#------------------------------ Todo -1------------------------------------------

from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# -------------------------------TODO-3:------------------------------------------
from hangman_art import logo

print(logo)

# ----------------------------------testing----------------------------------------
#print(f'the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
 #---------------------------------------------------------- TODO-4:------------------------------------ -
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # ------------------------------------TODO-5---------------------------------------------
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'the solution is {chosen_word}.')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # -----------------------------------------TODO-2------------------------------------------
    from hangman_art import stages
    print(stages[lives])