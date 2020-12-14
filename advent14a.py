import re

from TestRunner import run_tests
from inputs.input14 import puzzle_input, test_cases_a


MEM_REGEX = 'mem\[(\d+)\] = (\d+)'


def solve(input):
    memory = {}
    mask = ''
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            if line[:4] == 'mask':
                mask = update_mask(line)
            else:
                parts = re.search(MEM_REGEX, line)
                location = int(parts[1])
                value = int(parts[2])
                memory[location] = apply_mask_to_value(value, mask)
    return sum([val for val in memory.values()])


def update_mask(line):
    return line.split(' = ')[1]


def apply_mask_to_value(value, mask):
    val_as_bin = format(value, '036b')

    new_val = ''
    for m, v in zip(mask, val_as_bin):
        if m == 'X':
            new_val += v
        else:
            new_val += m

    return int(new_val, 2)


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
