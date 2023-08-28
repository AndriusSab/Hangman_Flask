import unittest

from hangman.hangman import HangmanGame

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        
        self.hangman_game = HangmanGame("secretword") 
        
    def test_correct_guess(self):
        result = self.hangman_game.make_guess("secretword")
        self.assertEqual(result, "Congratulations! You've guessed the word!")
    
    def test_already_guessed(self):
        self.hangman_game.make_guess("a")  
        result = self.hangman_game.make_guess("a")
        self.assertEqual(result, "You've already guessed that letter.")
    
    def test_incorrect_guess(self):
        result = self.hangman_game.make_guess("x")
        self.assertEqual(result, "Incorrect guess! Try again.")
        self.assertEqual(self.hangman_game.max_attempts, 5)  
    
    def test_incorrect_guess_updates_hangman_state(self):
        self.hangman_game.make_guess("x")
        self.assertEqual(self.hangman_game.current_hangman_state, 1)
    
    def test_max_attempts_decrease(self):
        self.hangman_game.make_guess("x")
        self.assertEqual(self.hangman_game.max_attempts, 5)
    
if __name__ == '__main__':
    unittest.main()