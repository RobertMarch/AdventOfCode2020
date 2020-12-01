from TestRunner import run_tests
from inputs.input01 import puzzle_input, test_cases_a


def solve(input):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line.strip()))
    values.sort()
    i, j = 0, len(values) - 1
    while j > i:
        val_i = values[i]
        val_j = values[j]
        if val_i + val_j == 2020:
            return val_i * val_j
        elif val_i + val_j > 2020:
            j -= 1
        else:
            i += 1


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
