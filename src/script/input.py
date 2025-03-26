from src.utils.validation import Validation

from src.utils.validation import Validation

def get_validated_input(prompt):
    while True:
        try:
            input_value = input(prompt)
            Validation.validate_null_input(input_value)  # 검증 수행
            return input_value  # 검증 성공 시 반환
        except ValueError as e:
            print(e)  # 오류 메시지 출력 후 다시 입력 요청


def print_input_participate_people():
    input_participate_people = get_validated_input(
        "참여할 사람 이름을 입력하세요. (이름은 쉼표(,)로 구분하세요)\n"
    ).split(",")
    participate_people = [
        participate_name for participate_name in input_participate_people
        if not Validation.validate_participate_name_length(participate_name)
    ]
    return participate_people


def print_input_game_result(input_participate):
    input_game_result = get_validated_input(
        "실행 결과를 입력하세요. (결과는 쉼표(,)로 구분하세요)\n"
    ).split(",")
    game_result = [
        result for result in input_game_result
        if not Validation.validate_game_result_type(result) and
           not Validation.validate_game_result_length(input_game_result, input_participate)
    ]
    return game_result


def print_input_ladder_height(input_participate):
    input_ladder_height = int(get_validated_input("최대 사다리 높이는 몇 개인가요?\n"))
    if not Validation.validate_ladder_height(input_ladder_height) and \
       not Validation.validate_ladder_height_length(input_participate, input_ladder_height):
        return input_ladder_height


def print_input_choice_result_person(input_participate, input_game_result):
    choice_result_person = get_validated_input("결과를 보고 싶은 사람은? (q 입력시 종료)\n")
    if choice_result_person == "q":
        quit()
    elif not Validation.validate_choice_result_person(choice_result_person, input_participate) and \
         not Validation.validate_game_result_length(input_participate, input_game_result):
        return choice_result_person
