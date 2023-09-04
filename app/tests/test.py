import unittest
from unittest.mock import patch
from app.hangman.hangman import HangmanGame

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        with patch('app.hangman.hangman.get_random_word') as mock_get_random_word:
            mock_get_random_word.return_value = "labas"
            self.hangman_game = HangmanGame()
        
               
    def test_correct_guess(self):
        result = self.hangman_game.make_guess("labas")
        self.assertEqual(result, "Congratulations! You've guessed the word!")
    
    def test_already_guessed(self):
        self.hangman_game.make_guess("a")  
        result = self.hangman_game.make_guess("a")
        self.assertEqual(result, "You've already guessed that letter.")
    
    def test_incorrect_guess(self):
        result = self.hangman_game.make_guess("x")
        self.assertEqual(result, "Incorrect guess! Try again.")
        
    
    def test_incorrect_guess_updates_hangman_state(self):
        self.hangman_game.make_guess("x")
        self.assertEqual(self.hangman_game.current_hangman_state, 1)
    

    
if __name__ == '__main__':
    unittest.main()