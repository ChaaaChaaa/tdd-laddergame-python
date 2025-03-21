def print_input_participate_people():
    print("참여할 사람 이름을 입력하세요. (이름은 쉼표(,)로 구분하세요)")
    input_participate_people = input().split(",")
    participate_people = [participate_name for participate_name in
                          input_participate_people if len(participate_name) < 5]
    return participate_people


def print_input_ladder_height():
    print("최대 사다리 높이는 몇 개인가요?")
    input_ladder_height = int(input())
    return input_ladder_height
