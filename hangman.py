import random
import os
from words import word_list
import time

def get_word():
    word = random.choice(word_list)
    return word.upper()

def clear():
    os.system('clear')

def build_gallows():
    gallows = []
    gallows.append('                   --------')
    gallows.append('                   |      |')# |
    gallows.append('                   |     ') #v'O'v
    gallows.append('                   |     ') # \|/
    gallows.append('                   |     ')#   |
    gallows.append('                   |     ') # / \
    gallows.append('                   |    ')#  ^   ^
    gallows.append('                   |')
    gallows.append('                   |')
    gallows.append('                -----------------')
    gallows.append('                |               |')
    return gallows

def display_gallows(gallows):
    for row in gallows:
        print(row)
    #[print(row) for row in gallows]

def update_gallows(mistake_count, guessed_letters, gallows):
    if mistake_count == 1:
        gallows[2]+=' O' # head
    if mistake_count == 2:#2:
        gallows[3]+=' |' # body
        gallows[4]+=' |'
    if mistake_count == 3: #3:
        gallows[3] +='/' #arm
    if mistake_count == 4:
        gallows[3] = '                   |     \\|/'
    if mistake_count == 5:
        gallows[5] += '/'
    if mistake_count == 6:
        gallows[5] += ' \\'
    if mistake_count == 7:
        gallows[2] += ' v'
    if mistake_count == 8:
        gallows[2] = '                   |    v O v'
    if mistake_count == 9:
        gallows[6] += '^'
    if mistake_count == 10:
        gallows[6] += '  ^'
    gallows[-2] = f"               ------" + '-'*len(guessed_letters)
    gallows[-1] = f"               | {guessed_letters} |"
    #make the guy fall if mistake_count == -1
    return gallows

gallows = build_gallows()
guessed_letters = ''
word = get_word()
missing_letters = "_" * len(word)
for i in range(11):
    clear()
    gallows = update_gallows(i, guessed_letters, gallows)
    display_gallows(gallows)
    print(missing_letters)
    guess = input("Enter the next guess: ")
    guessed_letters+=guess

    # if mistake_count == -1:
    #     gallows[2] = '                   |    v x v'
    #     gallows.insert(1, gallows[1])
    #     gallows.insert(1, gallows[1])
    #     gallows.pop(9)
    #     gallows.pop(9)


# def update_board(missing_letters, word, guess):
#     missing_letters_list = list(missing_letters)
#     indices = [i for i, letter in enumerate(word) if letter == guess]
#     for j in indices:
#         missing_letters_list[j] = guess
#     return missing_letters
#

#
# def main(game_over=False):
#     gallows = build_gallows()
#     word = get_word()
#     missing_letters = "_" * len(word)
#     guessed_letters = []
#     tries = int(input('How many attempts? '))
#     for i in range(tries):
#         clear()
#         guess = input("Enter a guess")
#         guessed_letters.append(guess)
#         guessed_letters = list(set(guessed_letters)).sort()
#         missing_letters = update_board(missing_letters, word, guess)
#         gallows = update_gallows(i, guessed_letters, gallows)
#         display_gallows(gallows)
#         print(missing_letters)
#         time.sleep(1)
#
#     game_over=True
#     if game_over:
#         clear()
#         gallows = update_gallows(-1, guessed_letters, gallows)
#         display_gallows(gallows)

# if __name__ == "__main__":
#     main()

# def play(word):
#     missing_letters = "_" * len(word)
#     game_over = False
#     guessed_letters = []
#     guessed_words = []
#     tries = 6
#     gallows = build_gallows()
#     print("Let's play Hangman!")
#     print(display_hangman(tries))
#     print(missing_letters)
#     print("\n")
#     while not game_over and tries > 0:
#         guess = input("Please guess a letter or word: ").upper()
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("You already guessed the letter", guess)
#             elif guess not in word:
#                 print(guess, "is not in the word.")
#                 tries -= 1
#                 guessed_letters.append(guess)
#             else:
#                 print("Good job,", guess, "is in the word!")
#                 guessed_letters.append(guess)
#                 word_as_list = list(missing_letters)
#                 indices = [i for i, letter in enumerate(word) if letter == guess]
#                 for index in indices:
#                     word_as_list[index] = guess
#                 missing_letters = "".join(word_as_list)
#                 if "_" not in missing_letters:
#                     game_over = True
#         elif len(guess) == len(word) and guess.isalpha():
#             if guess in guessed_words:
#                 print("You already guessed the word", guess)
#             elif guess != word:
#                 print(guess, "is not the word.")
#                 tries -= 1
#                 guessed_words.append(guess)
#             else:
#                 game_over = True
#                 missing_letters = word
#         else:
#             print("Not a valid guess.")
#         clear()
#         print(display_hangman(tries))
#         print(missing_letters)
#         print("\n")
#     if game_over:
#         print("Congrats, you guessed the word! You win!")
#     else:
#         print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")
