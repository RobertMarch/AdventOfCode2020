import itertools

from TestRunner import run_tests
from inputs.input19 import puzzle_input, test_cases_b


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

    options42, resolved_rules = find_options_for_id('42', rules, resolved_rules)
    options31, resolved_rules = find_options_for_id('31', rules, resolved_rules)

    count = 0
    for message in messages.splitlines():
        count42, count31 = 0, 0
        change_made = True

        while len(message) > 0 and change_made == True:
            change_made = False
            for opt in options42:
                if message.startswith(opt):
                    count42 += 1
                    message = message[len(opt):]
                    change_made = True
            if count42 >= 2 and count42 > count31 + 1:
                for opt in options31:
                    if message.endswith(opt):
                        count31 += 1
                        message = message[:-1 * len(opt)]
                        change_made = True

        if len(message) == 0 and count42 > count31 > 0:
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
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
