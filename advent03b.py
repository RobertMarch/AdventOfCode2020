from TestRunner import run_tests
from inputs.input03 import puzzle_input, test_cases_b


def solve(input):
    slopes = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    result = 1

    for slope in slopes:
        result *= calculate_trees_hit(input, slope[0], slope[1])

    return result


def calculate_trees_hit(input, x_step, y_step):
    trees_hit = 0
    current_offset = 0
    row_number = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            if row_number % y_step == 0:
                if line[current_offset] == '#':
                    trees_hit += 1
                current_offset = (current_offset + x_step) % len(line)
            row_number += 1
    return trees_hit


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
