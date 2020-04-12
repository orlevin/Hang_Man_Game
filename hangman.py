from hang_man import hangman_photos as photos
import os

MAX_TRIES = 7

HANGMAN_PHOTOS = [photos.PHOTO0, photos.PHOTO1, photos.PHOTO2, photos.PHOTO3, photos.PHOTO4, photos.PHOTO5, photos.PHOTO6]


def print_welcome_screen():
    print(photos.HANGMAN_ASCII_ART, "\n", MAX_TRIES , "\n")


#ensure that user insert exist file
def set_valid_file_path():
    while True:
        file_path = input("Enter file path:")
        if os.path.isfile(file_path):
            return  file_path
        print("file path not exist\n")


#ensure that user insert integer number
def set_valid_word_index():
    while True:
        index = input("Enter index:")
        if  index.isdigit():
            return  int(index)
        print("not valid index, please enter an integer number \n")


#print the hangman ART
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


#check if letter is one english letter, that not selected yet
def check_valid_input(letter_guessed, old_letters_guessed):
    is_one_char = len(letter_guessed) == 1
    is_alpha_char =  letter_guessed.isalpha()
    return is_one_char and is_alpha_char  and letter_guessed not in old_letters_guessed


#ensure that user insert one new english letter
def valid_letter_guessed(letter_guessed, old_letters_guessed):
    while not check_valid_input(letter_guessed,old_letters_guessed):
        print("not a valid input, choose one letter from a - z that you didnt guess already")
        letter_guessed = input("Guess a letter:").lower()
    old_letters_guessed += [letter_guessed.lower()]
    return letter_guessed


#check if the letter_guessed is contain in the secret_word
def is_letter_from_secret_word(letter_guessed, secret_word):
    if letter_guessed in secret_word:
        return True
    return False


#print massage when user guess wrong letter
def print_wrong_guess_massage(old_letters_guessed):
        print(':(')
        old_letters_guessed.sort()
        print(' -> '.join(old_letters_guessed))


#choose secret word from file, that the player will need to guess
def choose_word(file_path, index):
    file = open(file_path, 'r')
    words = file.read().split(" ")
    file.close()
    index = (index-1) % len(words)
    return  words[index]


#print the player progress with the hidden word
def show_hidden_word(secret_word, old_letters_guessed):
    reveal_word = ""
    for char in secret_word:
        if char in old_letters_guessed:
            reveal_word += char + " "
        else:
            reveal_word+="_ "
    print(reveal_word)


#check if all the letters were revealed
def check_win(secret_word, old_letters_guessed):
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


def main():
    print_welcome_screen()

    #get secret word
    file_path = set_valid_file_path()
    word_index = set_valid_word_index()
    secret_word = choose_word(file_path, word_index)

    print("Lets start!")

    #start parameters
    letters_guessed = []
    tries = 0

    while tries < MAX_TRIES:

        #print game state
        print_hangman(tries)
        show_hidden_word(secret_word,letters_guessed)

        #input letter from user
        guess = input("Guess a letter:").lower()
        valid_letter = valid_letter_guessed(guess,letters_guessed)

        #update state
        if is_letter_from_secret_word(valid_letter,secret_word):
            if check_win(secret_word, letters_guessed):
                show_hidden_word(secret_word, letters_guessed)
                print("\n  WIN ! ! ! \n")
                return
        else:
            print_wrong_guess_massage(letters_guessed)
            tries += 1
    show_hidden_word(secret_word, letters_guessed)
    print("\n LOSE . . . \n")




#if _name_ == "_main_":
main()