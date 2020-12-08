from TestRunner import run_tests
from inputs.input08 import puzzle_input, test_cases_b


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
        elif self.op == 'nop':
            index += 1
        return accumulator, index


def solve(input):
    instructions = []
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            instructions.append(parse_line(line))

    for i in range(len(instructions)):
        if instructions[i].op in ['nop', 'jmp']:
            result = run_instructions_with_change(instructions, i)
            if result is not None:
                return result


def parse_line(line):
    parts = line.split(' ')
    return Instruction(parts[0], int(parts[1]))


def run_instructions_with_change(instructions, i):
    original_op = instructions[i].op
    instructions[i].op = 'nop' if original_op == 'jmp' else 'jmp'

    accumulator = 0
    index = 0
    indexes_run = set()

    while index not in indexes_run and 0 <= index < len(instructions):
        indexes_run.add(index)
        accumulator, index = instructions[index].run(accumulator, index)

    instructions[i].op = original_op
    return accumulator if index == len(instructions) else None


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
