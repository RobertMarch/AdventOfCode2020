from TestRunner import run_tests
from inputs.input13 import puzzle_input, test_cases_a


def solve(input):
    best_id = -1
    shortest_wait = 1000000
    lines = input.split('\n')
    target = int(lines[0])
    bus_ids = lines[1].split(',')
    for id in bus_ids:
        if id.isdigit():
            id_num = int(id)
            wait = id_num - (target % id_num)
            if wait < shortest_wait:
                shortest_wait = wait
                best_id = id_num
    return best_id * shortest_wait


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
