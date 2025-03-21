import unittest
from unittest.mock import patch
from src.script.input import print_input_participate_people, print_input_ladder_height

'''
- 참가자 이름 입력 테스트
- 참가자 이름 길이 테스트
- 사다리 높이 입력 테스트
'''

class TestInputFunction(unittest.TestCase):
    @patch('builtins.input',return_value="A,B,C,D,E")
    def test_print_input_participate_people(self,mock_input):
        result = print_input_participate_people()
        expected_result = ["A","B","C","D","E"]
        self.assertEqual(result,expected_result)

    @patch('builtins.input',return_value="A,B,CDEFG,H")
    def test_print_input_participate_people_with_name_length(self,mock_input):
        result = print_input_participate_people()
        expected_result = ["A","B","H"]
        self.assertEqual(result,expected_result)

    @patch('builtins.input',return_value="5")
    def test_print_input_ladder_height(self,mock_input):
        result = print_input_ladder_height()
        self.assertEqual(result,5)

if __name__ == '__main__':
    unittest.main()
    
        
