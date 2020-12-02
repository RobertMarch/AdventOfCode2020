from TestRunner import run_tests
from inputs.inputXX import puzzle_input, test_cases_a


def solve(input):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(line)
    return 1


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
