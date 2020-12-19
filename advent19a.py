import itertools

from TestRunner import run_tests
from inputs.input19 import puzzle_input, test_cases_a


def solve(input):
    rule_input, messages = input.split('\n\n')
    rules = {}
    resolved_rules = {}
    for rule in rule_input.splitlines():
        rule_id, options = rule.split(': ')
        val = []
        if options.startswith('"'):
            val = [options.strip('"')]
            resolved_rules[rule_id] = val
        else:
            for opt in options.split(' | '):
                val.append(opt.split(' '))
        rules[rule_id] = val

    options, _ = find_options_for_id('0', rules, resolved_rules)

    count = 0
    for message in messages.splitlines():
        if message in options:
            count += 1

    return count


def find_options_for_id(rule_id, rules, resolved_rules):
    if rule_id in resolved_rules:
        return resolved_rules[rule_id], resolved_rules
    options = rules[rule_id]
    result_lists = []
    for option in options:
        vals = []
        for r in option:
            v, resolved_rules = find_options_for_id(r, rules, resolved_rules)
            vals.append(v)
        for z in itertools.product(*vals):
            result_lists.append(''.join(z))

    resolved_rules[rule_id] = result_lists
    return result_lists, resolved_rules


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
