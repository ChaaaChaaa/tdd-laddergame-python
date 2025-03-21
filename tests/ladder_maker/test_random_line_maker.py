import unittest
from unittest.mock import patch
from src.ladder_maker.random_line_maker import make_random_line

class TestRandomLineMaker(unittest.TestCase):
    
    @patch('random.choice',return_value=0)
    def test_make_random_line_zero(self,mock_random_choice):
        ladder_participate_count = 3
        result = make_random_line(ladder_participate_count)
        self.assertEqual(result,0)

    @patch('random.choice',return_value=3)
    def test_make_random_line_max(self,mock_random_choice):
        ladder_participate_count = 3
        result = make_random_line(ladder_participate_count)
        self.assertEqual(result,3)

if __name__ == '__main__':
    unittest.main()

    