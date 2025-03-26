def match_name_and_position(participate_people, result_positions, game_results):
    results = {}
    for index, result_position in enumerate(result_positions):
        participate_name = participate_people[index]
        game_result = game_results[result_position]
        results[participate_name] = game_result
    return results
