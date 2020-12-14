import re
import more_itertools

from TestRunner import run_tests
from inputs.input14 import puzzle_input, test_cases_b

MEM_REGEX = 'mem\[(\d+)\] = (\d+)'


def solve(input):
    memory = {}
    mask = ''
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            if line[:4] == 'mask':
                mask = line.split(' = ')[1]
            else:
                parts = re.search(MEM_REGEX, line)
                location = int(parts[1])
                value = int(parts[2])
                location_with_mask = apply_mask_to_location(location, mask)
                memory = store_value_in_memory(location_with_mask, value, memory)

    return sum([val for val in memory.values()])


def apply_mask_to_location(location, mask):
    val_as_bin = format(location, '036b')

    new_val = ''
    for m, v in zip(mask, val_as_bin):
        if m == '0':
            new_val += v
        if m == '1':
            new_val += '1'
        if m == 'X':
            new_val += 'X'

    return new_val


def store_value_in_memory(location_with_mask, value, memory):
    floating_indices = []
    location = list(location_with_mask)
    for i, loc in enumerate(location):
        if loc == 'X':
            floating_indices.append(pow(2, 36 - (i + 1)))
            location[i] = '0'

    base_location = int(''.join(location), 2)

    for a in more_itertools.powerset(floating_indices):
        memory[base_location + sum(a)] = value

    return memory


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
