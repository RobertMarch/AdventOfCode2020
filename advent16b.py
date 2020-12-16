from TestRunner import run_tests
from inputs.input16 import puzzle_input, test_cases_b


def solve(input):
    groups = input.split('\n\n')
    rules = groups[0]
    my_ticket_values = [int(v) for v in groups[1].splitlines()[1].split(',')]
    nearby_tickets = groups[2]

    rule_dict, valid_numbers = parse_rules(rules)

    valid_tickets = get_valid_tickets(nearby_tickets, valid_numbers)

    field_values = map_valid_tickets_to_field_values(valid_tickets, my_ticket_values)

    field_name_to_index = {}

    while len(field_name_to_index) < len(rule_dict.keys()):
        for field_name in rule_dict.keys():
            if field_name in field_name_to_index.keys():
                continue
            possible_field_indexes = []
            for index in range(len(field_values)):
                if index in field_name_to_index.values():
                    continue
                if rule_dict[field_name].issuperset(field_values[index]):
                    possible_field_indexes.append(index)
            if len(possible_field_indexes) == 1:
                field_name_to_index[field_name] = possible_field_indexes[0]

    result = 1
    for field in field_name_to_index.keys():
        if field.startswith('departure'):
            result *= my_ticket_values[field_name_to_index[field]]

    return result


def parse_rules(rules):
    rule_dict = {}
    valid_numbers = set()

    for rule in rules.splitlines():
        rule_valid_numbers = set()
        name, values = rule.split(': ')
        ranges = values.split(' or ')
        for r in ranges:
            start, end = r.split('-')
            for i in range(int(start), int(end)+1):
                rule_valid_numbers.add(i)

        rule_dict[name] = rule_valid_numbers
        valid_numbers.update(rule_valid_numbers)
    return rule_dict, valid_numbers


def get_valid_tickets(nearby_tickets, valid_numbers):
    valid_tickets = []

    for ticket in nearby_tickets.split('\n'):
        if ticket == 'nearby tickets:':
            continue
        vals = [int(v) for v in ticket.split(',')]
        if all([v in valid_numbers for v in vals]):
            valid_tickets.append(vals)

    return valid_tickets


def map_valid_tickets_to_field_values(valid_tickets, my_ticket):
    return [set(x) for x in zip(*valid_tickets, my_ticket)]


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
