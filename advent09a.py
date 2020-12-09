import itertools

from TestRunner import run_tests
from inputs.input09 import puzzle_input, test_cases_a


def solve(input, window=25):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line))
    return get_first_invalid_value(values, window)


def get_first_invalid_value(values, window):
    for i in range(window, len(values)):
        prev_values = values[i - window: i]
        if values[i] not in get_valid_sums(prev_values):
            return values[i]


def get_valid_sums(prev_values):
    return set([a + b for [a, b] in itertools.combinations(prev_values, 2)])


if __name__ == "__main__":
    run_tests(test_cases_a, solve, 5)
    print(solve(puzzle_input, 25))
