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


def to_bitboard(l):
    return [reduce(lambda acc, val: ((acc << 1) | int(val == "#")), reversed(row), 0) for row in l]

def print_grid(grid):
    for row in grid:
        print("".join(row))

def do_case(inp: str, sample=False):
    from time import perf_counter_ns
    start = perf_counter_ns()
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    grid = []
    x, y = 0, 0
    for i, line in enumerate(lines):
        grid.append([*line])
        if line.find("^") > -1:
            y = i
            x = line.find("^")
    dirs = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]
    h = len(grid)
    w = len(grid[0])
    d = 0

    g = to_bitboard(grid)
    t = to_bitboard(trans(grid))

    while True:
        x2 = x + dirs[d][0]
        y2 = y + dirs[d][1]
        if g[y2] & (1 << x2):
            sprint((x, y), (x2, y2))
            d = (d + 1) & 3
            if sample:
                print_grid(grid)
        else:
            if d == 0:
                y2 = msb(lmask(t[x], y)) + 1
                if y2 == 0:
                    for i in range(y, -1, -1):
                        grid[i][x] = "X"
                    break
                for i in range(y, y2 - 1, -1):
                    grid[i][x] = "X"
            elif d == 1:
                x2 = lsb(rmask(g[y], w - x - 1, w)) - 1
                if x2 == -2:
                    for i in range(x, w, 1):
                        grid[y][i] = "X"
                    break
                for i in range(x, x2 + 1, 1):
                    grid[y][i] = "X"
            elif d == 2:
                y2 = lsb(rmask(t[x], h - y - 1, h)) - 1
                if y2 == -2:
                    for i in range(y, h, 1):
                        grid[i][x] = "X"
                    break
                for i in range(y, y2 + 1, 1):
                    grid[i][x] = "X"
            elif d == 3:
                x2 = msb(lmask(g[y], x)) + 1
                if x2 == 0:
                    for i in range(x, -1, -1):
                        grid[y][i] = "X"
                    break
                for i in range(x, x2 - 1, -1):
                    grid[y][i] = "X"
            x = x2
            y = y2
    if sample:
        print_grid(grid)
    print(sum(reduce(lambda acc, val: acc + int(val == "X"), row, 0) for row in grid))

    end = perf_counter_ns()
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