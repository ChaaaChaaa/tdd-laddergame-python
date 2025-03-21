import unittest
from unittest.mock import patch

import src.script.output as output
from src.ladder_maker.ladder_maker import LadderMaker
from src.script.input import print_input_participate_people, print_input_ladder_height


class TestSimulation(unittest.TestCase):
    '''
    patch decorator 
    특정 함수나 메서드를 모의(mock)하여 테스트 환경에서 실제로 호출되지 않도록 함
    대신, 지정한 반환 값을 사용하거나 호출 여부를 확인할 수 있다.
    일관성 -> 항상 동일한 결과 반환하도록 함
    '''

    @patch('builtins.input', side_effect=[
        'aa,bb,cc,dd,ee',
        5,
    ])
    # @patch('src.ladder_maker.ladder_maker.LadderMaker.make_width',
    #        return_value=["----", "    "])
    @patch('src.ladder_maker.random_line_maker.make_random_line', return_value=5) #매번 -----로 나오게 함
    @patch('src.script.output.print_ladder_participate_people')
    @patch('src.script.output.print_ladder_height')
    def test_full_simulation(self, mock_print_ladder_height,
                             mock_print_ladder_participate_people,
                             mock_make_random_line,
                             mock_input):
        # step1 : 사용자 입력 - 참여자 이름,최대 사다리 높이
        participate_people = print_input_participate_people()
        self.assertEqual(participate_people, ['aa', 'bb', 'cc', 'dd', 'ee'])

        ladder_height = print_input_ladder_height()
        self.assertEqual(ladder_height, 5)

        # step2: Ladder_Maker 객체 생성  
        ladder_maker = LadderMaker(participate_people, ladder_height)
                               

        # step3 : 사다리 가로 길이 생성
        ladder_structure = ladder_maker.make_width()
        # mock_make_width.assert_called_once()
        mock_make_random_line.assert_called()
        expected_structure = []
        for _ in range(ladder_height):
            expected_structure.append(
                ["-" * len(participate_people)] * (len(participate_people) - 1))
        self.assertEqual(ladder_structure, expected_structure)

        # step4 : 결과 출력
        output.print_ladder_participate_people(participate_people,
                                               len(participate_people))
        mock_print_ladder_participate_people.assert_called_once_with(participate_people,
                                                                     len(participate_people))

        output.print_ladder_height(ladder_structure)
        mock_print_ladder_height(ladder_structure)


if __name__ == '__main__':
    unittest.main()
