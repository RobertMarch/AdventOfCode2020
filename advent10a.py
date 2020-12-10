from TestRunner import run_tests
from inputs.input10 import puzzle_input, test_cases_a


def solve(input):
    values = [0]
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line))

    values.sort()

    count_diff_1 = 0
    count_diff_3 = 1

    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        if diff == 1:
            count_diff_1 += 1
        elif diff == 3:
            count_diff_3 += 1

    return count_diff_1 * count_diff_3


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
