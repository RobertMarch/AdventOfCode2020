import itertools

from TestRunner import run_tests
from inputs.input01 import puzzle_input, test_cases_b


def solve(input):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line.strip()))

    for [a, b, c] in itertools.combinations(values, 3):
        if a + b + c == 2020:
            return a * b * c


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
