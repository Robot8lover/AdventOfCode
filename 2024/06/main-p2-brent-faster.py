import sys; sys.dont_write_bytecode = True; from utils import *
"""
To do: ensure Code Runner works, have preloaded the day and input in Chrome,
saved input into the folder, have utils on the side, collapse regions

Strings, lists, dicts:
lmap, ints, positive_ints, floats, positive_floats, words, keyvalues

Algorithms:
bisect, binary_search, hamming_distance, edit_distance

Data structures:
Linked, UnionFind
use deque for queue: q[0], q.append and q.popleft

List/Vector operations:
GRID_DELTA, OCT_DELTA
lget, lset, fst, snd
padd, pneg, psub, pmul, pdot, pdist1, pdist2sq, pdist2

Matrices:
matmat, matvec, matexp

Previous problems:
knot

Dict things:
dict.keys()
dict.values()
dict.items()
"""

dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0),
]

def state(x, y, d, h, w):
    return d * h * w + y * w + x

def advance(x, y, d, h, w, grid):
    x2 = x + dirs[d][0]
    y2 = y + dirs[d][1]
    if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
        return -1, -1, -1
    elif grid[y2][x2] == "#":
        d = (d + 1) % 4
        return x, y, d
    else:
        return x2, y2, d

def do_case(inp: str, sample=False):
    from time import perf_counter_ns as pcns
    start = pcns()
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    grid = []
    x, y = 0, 0
    for i, line in enumerate(lines):
        grid.append([c for c in line])
        if line.find("^") > -1:
            y = i
            x = line.find("^")

    h = len(grid)
    w = len(grid[0])
    ox = x
    oy = y

    d = 0

    pos = set()
    pos.add((x, y))
    while True:
        x2 = x + dirs[d][0]
        y2 = y + dirs[d][1]
        if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
            break
        elif grid[y2][x2] == "#":
            d = (d + 1) % 4
        else:
            x = x2
            y = y2
            pos.add((x, y))

    x = ox
    y = oy
    d = 0

    result = 0
    esc = (-1, -1, -1)
    for j, i in pos:
        if grid[i][j] != ".":
            continue
        grid[i][j] = "#"
        x = ox
        y = oy
        d = 0
        lam = 1
        power = lam
        tort = (x, y, d)
        hare = advance(x, y, d, h, w, grid) # hopefully not an end oh well
        stuck = False
        while True:
            if power == lam:
                tort = hare
                power *= 2
                lam = 0
            hare = advance(*hare, h, w, grid)
            lam += 1
            if hare == esc:
                break
            if tort == hare:
                stuck = True
                break
        if stuck:
            result += 1
        grid[i][j] = "."
    print(result)

    end = pcns()
    print(f"Took {(end - start) / 1e6} ms")

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
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