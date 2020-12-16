from TestRunner import run_tests
from inputs.input16 import puzzle_input, test_cases_a


def solve(input):
    groups = input.split('\n\n')
    rules = groups[0]
    nearby_tickets = groups[2]

    valid_numbers = get_valid_numbers(rules)

    invalid_count = 0
    for ticket in nearby_tickets.splitlines():
        if ticket == 'nearby tickets:':
            continue
        vals = [int(v) for v in ticket.split(',')]
        for val in vals:
            if val not in valid_numbers:
                invalid_count += val

    return invalid_count


def get_valid_numbers(rules):
    valid_numbers = set()
    for rule in rules.splitlines():
        name, values = rule.split(': ')
        ranges = values.split(' or ')
        for r in ranges:
            start, end = r.split('-')
            for i in range(int(start), int(end)+1):
                valid_numbers.add(i)
    return valid_numbers


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
