from utils import read_input
from collections import deque

puzzle_input = read_input(4)

def solve_part_1(puzzle_input):
    letter_queue = deque()
    puzzle = parse_crossword_puzzle(puzzle_input)
    xmases_found = 0
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    for i, line in enumerate(puzzle):
        for j, char in enumerate(line):
            if char == "X":
                for direction in directions:
                    letter_queue.append(("X", i, j, direction))

    while len(letter_queue) > 0:
        letter, i, j, direction = letter_queue.popleft()

        if letter == "S":
            xmases_found += 1
        else:
            valid_letters = check_for_next_valid_letter(puzzle, letter, i, j, direction)
            letter_queue.extend(valid_letters)
    
    return xmases_found

def check_for_next_valid_letter(puzzle, letter, i, j, direction):
    valid_letters = []
    letter_map = {'X': 'M', 'M': 'A', 'A': 'S'}
    
    if letter not in letter_map:
        return valid_letters
        
    next_letter = letter_map[letter]
    di, dj = direction
    
    new_i = i + di
    new_j = j + dj
    if (0 <= new_i < len(puzzle) and 
        0 <= new_j < len(puzzle[0]) and 
        puzzle[new_i][new_j] == next_letter):
        valid_letters.append((next_letter, new_i, new_j, direction))
            
    return valid_letters

def parse_crossword_puzzle(puzzle_input):
    # Split input into lines and convert each line into a list of characters
    return [list(line) for line in puzzle_input.strip().split('\n')]

print(solve_part_1(puzzle_input))
