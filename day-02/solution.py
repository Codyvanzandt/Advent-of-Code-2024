from utils import read_input

puzzle_input = read_input(2)

def parse_puzzle_input(puzzle_input):
    reports = puzzle_input.strip().split('\n')
    result = []
    for report in reports:
        numbers = [int(num) for num in report.split()]
        result.append(numbers)
    return result

def solve_part_1(puzzle_input):
    reports = parse_puzzle_input(puzzle_input)
    num_safe_reports = 0
    for report in reports:
        if is_report_safe(report):
            num_safe_reports += 1
    return num_safe_reports


def is_report_safe(numbers):
    if len(numbers) < 2:
        return True
    differences = [numbers[i+1] - numbers[i] for i in range(len(numbers) - 1)]
    return all(1 <= diff <= 3 for diff in differences) or all(-3 <= diff <= -1 for diff in differences)

def solve_part_2(puzzle_input):
    reports = parse_puzzle_input(puzzle_input)
    safe_reports_with_one_removed_max = 0
    for report in reports:
        safe = is_report_safe(report)
        safe_with_removal = any(is_report_safe(report[:i] + report[i+1:]) for i in range(len(report)))
        if safe or safe_with_removal:
            safe_reports_with_one_removed_max += 1
    return safe_reports_with_one_removed_max

print(solve_part_1(puzzle_input))
print(solve_part_2(puzzle_input))
