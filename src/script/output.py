def print_result_text():
    print("실행결과")


def print_ladder_participate_people(participate_people_name, ladder_participate_count):
    seperator = " " * (ladder_participate_count-1)
    print(seperator.join(participate_people_name))


def print_ladder_height(ladder_structure):
    for segment in ladder_structure:
        print("|" + "|".join(segment) + "|")
