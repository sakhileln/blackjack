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