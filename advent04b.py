import re

from TestRunner import run_tests
from inputs.input04 import puzzle_input, test_cases_b


def solve(input):
    valid_count = 0
    entry = ''
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            entry = "{} {}".format(entry, line.strip()).strip()
        elif len(entry) > 0:
            valid_count += 1 if is_valid(entry) else 0
            entry = ''
    return valid_count


def is_valid(entry):
    expected_field_seen = {
        'byr': False,
        'iyr': False,
        'eyr': False,
        'hgt': False,
        'hcl': False,
        'ecl': False,
        'pid': False,
    }
    for field in entry.split(" "):
        key, value = field.split(":")
        if key == 'byr':
            expected_field_seen[key] = 1920 <= int(value) <= 2002
        elif key == 'iyr':
            expected_field_seen[key] = 2010 <= int(value) <= 2020
        elif key == 'eyr':
            expected_field_seen[key] = 2020 <= int(value) <= 2030
        elif key == 'hgt':
            units = value[-2:]
            val = value[:-2]
            if units == "cm":
                expected_field_seen[key] = 150 <= int(val) <= 193
            elif units == "in":
                expected_field_seen[key] = 59 <= int(val) <= 76
        elif key == 'hcl':
            expected_field_seen[key] = re.search('#[0-9a-f]{6}', value) is not None and len(value) == 7
        elif key == 'ecl':
            expected_field_seen[key] = value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif key == 'pid':
            expected_field_seen[key] = len(value) == 9 and int(value)

    return all(f for f in expected_field_seen.values())


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
