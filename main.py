from src.ladder_maker.ladder_maker import LadderMaker
from src.script.input import print_input_participate_people, print_input_ladder_height, \
    print_input_choice_result_person, print_input_game_result
from src.script.output import print_ladder_height, print_ladder_participate_people, \
    print_result_text, print_game_result_choice_person, print_ladder_game_result
from src.result_calculator.calculator import calculate_result
from src.result_calculator.matcher import match_name_and_position


def print_input_info():
    participate_people = print_input_participate_people()
    ladder_height = print_input_ladder_height(participate_people)
    game_result = print_input_game_result(participate_people)
    return participate_people, ladder_height, game_result


def make_ladder(participate_people, ladder_height):
    ladder_maker = LadderMaker(participate_people, ladder_height)
    ladder_structure = ladder_maker.make_width()
    return ladder_structure


def print_input_result_person(participate_people, game_result):
    choice_result_person = print_input_choice_result_person(participate_people,
                                                            game_result)
    return choice_result_person


def print_ladder_result(participate_people, ladder_structure, game_result,
                        ladder_participate_count):
    print_result_text()
    print_ladder_participate_people(participate_people, len(participate_people))
    print_ladder_height(ladder_structure)
    print_ladder_game_result(game_result, ladder_participate_count)


def get_game_match_result(participate_people, ladder_structure, ladder_height,
                          game_results):
    positions = calculate_result(ladder_structure, ladder_height)
    results = match_name_and_position(participate_people, positions, game_results)
    return results


def print_game_result(participate_people, match_results):
    while True:
        choice_result_person = print_input_choice_result_person(participate_people,
                                                                match_results)
        print_game_result_choice_person(choice_result_person, match_results)


def main():
    participate_people, ladder_height, game_result = print_input_info()
    ladder_structure = make_ladder(participate_people, ladder_height)
    print_ladder_result(participate_people, ladder_structure, game_result,
                        len(participate_people))
    match_results = get_game_match_result(participate_people, ladder_structure,
                                          ladder_height, game_result)
    print_game_result(participate_people, match_results)


if __name__ == '__main__':
    main()
