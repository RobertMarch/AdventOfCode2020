from TestRunner import run_tests
from inputs.input18 import puzzle_input, test_cases_b


def solve(input):
    total = 0
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            total += evaluate_expression(line)

    return total


def evaluate_expression(expression):
    expression += ' '
    items_to_depth = []
    depth = 0
    val = ''
    for c in expression:
        if c == '(':
            depth += 1
        elif c == ')':
            if val != '':
                items_to_depth.append([int(val), depth])
                val = ''
            depth -= 1
        elif c != ' ':
            val += c
        elif val != '':
            val_to_store = int(val) if val.isdigit() else val
            items_to_depth.append([val_to_store, depth])
            val = ''

    return evaluate(items_to_depth)


def evaluate(items):
    while len(items) > 1:
        for i in range(0, len(items), 2):
            if (i == 0 or items[i - 1][1] < items[i][1]) and (i == (len(items) - 1) or items[i + 1][1] < items[i][1]):
                items[i][1] -= 1
                break

        addition_made = False
        for i in range(0, len(items) - 2, 2):
            if items[i][1] == items[i+1][1] == items[i+2][1] and items[i+1][0] == '+':
                items[i][0] = items[i][0] + items[i+2][0]
                addition_made = True
                del items[i + 1: i + 3]
                break

        if not addition_made:
            max_depth = max([i[1] for i in items])
            for i in range(0, len(items) - 2, 2):
                if items[i][1] == items[i + 1][1] == items[i + 2][1] and items[i + 1][0] == '*' and items[i][1] == max_depth:
                    items[i][0] = items[i][0] * items[i + 2][0]
                    del items[i + 1: i + 3]
                    break

    return items[0][0]


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
