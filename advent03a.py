from TestRunner import run_tests
from inputs.input03 import puzzle_input, test_cases_a


def solve(input):
    trees_hit = 0
    current_offset = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            if line[current_offset] == '#':
                trees_hit += 1
            current_offset = (current_offset + 3) % len(line)
    return trees_hit


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
