from TestRunner import run_tests
from inputs.input05 import puzzle_input, test_cases_a


def solve(input):
    max_id = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            value = calculate_seat_id(line)
            max_id = max(max_id, value)
    return max_id


def calculate_seat_id(value):
    row = extract_bin_value(value[:7], "F", "B")
    column = extract_bin_value(value[7:], "L", "R")
    return row * 8 + column


def extract_bin_value(value: str, zero_char, one_char):
    bin_value_as_string = value.replace(zero_char, "0").replace(one_char, "1")
    return int(bin_value_as_string, 2)


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
