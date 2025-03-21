from src.ladder_maker.ladder_maker import LadderMaker
from src.script.input import print_input_participate_people, print_input_ladder_height
from src.script.output import print_ladder_height, print_ladder_participate_people, \
    print_result_text


def print_input_info():
    participate_people = print_input_participate_people()
    ladder_height = print_input_ladder_height()
    return participate_people, ladder_height


def make_ladder(participate_people, ladder_height):
    ladder_maker = LadderMaker(participate_people, ladder_height)
    ladder_structure = ladder_maker.make_width()
    return ladder_structure


def print_result(participate_people, ladder_structure):
    print_result_text()
    print_ladder_participate_people(participate_people, len(participate_people))
    print_ladder_height(ladder_structure)


def main():
    participate_people, ladder_height = print_input_info()
    ladder_structure = make_ladder(participate_people, ladder_height)
    print_result(participate_people, ladder_structure)


if __name__ == '__main__':
    main()
