def calculate_result(ladder_structure, ladder_height):
    num_players = len(ladder_structure[0])+1
    positions = []

    for player in range(num_players):
        position = player
        for row in range(ladder_height):
            if position < num_players - 1 and ladder_structure[row][position].strip() != '':
                position += 1
            elif position > 0 and ladder_structure[row][position-1].strip() != '':
                position -= 1
        positions.append(position)
    return positions
