file_path = 'dec2.csv'

with open(file_path, 'r') as file:
    game_data = file.readlines()
    
def is_game_possible(game_info, max_cubes):
    game_parts = game_info.split(':')
    game_id = int(game_parts[0].split()[1])
    rounds = game_parts[1].split(';')

    for round in rounds:
        cubes = round.strip().split(',')
        for cube in cubes:
            parts = cube.strip().split(' ')
            count, color = int(parts[0]), parts[1]
            if count > max_cubes[color]:
                return None

    return game_id

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

possible_game_ids_sum = sum(is_game_possible(game, max_cubes) for game in game_data if is_game_possible(game, max_cubes))
print(possible_game_ids_sum)
