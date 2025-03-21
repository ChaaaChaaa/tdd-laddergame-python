import unittest
from io import StringIO
from unittest.mock import patch
from src.script.output import print_result_text,print_ladder_participate_people,print_ladder_height

'''
- 결과 출력 테스트
- 참가자 이름 출력 테스트
- 사다리 높이 출력 테스트
'''

class TestOutputFunction(unittest.TestCase):
    @patch('sys.stdout',new_callable=StringIO)
    def test_print_result_text(self,mock_stdout):
        print_result_text()
        self.assertEqual(mock_stdout.getvalue(),"실행결과\n")

    @patch('sys.stdout',new_callable=StringIO)
    def test_print_ladder_participate_people(self,mock_stdout):
        participate_people_name = ["A","B","C"]
        ladder_participate_count = 3
        print_ladder_participate_people(participate_people_name,ladder_participate_count)
        self.assertEqual(mock_stdout.getvalue().strip(),"A  B  C")

    @patch('sys.stdout',new_callable=StringIO)
    def test_print_ladder_height(self,mock_stdout):
        ladder_structure = [
        ["   ", "---"],
        ["---", "   "]
        ]
        print_ladder_height(ladder_structure)
        expected_output = "|   |---|\n|---|   |"
        self.assertEqual(mock_stdout.getvalue().strip(),expected_output)

if __name__ == '__main__':
    unittest.main()
        