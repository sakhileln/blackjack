"""
Test cases for the blackjack game.
"""

from helper import (
    deal_card,
    calculate_score
)
import unittest
from unittest.mock import patch


class TestDealCard(unittest.TestCase):
    """
    Test cases for blackjack functions 
    """
    @patch('helper.choice')  # Patch the helper.choice used in deal_card
    def test_deal_card_valid_values(self, mock_choice):
        """Test that deal_card returns a valid card (2-11)."""
        # Mock the random.choice to return 10 for this test
        mock_choice.return_value = 10
        # Call the function and check the result
        result = deal_card()
        # Assert that the result is in the valid set of card values
        self.assertIn(result, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    @patch('helper.choice')
    def test_card_randomness(self, mock_choice):
        """Test that deal_card returns a random value."""
        mock_choice.return_value = 7
        self.assertEqual(deal_card(), 7)

        mock_choice.return_value = 11
        self.assertEqual(deal_card(), 11)

        mock_choice.return_value = 3
        self.assertEqual(deal_card(), 3)

    @patch('helper.choice')
    def test_deal_card_multiple_calls(self, mock_choice):
        """Test mulitple calls deal_card returns same value."""
        mock_choice.return_value = 6
        for _ in range(21):
            self.assertEqual(deal_card(), 6)

    @patch('helper.choice')
    def test_deal_card_edge_cases(self, mock_choice):
        """Test deal_card when it has edge cases."""
        mock_choice.return_value = 11 # Aces
        self.assertEqual(deal_card(), 11)
        mock_choice.return_value = 2
        self.assertEqual(deal_card(), 2)

    def test_no_ace(self):
        """Test a hand with no ace, no adjustments needed."""
        hand = [2, 3, 4]
        self.assertEqual(calculate_score(hand), 9)
    
    def test_single_ace_no_bust(self):
        """Test a hand with a single Ace that doesn't bust."""
        hand = [10, 11]  # Ace is 11 here, score = 21
        self.assertEqual(calculate_score(hand), 21)

    def test_single_ace_with_bust(self):
        """Test a hand with a single Ace where the score exceeds 21 and needs adjustment."""
        hand = [10, 11, 6]  # Ace is 11, score = 27, adjust Ace to 1, score = 17
        self.assertEqual(calculate_score(hand), 17)

    def test_multiple_aces_no_bust(self):
        """Test a hand with multiple aces that doesn't bust."""
        hand = [11, 11, 9]  # score = 31, adjusted score = 21
        self.assertEqual(calculate_score(hand), 21)

    def test_multiple_aces_with_bust(self):
        """Test a hand with multiple aces where the score exceeds 21 and needs adjustments."""
        hand = [11, 11, 11, 10]  # score = 43, adjusted score = 13
        self.assertEqual(calculate_score(hand), 13)

    def test_empty_hand(self):
        """Test an empty hand, score 0."""
        hand = []
        self.assertEqual(calculate_score(hand), 0)


if __name__ == "__main__":
    unittest.main()