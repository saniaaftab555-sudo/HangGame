import random

# Predefined word list
words = ["python", "apple", "chair", "table", "house"]

# Choose a random word
word = random.choice(words)
word_letters = list(word)

# To track guessed letters
guessed_letters = []

# To display progress
display = ["_"] * len(word)

# Number of wrong guesses allowed
max_attempts = 6
attempts = 0

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while attempts < max_attempts and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_attempts - attempts)
    
    guess = input("Enter a letter: ").lower()
    
    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in word_letters:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        attempts += 1

# Result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
