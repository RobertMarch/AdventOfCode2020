import itertools

from TestRunner import run_tests
from inputs.input09 import puzzle_input, test_cases_b


def solve(input, window=25):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line))

    invalid_index = get_first_invalid_index(values, window)
    invalid_value = values[invalid_index]

    i, j = 0, 1
    while j < invalid_index:
        ij_values = [values[k] for k in range(i, j + 1)]
        ij_sum = sum(ij_values)
        if ij_sum > invalid_value:
            i += 1
        elif ij_sum < invalid_value:
            j += 1
        else:
            return min(ij_values) + max(ij_values)


def get_first_invalid_index(values, window):
    for i in range(window, len(values)):
        prev_values = values[i - window: i]
        if values[i] not in get_valid_sums(prev_values):
            return i


def get_valid_sums(prev_values):
    return set([a + b for [a, b] in itertools.combinations(prev_values, 2)])


if __name__ == "__main__":
    run_tests(test_cases_b, solve, 5)
    print(solve(puzzle_input, 25))
