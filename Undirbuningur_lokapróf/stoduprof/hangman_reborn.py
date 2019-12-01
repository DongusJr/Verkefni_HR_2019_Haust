import random

# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    ''' Function that returns the psuedo-random seed given by user '''
    seed = int(input("Random seed: "))
    random.seed(seed)

def print_word_to_guess(word):
    ''' Function that prints out the hidden word and reveals letters already guessed '''
    print("Word to guess:", end="")
    for letter in word:
        print(" " + letter, end="")
    print()

def check_letter(letter, chosen_words, real_word):
    ''' Function that checks wheter the word has been already chosen, is correct or incorrect
        returns booleans indicating wheter it should add to the guess counter and replace the word '''
    if letter in chosen_words:  # If the letter has been already selceted
        print("You have already guessed that letter!")
        return False, False
    elif letter in real_word:  # If the letter is correct
        print("You guessed correctly!")
        return True, True
    else:                      # If the letter is incorrect
        print("The letter is not in the word!")
        return True, False

def replace_secret_word(secret_word, real_word, user_letter):
    ''' Function that reveals hidden letters in the secret word if the user guess correctely '''
    for index, letter in enumerate(real_word):
        if user_letter == letter:   # If the index matches the letter guessed by user
            secret_word[index] = user_letter  # Reveal it
    return secret_word

# Main program starts here
random_seed()

def main():
    ''' Main function of this program '''
    guess_counter = 0
    chosen_words = set()  # Make it a set to single the unique letters
    running = True        # While loop control variable
    real_word = random.choice(WORD_LIST)  # The word the user needs to guess
    secret_word = [CHAR_PLACEHOLDER]*len(real_word)  # The secret word "- - - ... - -"
    print("The word you need to guess has {} characters".format(len(real_word)))
    print_word_to_guess(secret_word)
    while(running):   # The main loop
        user_letter = input("Choose a letter: ")
        valid_letter, replace_letter = check_letter(user_letter, chosen_words, real_word)
        chosen_words.add(user_letter)  # Add the unique letter to the chosen
        if valid_letter:  # If it was correct or incorrect
            guess_counter += 1
            if replace_letter:  # if it was correct
                secret_word = replace_secret_word(secret_word, real_word, user_letter)
        if CHAR_PLACEHOLDER not in secret_word:  # If there are no more hidden letters, you win
            print("You won!")
            running = False  # Stop the game
        if running:  # Only when game is running
            print("You are on guess {}/{}".format(str(guess_counter), str(MAX_GUESS)))  # display guesses made
        print_word_to_guess(secret_word)  # Display letters user has unveiled
        if guess_counter == MAX_GUESS and running:  # if user has used all his guesses and the user has not won yet 
            print("You lost! the secret word was {}".format(real_word))
            running = False  # Stop the game

main()