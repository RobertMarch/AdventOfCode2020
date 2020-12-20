from TestRunner import run_tests
from inputs.input20 import puzzle_input, test_cases_a


def solve(input):
    tile_edges = {}
    for tile in input.split('\n\n'):
        lines = tile.splitlines()
        tile_id = int(lines[0][5:-1])
        right_edge = ''.join([l[-1] for l in lines[1:]])
        left_edge = ''.join([l[0] for l in lines[1:]])
        edges = [lines[1], right_edge, lines[-1], left_edge]
        tile_edges[tile_id] = edges

    edge_counts = {}

    for edges in tile_edges.values():
        for edge in edges:
            e = edge if edge > edge[::-1] else edge[::-1]
            if e in edge_counts:
                edge_counts[e] += 1
            else:
                edge_counts[e] = 1

    tile_id_product = 1

    for tile in tile_edges:
        unmatched_edges = 0
        for edge in tile_edges[tile]:
            e = edge if edge > edge[::-1] else edge[::-1]
            if edge_counts[e] == 1:
                unmatched_edges += 1
        if unmatched_edges == 2:
            tile_id_product *= tile

    return tile_id_product


if __name__ == "__main__":
    run_tests(test_cases_a, solve)
    print(solve(puzzle_input))
