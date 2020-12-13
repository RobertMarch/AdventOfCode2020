import math

from TestRunner import run_tests
from inputs.input13 import puzzle_input, test_cases_b


def solve(input):
    lines = input.split('\n')

    bus_ids = []
    bus_ids_to_offset = {}
    for i, id in enumerate(lines[1].split(',')):
        if id.isdigit():
            id_num = int(id)
            bus_ids.append(id_num)
            bus_ids_to_offset[id_num] = i
    bus_ids.sort(reverse=True)

    max_id = bus_ids[0]
    t = max_id - bus_ids_to_offset[max_id]
    matched_buses = [max_id]

    while not len(matched_buses) == len(bus_ids):
        t += math.prod(matched_buses)
        matched_buses = get_matched_buses(t, bus_ids_to_offset)

    return t


def get_matched_buses(t, bus_ids_to_offset):
    return [bus_id for bus_id in bus_ids_to_offset.keys() if (t + bus_ids_to_offset[bus_id]) % bus_id == 0]


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
