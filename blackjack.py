"""
A main backjack module for the game.
"""

from helper import (
    deal_card,
    calculate_score,
    display_hands
)

def backjack() -> None:
    """Main function to play blackjack."""
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        ...

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deal_card())

    display_hands(player_hand, dealer_hand, reveal_hand=True)
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("You lose")
    else:
        print("It's a draw")


if __name__ == "__main__":
    # Start game
    blackjack()