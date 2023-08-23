
import random
from typing import List
from .words_list import get_random_words_list
from .hangman_states import hangman_states



class HangmanGame:
    def __init__(self):
        # self.words_list: List[str] = get_random_words_list()
        self.secret_word: str = get_random_words_list()
        self.guesses: List[str] = []
        self.max_attempts: int = 50
        self.hangman_states: List[str] = hangman_states
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

    def display_hangman(self) -> None:
        print(self.hangman_states[self.current_hangman_state])


    def make_guess(self, guess: str) -> str:
        guess = guess.lower()
        if guess == self.secret_word:
            self.guesses.append(guess)
            return "Congratulations! You've guessed the word!"
        elif guess in self.guesses:
            return "You've already guessed that letter."
        else:
            self.guesses.append(guess)
            if guess != self.secret_word:
                self.max_attempts -= 1
                self.current_hangman_state += 1
            return "Incorrect guess! Try again."
        
    def has_won(self) -> bool:
        for letter in self.secret_word:
            if letter not in self.guesses:
                return False
        return True

    def is_game_over(self) -> bool:
        if self.max_attempts <= 0 or self.current_hangman_state >= len(self.hangman_states):
            return True
        if " _ " not in self.display_word():
            return True
        return False



    def to_dict(self) -> dict:
        return {
            # "words_list": self.words_list,
            "secret_word": self.secret_word,
            "guesses": self.guesses,
            "max_attempts": self.max_attempts,
            "current_hangman_state": self.current_hangman_state,
            "incorrect_guesses": self.incorrect_guesses
        }

    @classmethod
    def from_dict(cls, data: dict):
        game = cls()
        # game.words_list = data["words_list"]
        game.secret_word = data["secret_word"]
        game.guesses = data["guesses"]
        game.max_attempts = data["max_attempts"]
        game.current_hangman_state = data["current_hangman_state"]
        game.incorrect_guesses = data["incorrect_guesses"]
        return game



