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

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/Hangman-Flask.git
    cd Hangman-Flask
    ```

2. **Create a Virtual Environment and Install Dependencies:**

    ```bash
    python3 -m venv venv
    ```

    Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

    Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask Development Server:**

    ```bash
    flask run
    ```

   This will start the development server, and you can access the Hangman game by opening your web browser and navigating to `http://localhost:5000`.

## Usage
Register a new player account or log in if you already have an account.
Start a new game and guess the secret word letter by letter.
Receive feedback on your guesses and continue playing until you win or lose.
View your game results and track your performance in the game.

## Screenshots

**Home page**
![Home page](https://github.com/AndriusSab/Hangman_Flask/assets/124807066/37672ff3-0540-4016-9779-ac407b65c060)





