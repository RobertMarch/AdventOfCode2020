from TestRunner import run_tests
from inputs.input01 import puzzle_input, test_cases_b


def solve(input):
    values = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            values.append(int(line.strip()))
    values.sort()

    for i in range(len(values) - 1, 0, -1):
        val_i = values[i]
        for j in range(0, i - 1):
            val_j = values[j]
            for k in range(j + 1, i):
                val_k = values[k]
                if val_i + val_j + val_k == 2020:
                    return val_i * val_j * val_k
                elif val_i + val_j + val_k > 2020:
                    break
            if val_i + val_j > 2020:
                break


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
