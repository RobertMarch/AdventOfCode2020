import string

from TestRunner import run_tests
from inputs.input06 import puzzle_input, test_cases_b


def solve(input):
    count = 0
    answer_set = set([c for c in string.ascii_lowercase])
    input = input.strip("\n") + "\n"
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            answer_set.intersection_update([c for c in line])
        else:
            count += len(answer_set)
            answer_set = set([c for c in string.ascii_lowercase])
    return count


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
