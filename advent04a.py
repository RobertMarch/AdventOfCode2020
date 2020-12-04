from TestRunner import run_tests
from inputs.input04 import puzzle_input, test_cases_a


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
        'cid': True,
    }
    for field in entry.split(" "):
        key, value = field.split(":")
        expected_field_seen[key] = True
    return all(f for f in expected_field_seen.values())


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
