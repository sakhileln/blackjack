"""
Test cases for the blackjack game.
"""

from helper import deal_card
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


if __name__ == "__main__":
    unittest.main()