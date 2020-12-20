import numpy as np

from TestRunner import run_tests
from inputs.input20 import puzzle_input, test_cases_b


HERE_BE_MONSTERS = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''


def solve(input):
    tile_edges, tile_centres = extract_tile_maps(input)

    edge_to_tiles = construct_edge_to_id_map(tile_edges)

    image, next_row_top_edge, previous_first_id, next_edge = get_first_corner(tile_edges, edge_to_tiles, tile_centres)

    image = fill_row(previous_first_id, next_edge, image, tile_edges, tile_centres, edge_to_tiles)

    while len(get_tile_ids_for_edge(next_row_top_edge, edge_to_tiles)) == 2:

        row, previous_first_id, next_row_top_edge, next_edge = get_first_tile_of_next_row(previous_first_id, next_row_top_edge, tile_edges, tile_centres, edge_to_tiles)

        row = fill_row(previous_first_id, next_edge, row, tile_edges, tile_centres, edge_to_tiles)

        image = np.vstack((image, row))

    for _ in range(4):
        image = find_monsters(image)
        np.rot90(image)

    image = np.flip(image, 0)

    for _ in range(4):
        image = find_monsters(image)
        np.rot90(image)

    return image.flatten().tolist().count('#')


def extract_tile_maps(input):
    tile_edges = {}
    tile_centres = {}
    for tile in input.split('\n\n'):
        lines = tile.splitlines()
        tile_id = int(lines[0][5:-1])
        right_edge = ''.join([l[-1] for l in lines[1:]])
        left_edge = ''.join([l[0] for l in lines[1:]])
        edges = [lines[1], right_edge, flip_edge(lines[-1]), flip_edge(left_edge)]
        tile_edges[tile_id] = edges
        tile_centres[tile_id] = np.array([[i for i in l[1:-1]] for l in lines[2:-1]])
    return tile_edges, tile_centres


def flip_edge(edge):
    return edge[::-1]


def construct_edge_to_id_map(tile_edges):
    edge_to_tiles = {}

    for tile in tile_edges:
        for edge in tile_edges[tile]:
            e = edge if edge > flip_edge(edge) else flip_edge(edge)
            if e in edge_to_tiles:
                edge_to_tiles[e].append(tile)
            else:
                edge_to_tiles[e] = [tile]

    return edge_to_tiles


def get_tile_ids_for_edge(edge, edge_to_tile_map):
    e = edge if edge > flip_edge(edge) else flip_edge(edge)
    return edge_to_tile_map[e]


def get_first_corner(tile_edges, edge_to_tiles, tile_centres):
    for tile in tile_edges:
        unmatched_edges = []
        for i, edge in enumerate(tile_edges[tile]):
            e = edge if edge > flip_edge(edge) else flip_edge(edge)
            if len(edge_to_tiles[e]) == 1:
                unmatched_edges.append(i)
        if len(unmatched_edges) == 2:
            im = tile_centres[tile]
            orientation = 0
            if unmatched_edges == [0, 1]:
                orientation = 1
            if unmatched_edges == [1, 2]:
                orientation = 2
            if unmatched_edges == [2, 3]:
                orientation = 3
            image = np.rot90(im, orientation)
            next_row_top_edge = tile_edges[tile][(orientation+2) % 4]
            next_edge = tile_edges[tile][(orientation+1) % 4]

            return image, next_row_top_edge, tile, next_edge


def get_first_tile_of_next_row(previous_first_id, next_row_top_edge, tile_edges, tile_centres, edge_to_tiles):
    next_id = next(x for x in get_tile_ids_for_edge(next_row_top_edge, edge_to_tiles) if x != previous_first_id)
    edges = tile_edges[next_id]

    rotation = 0
    flipped = False
    for i in range(4):
        if edges[i] == next_row_top_edge:
            rotation = i
            flipped = True
            break
        if edges[i] == flip_edge(next_row_top_edge):
            rotation = i
            flipped = False
            break

    im = tile_centres[next_id]
    im = np.rot90(im, rotation)
    next_top_edge = edges[(rotation + 2) % 4]
    next_edge = edges[(rotation + 1) % 4]
    if flipped:
        im = np.flip(im, 1)
        next_edge = flip_edge(edges[(rotation - 1) % 4])
        next_top_edge = flip_edge(next_top_edge)

    return im, next_id, next_top_edge, next_edge


def fill_row(previous_id, next_edge, row, tile_edges, tile_centres, edge_to_tiles):
    while len(get_tile_ids_for_edge(next_edge, edge_to_tiles)) == 2:
        next_id = next(x for x in get_tile_ids_for_edge(next_edge, edge_to_tiles) if x != previous_id)
        edges = tile_edges[next_id]

        rotation = 0
        flipped = False
        for i in range(4):
            if edges[i] == next_edge:
                rotation = i
                flipped = True
                break
            if edges[i] == flip_edge(next_edge):
                rotation = i
                flipped = False
                break

        im = tile_centres[next_id]
        im = np.rot90(im, (rotation + 1))
        next_edge = edges[(rotation + 2) % 4]

        if flipped:
            im = np.flip(im, 0)
            next_edge = flip_edge(next_edge)

        row = np.concatenate((row, im), axis=1)
        previous_id = next_id
    return row


def find_monsters(image):
    monster_template = HERE_BE_MONSTERS.splitlines()
    monster_height, monster_width = len(monster_template), len(monster_template[0])
    for y in range(0, image.shape[0] - monster_height - 1):
        for x in range(0, image.shape[1] - monster_width - 1):
            sighting = True
            for j in range(monster_height):
                for i in range(monster_width):
                    if monster_template[j][i] == '#':
                        if image[y + j][x + i] == '.':
                            sighting = False
            if sighting:
                # Mark the spot
                for j in range(monster_height):
                    for i in range(monster_width):
                        if monster_template[j][i] == '#':
                            image[y + j][x + i] = 'O'
    return image


if __name__ == "__main__":
    run_tests(test_cases_b, solve)
    print(solve(puzzle_input))
