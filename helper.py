"""
A module containing all helper functions
"""

from random import choice


def deal_card() -> int:
    """
    Returns a random card from the deck.

    Parameters.
        None
    Return
        card (int): Random card from deck.
    """
    # Aces are 11 and face cards are 10
    cards = [
        2,3,4,5,6,7,8,9,10,10,10,10,11
    ]
    return choice(cards)


def calculate_score(hand: list) -> int:
    """
    Calculate the score og given hand.

    Parameters:
        hand (list): Player hand
    Return:
        score (int): Total score of player hand
    """
    score = sum(hand)
    # Adjust for aces if if score is over 21
    while score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score


def display_hands(
    player_hand: list,
    dealer_hand: list,
    reveal_hand=False: bool
) -> None:
    """
    Dsiplay player and dealer hands.

    Parameters:
        player_hand (list): The player's hand
        dealer_hand (list): The dealer's hand
        reveal_hand (bool): Reveal dealer hand
    Return:
        None
    """
    print(f"Your hand: {player_hand}, current score: {calculate_score(player_hand)}")
    if reveal_hand:
        print(f"Dealer's hand: {dealer_hand}, score: {calculate_score(dealer_hand)}")
    else:
        print(f"Dealer's hand: [{dealer_hand[0]}, ?]")
