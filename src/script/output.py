def print_result_text():
    print("사다리 결과")


def print_ladder_participate_people(participate_people_name, ladder_participate_count):
    seperator = " " * (ladder_participate_count - 1)
    print(seperator.join(participate_people_name))


def print_ladder_height(ladder_structure):
    for segment in ladder_structure:
        print("|" + "|".join(segment) + "|")


# print_ladder_game_result랑 print_ladder_result_choice_person이름 차이를 어떻게 둬야할지 모르겠음
def print_ladder_game_result(game_result, ladder_participate_count):
    seperator = " " * (ladder_participate_count - 1)
    print(seperator.join(game_result))


def print_game_result_choice_person(choice_result_person, match_results):
    print("실행 결과")
    if choice_result_person == "all":
        for participant in match_results:
            print(participant,":",match_results.get(participant))
    elif choice_result_person == "q" or choice_result_person is None:
        return quit()
    else:
        return print(match_results.get(choice_result_person))
