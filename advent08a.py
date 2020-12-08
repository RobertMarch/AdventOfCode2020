from TestRunner import run_tests
from inputs.input08 import puzzle_input, test_cases_a


class Instruction:
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def run(self, accumulator, index):
        if self.op == 'acc':
            accumulator += self.arg
            index += 1
        elif self.op == 'jmp':
            index += self.arg
        else:
            index += 1
        return accumulator, index


def solve(input):
    instructions = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            instructions.append(parse_line(line))

    accumulator = 0
    index = 0
    indexes_run = set()

    while index not in indexes_run:
        indexes_run.add(index)
        accumulator, index = instructions[index].run(accumulator, index)

    return accumulator


def parse_line(line):
    parts = line.split(' ')
    return Instruction(parts[0], int(parts[1]))


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
