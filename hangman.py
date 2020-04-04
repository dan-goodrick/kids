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
    gallows.append('                ---------------')
    gallows.append('                |               |')
    return gallows

def display_gallows(gallows, guessed_letters, missing_letters):
    gallows[-2] = f"               --------------"
    gallows[-1] = f"               | {guessed_letters:<10} |"
    for row in gallows:
        print(row)
    print(f"{len(missing_letters)} {missing_letters}")
    #[print(row) for row in gallows]

def update_gallows(mistake_count, gallows):
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
        gallows[6] += '   ^'
    if mistake_count == 11:
        gallows[2] = '                   |    v x v'
        gallows.insert(1, gallows[1])
        gallows.insert(1, gallows[1])
        gallows.pop(9)
        gallows.pop(9)
    #make the guy fall if mistake_count == -1
    return gallows

def update_board(missing_letters, word, guess):
    missing_letters_list = list(missing_letters)
    indices = [i for i,l in enumerate(word) if l == guess]
    for i in indices:
        missing_letters_list[i] = guess
    missing_letters = ''.join(missing_letters_list)

    return missing_letters

def main():
    clear()
    gallows = build_gallows()
    guessed_letters = ''
    word = get_word()
    missing_letters = "*" * len(word)
    display_gallows(gallows, guessed_letters, missing_letters)
    i = 0
    # for i in range(11):
    while '*' in missing_letters:
        guess = input("Enter the next guess: ").upper()
        if guess in missing_letters or guess in guessed_letters:
            print(f"You already guessed {guess}.  Try again.")
            continue
        clear()
        if guess in word:
            missing_letters = update_board(missing_letters, word, guess)
        else:
            guessed_letters+=guess
            i += 1
            gallows = update_gallows(i, gallows)
        display_gallows(gallows, guessed_letters, missing_letters)

        if i == 11:
            print(f'You lost!  The word was {word}')
            return
    print(f"Good Job!  You got it!")

if __name__ == "__main__":
    main()
