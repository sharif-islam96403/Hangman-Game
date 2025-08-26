import random
from word_file import words_diary
import string
print(f'\nWelcome to the game of Hangman. Here you get 10 lives and you have to guess the secret word before you are HANGED!!!')
def get_valid_word(words):
    word = random.choice(words_diary)
    while '-' in word or ' ' in word:
        word = random.choice(words_diary)

    return word.upper()

def hangman():
    word = get_valid_word(words_diary)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 15

    while len(word_letter) > 0 and lives > 0:
        print(f'You have {lives} lives left and you have used this letter: ', ' '.join(used_letter))
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print(f'\nCurrent word: ', ' '.join(word_list))

        user_input = input(f'Enter a guess letter: ').upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                lives = lives - 1
                print(f'Letter not in the secret word.\n')
        elif user_input in used_letter:
            print(f'You have used this letter before. Try again!\n')
        else:
            print(f'Invalid character. Try again!\n')
    if lives == 0:
        print(f'You failed to guess the secret word. The secret word is {word}')
    if len(word_letter) == 0:
        print(f'\nCONGRATULATIONS!! You have succesfully guesse the secret word {word}.')
hangman()




