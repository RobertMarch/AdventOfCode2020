from TestRunner import run_tests
from inputs.input21 import puzzle_input, test_cases_b


def solve(input):
    foods = []
    for line in input.splitlines():
        ingredients, allergens = line.rstrip(')').split(' (contains ')
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')
        foods.append([ingredients, allergens])

    all_ingredients = set()
    all_allergens = set()
    for food in foods:
        [all_ingredients.add(ingredient) for ingredient in food[0]]
        [all_allergens.add(allergen) for allergen in food[1]]

    possible_allergen_sources = {allergen: all_ingredients.copy() for allergen in all_allergens}

    for food in foods:
        for allergen in food[1]:
            possible_allergen_sources[allergen].intersection_update(set(food[0]))

    allergen_sources = {}
    while len(possible_allergen_sources) > 0:
        for allergen in possible_allergen_sources:
            sources = possible_allergen_sources[allergen]
            if len(sources) == 1:
                source = sources.pop()
                allergen_sources[allergen] = source
                possible_allergen_sources.pop(allergen)
                for al_sources in possible_allergen_sources.values():
                    al_sources.discard(source)
                break

    return ','.join([allergen_sources[allergen] for allergen in sorted(allergen_sources.keys())])


if __name__ == "__main__":
    # run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
