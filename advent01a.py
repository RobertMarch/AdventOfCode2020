import itertools

from TestRunner import run_tests
from inputs.input01 import puzzle_input, test_cases_a


def solve(input):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line.strip()))

    for [a, b] in itertools.combinations(values, 2):
        if a + b == 2020:
            return a * b


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
