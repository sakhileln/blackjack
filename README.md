# Blackjack Game in Python
This is a simple implementation of the Blackjack card game in Python. It allows you to play against a computer dealer, where the goal is to get a hand value as close to 21 as possible without going over. The game includes basic features such as drawing cards, deciding whether to "hit" or "stand", and handling a game over situation.

## Table of Contents
- [Game Rules](#game-rules)
- [Features](#features)
- [Requirements](#requirements)
- [How to Play](#how-to-play)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)

# Game Rules
- Card values:
    - Cards 2-10 are worth their face value.
    - Jacks, Queens, and Kings are worth 10 points.
    - Aces are worth 1 or 11 points, whichever is more beneficial to the player.
- The player wins if:
    - They have a higher total than the dealer without busting.
    - The dealer busts (goes over 21).
- The player loses if:
    - Their total exceeds 21 (busts).
    - The dealer has a higher total and does not bust.

# Features
- **Deck of cards**: A standard deck of 52 cards.
- **Player Actions**: The player can "hit" (take another card) or "stand" (keep their current hand).
- **Dealer Behavior**: The dealer will hit until their hand value is 17 or more.
- **Game Over Conditions**: The game ends when the player or dealer goes over 21 (busts), or when both have finished their turns and the winner is determined.

# Requirements
- Python 3.x
- No external libraries required (uses built-in Python modules).

# How to Play
1. Run the blackjack.py file.
2. The game will prompt you for actions:
    - Type **hit** to take another card.
    - Type **stand** to keep your current hand and end your turn.
3. The game will simulate the dealer’s turn, and then determine the winner based on who has the higher score without going over 21.
4. The game will tell you if you win, lose, or if it’s a tie.

# Usage
- Clone the repository or download the blackjack.py file.
- Open a terminal and navigate to the directory where the file is located.
- Run the script:
    ```bash
    $ python blackjack.py
    ```
- Follow the prompts to play the game.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.
1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## Contact
- Sakhile III  
- [LinkedIn Profile](https://www.linkedin.com/in/sakhile-ndlazi)
- [GitHub Profile](https://github.com/sakhileln)
