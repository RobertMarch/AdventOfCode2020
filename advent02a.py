import re

from TestRunner import run_tests
from inputs.input02 import puzzle_input, test_cases_a


INPUT_REGEX = '(\d+)-(\d+) (\w): (\w+)'


def solve(input):
    valid_passwords = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            parsed_values = re.search(INPUT_REGEX, line.strip())

            if is_valid(int(parsed_values[1]), int(parsed_values[2]), parsed_values[3], parsed_values[4]):
                valid_passwords += 1
    return valid_passwords


def is_valid(min_count, max_count, req_letter, password):
    count = 0
    for letter in password:
        if letter == req_letter:
            count += 1
    return min_count <= count <= max_count


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
