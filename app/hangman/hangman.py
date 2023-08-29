from typing import List
from .get_random_word import get_random_word




class HangmanGame:
    def __init__(self):
        self.secret_word: str = get_random_word()
        self.guesses: List[str] = []
        self.max_attempts: int = 2
        self.current_hangman_state: int = 0
        self.incorrect_guesses = 0


    def display_word(self) -> str:
        displayed_word = ""   # Initialize an empty string to store the displayed word
        for letter in self.secret_word: #iteruojama  per kiekviena raide slaptame zodyje
            if letter in self.guesses: # jei spejama raide yra zodyje, parodoma raide
                displayed_word += letter
            else:
                displayed_word += " _ " #pirmiausia ivyksta sita logika
        return displayed_word

    def make_guess(self, guess: str) -> str:
        guess = guess.lower() # Convert the guess to lowercase to handle case-insensitivity
        
        # pasitikirnam ar spejamas zodis yra "uzsleptas zodis"
        if guess == self.secret_word:
            self.guesses.append(guess) # Add the guess to the list of guesses
            return "Congratulations! You've guessed the word!"
        
       # pasitikirnam ar spejama raide jau buvo speta ar ne"
        if guess in self.guesses:
            return "You've already guessed that letter."
        self.guesses.append(guess)  #Add the guess to the list of guesses
        
        # Check if the guess is incorrect
        if guess != self.secret_word and guess not in self.secret_word:
            self.max_attempts -= 1 # Decrease the remaining attempts
            self.current_hangman_state += 1 # Increase the hangman state
        
        return "Incorrect guess! Try again."
            
            
        
        
    def has_won(self) -> bool:
        if self.secret_word in self.guesses: 
            return True  # pasitikirnam ar spejamas zodis yra "uzsleptas zodis"
        for letter in self.secret_word:
            if letter not in self.guesses: # If any letter is not yet guessed
                return False  # The player has not won yet
        return True

    def is_game_over(self) -> bool:
        if self.max_attempts <= 0 or self.current_hangman_state >= 10:
            return True # If maximum attempts are exhausted or hangman state is complete, the game is over
        if " _ " not in self.display_word():
            return True # If there are no more blanks in the displayed word, the game is over
        return False # If neither of the above conditions are met, the game is not over



    def to_dict(self) -> dict:
        return {
            "secret_word": self.secret_word,
            "guesses": self.guesses,
            "max_attempts": self.max_attempts,
            "current_hangman_state": self.current_hangman_state,
            "incorrect_guesses": self.incorrect_guesses
        }

    @classmethod
    def from_dict(cls, data: dict):
        game = cls()
        game.secret_word = data["secret_word"]
        game.guesses = data["guesses"]
        game.max_attempts = data["max_attempts"]
        game.current_hangman_state = data["current_hangman_state"]
        game.incorrect_guesses = data["incorrect_guesses"]
        return game



