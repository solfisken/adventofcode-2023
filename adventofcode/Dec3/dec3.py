import re

def is_symbol(char):
    return not char.isdigit() and char != '.'

def is_adjacent_to_symbol(x, y, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and is_symbol(grid[nx][ny]):
            return True
    return False

def sum_part_numbers(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file.readlines()]

    total_sum = 0
    rows, cols = len(grid), len(grid[0])

    def extract_number_sum(x, y):
        number_sum = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny].isdigit():
                        num_str = ''
                        while ny < cols and grid[nx][ny].isdigit():
                            num_str += grid[nx][ny]
                            grid[nx][ny] = '.'  
                            ny += 1
                        number_sum += int(num_str)
                        break
        return number_sum

    for x in range(rows):
        for y in range(cols):
            if is_symbol(grid[x][y]):
                total_sum += extract_number_sum(x, y)

    return total_sum


file_path = 'dec3.csv'
print(sum_part_numbers(file_path))