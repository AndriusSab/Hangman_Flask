from typing import List
from .get_random_word import get_random_word


"""
HangmanGame class.
This class encapsulates the logic and state of a Hangman game, including the secret word,
guessed letters, remaining attempts, hangman drawing state, and game outcome.
"""


class HangmanGame:
    
    def __init__(self):
        self.secret_word: str = get_random_word()
        self.guesses: List[str] = []
        self.max_attempts: int = 100
        self.current_hangman_state: int = 0
        self.incorrect_guesses = 0
        

    def display_word(self) -> str:
        displayed_word = ""   
        for letter in self.secret_word: 
            if letter in self.guesses:
                displayed_word += letter
            else:
                displayed_word += " _ " 
        return displayed_word

    def make_guess(self, guess: str) -> str:
        guess = guess.lower() 
        
       
        if guess == self.secret_word:
            self.guesses.append(guess)
            return "Congratulations! You've guessed the word!"
        
      
        if guess in self.guesses:
            return "You've already guessed that letter."
        self.guesses.append(guess)  
         
        if guess != self.secret_word and guess not in self.secret_word:
            self.max_attempts -= 1
            self.current_hangman_state += 1 
        return "Incorrect guess! Try again."                     
        
    def has_won(self) -> bool:
        if self.secret_word in self.guesses: 
            return True  
        for letter in self.secret_word:
            if letter not in self.guesses: 
                return False  
        return True

    def is_game_over(self) -> bool: # update func name to has_lost
        if self.max_attempts <= 0 or self.current_hangman_state >= 10:
            return True 
        if " _ " not in self.display_word():
            return True 
        return False 



    def to_dict(self) -> dict:
        """
Converts the current state of the Hangman game into a dictionary.
Returns:
    dict: A dictionary containing the game state.
        """
        
        return {
            "secret_word": self.secret_word,
            "guesses": self.guesses,
            "max_attempts": self.max_attempts,
            "current_hangman_state": self.current_hangman_state,
            "incorrect_guesses": self.incorrect_guesses
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
Creates a new Hangman game instance from a dictionary containing game state.
Args:
    data (dict): A dictionary containing game state.
Returns:
    HangmanGame: A new HangmanGame instance initialized with the provided state.
"""   
      
        game = cls()
        game.secret_word = data["secret_word"]
        game.guesses = data["guesses"]
        game.max_attempts = data["max_attempts"]
        game.current_hangman_state = data["current_hangman_state"]
        game.incorrect_guesses = data["incorrect_guesses"]
        return game



