import re

from TestRunner import run_tests
from inputs.input02 import puzzle_input, test_cases_b


INPUT_REGEX = '(\d+)-(\d+) (\w): (\w+)'


def solve(input):
    valid_passwords = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            parsed_values = re.search(INPUT_REGEX, line.strip())

            if is_valid(int(parsed_values[1]), int(parsed_values[2]), parsed_values[3], parsed_values[4]):
                valid_passwords += 1
    return valid_passwords


def is_valid(pos_a, pos_b, req_letter, password):
    letter_a = password[pos_a - 1]
    letter_b = password[pos_b - 1]
    return (letter_a == req_letter) ^ (letter_b == req_letter)


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
