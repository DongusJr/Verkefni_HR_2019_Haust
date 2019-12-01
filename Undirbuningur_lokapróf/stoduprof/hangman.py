import random

# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'

def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def get_user_input(letters_used, guess_count):
    user_letter = input("Choose a letter: ")
    if user_letter not in letters_used:
        letters_used.append(user_letter)
        return user_letter
    else:
        print("You have already guessed that letter!")
        return None

def progress_game(user_letter, game_word, secret_word, guess_count):
    if user_letter in game_word:
        print("You guessed correctly!")
        guess_count += 1
        for i in range(len(game_word)):
            if game_word[i] == user_letter:
                secret_word = secret_word[:i] + user_letter + secret_word[i+1:]
    else:
        print("The letter is not in the word")
        guess_count += 1
    return secret_word, guess_count

def print_word_to_guess(secret_word):
    print_str = "Word to guess"
    for letter in secret_word:
        print_str += " " + letter
    print(print_str)

# Main program starts here
random_seed()

def main():
    game_word = random.choice(WORD_LIST)
    secret_word = CHAR_PLACEHOLDER*len(game_word)
    print("The word you need to guess has {} characters".format(len(game_word)))
    running = True
    letters_used = []
    guess_count = 0
    while running:
        print_word_to_guess(secret_word)
        user_letter = get_user_input(letters_used, guess_count)
        if user_letter:
            secret_word, guess_count = progress_game(user_letter, game_word, secret_word, guess_count)

        if CHAR_PLACEHOLDER not in secret_word:
            print("You won!")
            running = False
            print("Word to guess:{}".format(secret_word))

        if running:
            print("You are on guess {}/12".format(str(guess_count)))

        if guess_count == 12:
            print("You lost! the secret word was {}".format(game_word))
            running = False


main()