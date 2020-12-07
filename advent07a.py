from TestRunner import run_tests
from inputs.input07 import puzzle_input, test_cases_a


def solve(input):
    colour_to_parents = {}
    for line in input.split('\n'):
        if len(line.strip()) > 0:
            parent, children = line.split(' contain ')
            parent_colour = ' '.join(parent.split(' ')[0:2])

            if children == 'no other bags.':
                continue
            children.replace('.', '')

            for child in children.split(', '):
                words = child.split(' ')
                colour = ' '.join(words[1:3])
                if colour not in colour_to_parents:
                    colour_to_parents[colour] = [parent_colour]
                else:
                    colour_to_parents[colour].append(parent_colour)

    external_colours = set()

    find_parent_colours("shiny gold", colour_to_parents, external_colours)
    return len(external_colours)


def find_parent_colours(colour, colour_to_parent, external_colours):
    for c in colour_to_parent[colour]:
        external_colours.add(c)
        if c in colour_to_parent:
            find_parent_colours(c, colour_to_parent, external_colours)


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
