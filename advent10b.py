from TestRunner import run_tests
from inputs.input10 import puzzle_input, test_cases_b


def solve(input):
    values = [0]
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line))

    values.sort()

    prev_values = [
        [0, 1]
    ]

    for i in range(1, len(values)):
        val = values[i]
        routes = 0
        for prev in prev_values:
            if val - prev[0] <= 3:
                routes += prev[1]
            else:
                prev_values = prev_values[:prev_values.index(prev)]
                break
        prev_values.insert(0, [val, routes])

    return prev_values[0][1]


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
