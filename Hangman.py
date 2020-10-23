import random
print("Hangman Game!")
print("There are only five guesses allowed.")
secretList = ["control", "remote", "laptop", "cognition", "shelf", "book", "house", "computer", "travel", "mechanical",
              "tomorrow", "potato", "lovely", "awesome", "ability", "nature", "yam", "target", "music", "concentration",
              "picture", "food", "mind", "brave", "robot", "conflict", "school", "forever", "tea", "car", "library",
              "great", "paradox", "insomnia", "yogurt", "time", "illusion", "vendetta", "crown", "world", "electrical",
              "wallpaper", "clock", "monkey", "space", "movie", "order", "chaos", "knight", "mystery", "destination"]
# choose a random word
secretWord = random.choice(secretList)
guesses = ""
noOfGuesses = 5
while noOfGuesses > 0:
    wrongGuess = 0
    # check for letter guessed by user
    for letter in secretWord:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            wrongGuess += 1
    if wrongGuess == 0:
        print("\nCongratulations. You win.")
        break
    guess = input("\nGuess a letter: ")
    guesses += guess
    if guess not in secretWord:
        noOfGuesses -= 1
        print("Wrong letter guess.")
        print("You have", + noOfGuesses, "more guesses left.")
if noOfGuesses == 0:
    print("You Lose. ", secretWord, " is the word")
