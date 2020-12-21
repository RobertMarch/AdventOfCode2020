from TestRunner import run_tests
from inputs.input21 import puzzle_input, test_cases_a


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

    non_allergens = all_ingredients.copy()
    for al in possible_allergen_sources:
        non_allergens.difference_update(possible_allergen_sources[al])

    count = 0
    for food in foods:
        ing_set = set(food[0])
        count += len(ing_set.intersection(non_allergens))

    return count


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
