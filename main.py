import random
import hangman_words
import hangman_art

#  TODO-1: randomly chose a word from word_list and assign it to variable called chosen_word
#  TODO-2: Ask the user to guess the letter and assign it to variable called guess and make it lowercase
#  TODO-3: Check if the letter user guessed(guess) is one of the letters in chosen_word
#  TODO-4: create a empty list blank_list for each letter in chosen word, add "_" each time to blank_list
#  TODO=5: loop through each position in chosen word if letter at that position matches the guess reveal that
#         letter at that position of blank_list
# TODO-6: Use while loop to let the user to guess again. The loop should only run if blanks are left and
#         and the user has not guessed all the letter in the word
# TODO-7: Create variable called lives to keep track of number of lives left
# TODO-8: If guess is not a letter in chosen word, then reduce live by 1 and once lives goes to zero
#         it should print you lose
# TODO-9: Join all the elements inlist and turn it into a string
# TODO-9: Print the ascii art from stages that corresponds to number of lives the user has remaining
# TODO-9: If the user has entered the letter they have already entered print letter and let them know
#         without losing their lives
# TODO-10: if letter is not in chosen word print out letter and let them know it's not in chosen word
stages = hangman_art.stages_of_lives
chosen_word = (random.choice(hangman_words.words_list)).lower()
blanks_left = True
blanks_list = []
entered_letters = []
lives = 7
print(hangman_art.logo)
for index in range(0, len(chosen_word)):
    blanks_list.append("_")
while blanks_left:
    word = ""
    guess_letter = (input("Guess a letter: ")).lower()
    for index in range(0, len(chosen_word)):
        if chosen_word[index] == guess_letter:
            blanks_list[index] = guess_letter
    for letter in blanks_list:
        word += (letter + " ")
    if guess_letter in entered_letters:
        print(word)
        print(f"you have already guessed: {guess_letter}")
        if lives <= 6:
            print(stages[lives])
            print("----------------------------------")
    elif guess_letter not in chosen_word:
        print(f"you guessed {guess_letter}, that's not in the word. You lose a life")
        print(word)
        print(stages[lives - 1])
        print("--------------------------------------")
        lives -= 1
    else:
        print(word)
    entered_letters.append(guess_letter)
    if lives == 0:
        blanks_left = False
        print(f"you lose\ncorrect word: {chosen_word}")
    # print(blanks_list)
    if "_" not in blanks_list:
        blanks_left = False
        print("you have won")
