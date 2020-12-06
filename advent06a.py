from TestRunner import run_tests
from inputs.input06 import puzzle_input, test_cases_a


def solve(input):
    count = 0
    answer_set = set()
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            for ans in line:
                answer_set.add(ans)
        else:
            count += len(answer_set)
            answer_set.clear()
    return count


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
