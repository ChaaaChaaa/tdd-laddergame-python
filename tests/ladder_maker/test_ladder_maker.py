import unittest
from unittest.mock import patch
from src.ladder_maker.ladder_maker import LadderMaker

'''
- 사다리 크기(높이,너비)가 맞는지 확인	
- 각 칸이 정확히 가로줄 또는 공백으로만 이루어졌는지 확인	
- 랜덤성을 고정하여 항상 가로줄만 나오는지 확인	모든 칸="---"
- 특수한 경우(참가자 한명)도 잘 처리되는지 확인
'''

class TestLadderMaker(unittest.TestCase):
    def test_ladder_structure(self):
        participants = ["A", "B", "C", "D"]
        ladder_height = 5

        ladder_maker = LadderMaker(participants, ladder_height)
        ladder_width = ladder_maker.make_width()

        self.assertEqual(len(ladder_width), ladder_height)

        for row in ladder_width:
            self.assertEqual(len(row), ladder_maker.ladder_participate_count - 1)

    def test_ladder_structure_garo_or_blank(self):
        participants = ["A", "B", "C"]
        ladder_height = 10

        ladder_maker = LadderMaker(participants, ladder_height)
        ladder_width = ladder_maker.make_width()

        for row in ladder_width:
            for segment in row:
                self.assertIn(segment, [ladder_maker.seperator, " " * ladder_maker.ladder_participate_count])

    @patch('src.ladder_maker.random_line_maker.make_random_line',return_value=3)
    def test_ladder_structure_random_line(self,mock_make_random_line):
        participants = ["A","B","C"]
        ladder_height = 5

        ladder_maker = LadderMaker(participants,ladder_height)
        ladder_width = ladder_maker.make_width()

        expected_result = [
            [ladder_maker.seperator for _ in range(ladder_maker.ladder_participate_count - 1)]
             for _ in range(ladder_height)
        ]

        self.assertEqual(ladder_width,expected_result)

    def test_ladder_edge_case(self):
        participates=["D"]
        ladder_height=1

        ladder_maker = LadderMaker(participates,ladder_height)
        ladder_width = ladder_maker.make_width()

        self.assertEqual(ladder_width,[[]])

if __name__ == '__main__':
    unittest.main()
    