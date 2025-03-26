class Validation:
    @staticmethod
    def validate_null_input(input_value):
        if not input_value or (
                isinstance(input_value, str) and input_value.strip() == ""):
            raise ValueError("입력이 비어 있습니다.")

    @staticmethod
    def validate_participate_name_length(input_participate):
        for person in input_participate:
            if len(person) > 5:
                raise ValueError(f"{person} 의 이름이 5자 이상입니다.")

    @staticmethod
    def validate_ladder_height_length(input_participate, input_ladder_height):
        if input_ladder_height < len(input_participate):
            raise ValueError("사다리의 높이가 참여하는 사람의 수보다 작습니다.")

    @staticmethod
    def validate_ladder_height(input_ladder_height):
        if input_ladder_height < 1 or input_ladder_height > 10:
            raise ValueError("사다리의 높이는 1~10 사이의 수여야 합니다.")

    @staticmethod
    def validate_game_result_type(input_game_result):
        for result in input_game_result:
            if result != "꽝" and not result.isnumeric():
                raise ValueError(f"{result} 는 올바른 결과가 아닙니다.")

    @staticmethod
    def validate_choice_result_person(input_choice_result_person, input_participate):
        if input_choice_result_person not in input_participate:
            raise ValueError(f"{input_choice_result_person} 는 참여하는 사람이 아닙니다.")

    @staticmethod
    def validate_game_result_length(input_participate, input_game_result):
        if len(input_participate) != len(input_game_result):
            raise ValueError("참여하는 사람과 실행 결과의 수가 같지 않습니다.")
