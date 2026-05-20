
# 📘 Assignment: Games in Python

## 🎯 Objective

Build a playable word-guessing game in Python while practicing strings, loops, conditionals, and user input. By the end, you will create a complete Hangman-style game with clear win/lose outcomes.

## 📝 Tasks

### 🛠️	Build the Core Game Loop

#### Description
Create the main game flow for Hangman. Your program should choose a secret word, repeatedly ask the player for letter guesses, and update the display after each guess.

#### Requirements
Completed program should:

- Randomly select a word from a predefined Python list.
- Display the word as hidden characters (for example, `_ _ _ _`) and reveal correct letters in their positions.
- Prompt the player to enter one letter at a time until the game ends.


### 🛠️	Add Win/Loss Rules and Feedback

#### Description
Finish the game by tracking incorrect guesses, preventing invalid gameplay actions, and displaying clear end-of-game messages.

#### Requirements
Completed program should:

- Decrease remaining attempts only for incorrect guesses.
- Handle invalid input (empty input, multiple characters, non-letters) with a helpful message.
- End with a win message when the full word is guessed, or a loss message when attempts reach zero.
