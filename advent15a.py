from TestRunner import run_tests
from inputs.input15 import puzzle_input, test_cases_a


def solve(input):
    last_seen_index = {}
    previous_value = ''
    starters = input.split(',')
    for i, starter in enumerate(starters):
        previous_value = int(starter)
        if i < len(starters) - 1:
            last_seen_index[int(starter)] = i

    for i in range(len(starters) - 1, 2019):
        if previous_value in last_seen_index:
            next_value = i - last_seen_index[previous_value]
        else:
            next_value = 0
        last_seen_index[previous_value] = i
        previous_value = next_value

    return previous_value


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
