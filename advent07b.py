from TestRunner import run_tests
from inputs.input07 import puzzle_input, test_cases_b


def solve(input):
    parent_to_children = {}
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            parent, children = line.split(' contain ')
            parent_colour = ' '.join(parent.split(' ')[0:2])
            parent_to_children[parent_colour] = []

            if children == 'no other bags.':
                continue

            children.replace('.', '')

            for child in children.split(', '):
                words = child.split(' ')
                quantity = int(words[0])
                colour = ' '.join(words[1:3])
                parent_to_children[parent_colour].append([quantity, colour])

    return count_child_bags("shiny gold", parent_to_children)


def count_child_bags(colour, parent_to_children):
    children = parent_to_children[colour]
    return sum([c_num * (1 + count_child_bags(c_colour, parent_to_children)) for [c_num, c_colour] in children])


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
