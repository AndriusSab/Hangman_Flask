This Hangman game allows players to guess a secret word letter by letter. 
The game provides a user interface where players can interact with the game and make their guesses. 
After each guess, the game provides feedback on whether the guessed letter is in the secret word or not. 
Players continue guessing until they either solve the word or run out of attempts.

## Features

- User registration and login functionality
- Interactive gameplay for guessing letters
- Feedback on correct and incorrect guesses
- Display of game results (wins and losses) for registered players
- SQLite database for storing player information and game results


## Installation

Clone the repository:

   ```bash
   git clone https://github.com/your-username/Hangman-Flask.git
   cd Hangman-Flask
    
 Create a virtual environment and install the required dependencies:
  
   
   python3 -m venv venv
   source venv/bin/activate  
   pip install -r requirements.txt

Run the Flask development server:
 
 ```bash
   flask run

