from utils import read_input

puzzle_input = read_input(1)

def parse_puzzle_input(puzzle_input):
    lines = puzzle_input.strip().split('\n')
    first_col = []
    second_col = []
    for line in lines:
        if line:
            num1, num2 = map(int, line.split())
            first_col.append(num1)
            second_col.append(num2)
    return first_col, second_col

def solve_part_1(first_col, second_col):
    first_col.sort()
    second_col.sort()
    return sum(abs(a-b) for a, b in zip(first_col, second_col))

def solve_part_2(first_col, second_col):
    similarity_score = 0
    for num in first_col:
        count = second_col.count(num)
        similarity_score += num * count
    return similarity_score

print(solve_part_1(*parse_puzzle_input(puzzle_input)))
print(solve_part_2(*parse_puzzle_input(puzzle_input)))
print("Hello world!")
