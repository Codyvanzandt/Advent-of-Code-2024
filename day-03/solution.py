from utils import read_input
import re

puzzle_input = read_input(3)

def solve_part_1(puzzle_input):
    result = 0
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input):
        num1, num2 = re.findall(r"\d{1,3}", match)
        result += int(num1) * int(num2)
    return result


def solve_part_2(puzzle_input):
    result = 0
    perform_calculation = True
    for instruction in find_all_valid_instructions(puzzle_input):
        if is_do_instruction(instruction):
            perform_calculation = True
        elif is_don_t_instruction(instruction):
            perform_calculation = False
        elif is_valid_mul_instruction(instruction) and perform_calculation:
            num1, num2 = re.findall(r"\d{1,3}", instruction)
            result += int(num1) * int(num2)
    return result

def find_all_valid_instructions(puzzle_input):
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don['']t\(\)", puzzle_input)
    return instructions

def is_do_instruction(match):
    return match == "do()"

def is_don_t_instruction(match):
    return match == "don't()"

def is_valid_mul_instruction(match):
    return re.match(r"mul\(\d{1,3},\d{1,3}\)", str(match)) is not None 

print(solve_part_1(puzzle_input))
print(solve_part_2(puzzle_input))
