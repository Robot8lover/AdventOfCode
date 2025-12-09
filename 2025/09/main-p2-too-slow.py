import sys; sys.dont_write_bytecode = True; from utils import *
"""
To do: ensure Code Runner works, have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions

Strings, lists, dicts:
lmap, min_max, max_minus_min

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:

List/Vector operations:

Matrices:

Previous problems:

Dict things:
dict.keys()
dict.values()
dict.items()
"""

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    tiles = []
    for line in lines:
        tiles.append([int(v) for v in line.split(",")])
    min_x, max_x = min_max([v[0] for v in tiles])
    min_y, max_y = min_max([v[1] for v in tiles])
    for tile in tiles:
        tile[0] -= min_x
        tile[1] -= min_y
    print("done normalizing", flush=True)
    max_x -= min_x
    max_y -= min_y
    print(max_x, max_y, flush=True)
    walls = [[False] * (max_x+1) for _ in range(max_y+1)]
    grid = [[False] * (max_x+1) for _ in range(max_y+1)]
    print("done setting up", flush=True)
    for i in range(-1, len(lines)-1):
        p1 = tiles[i]
        p2 = tiles[i+1]
        start_x, end_x = min_max((p1[0], p2[0]))
        start_y, end_y = min_max((p1[1], p2[1]))
        if start_x == end_x:
            for row_index in range(start_y, end_y+1):
                walls[row_index][start_x] = True
                grid[row_index][start_x] = True
        else:
            # start_y == end_y by guarantee
            for col_index in range(start_x, end_x+1):
                walls[start_y][col_index] = True
                grid[start_y][col_index] = True
    print("done finding walls", flush=True)
    for row_index in range(min(v[1] for v in tiles), max_y+1):
        inside = False
        wall_row = walls[row_index]
        grid_row = grid[row_index]
        on_wall = False
        for col_index in range(max_x+1):
            if wall_row[col_index]:
                if not on_wall:
                    inside = not inside
                    on_wall = True
            else:
                on_wall = False
                if inside:
                    grid_row[col_index] = True
    # if sample:
    #     for row in walls:
    #         print([("X" if v else ".") for v in row])
    #     print()
    #     for row in grid:
    #         print([("X" if v else ".") for v in row])
    print("done filling", flush=True)
    area = 0
    for i, p in enumerate(tiles):
        for p2 in tiles[:i]:
            start_x, end_x = min_max((p[0], p2[0]))
            start_y, end_y = min_max((p[1], p2[1]))
            temp_area = (abs(p[0] - p2[0]) + 1) * (abs(p[1] - p2[1]) + 1)
            if temp_area > area:
                filled = True
                for row in grid[start_y:end_y+1]:
                    for space in row[start_x:end_x+1]:
                        if not space:
                            filled = False
                            break
                    if not filled:
                        break
                if filled:
                    area = temp_area
    print(area)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case) # day and year can be added as arguments if not doing today