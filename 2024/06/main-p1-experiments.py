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

def do_case(inp: str, sample=False):
    from time import perf_counter_ns as pcns
    start = pcns()
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
    opath = []
    opath.append((x, y, d))

    t = trans(grid)
    while True:
        x2 = x + dirs[d][0]
        y2 = y + dirs[d][1]
        if grid[y2][x2] == "#":
            d = (d + 1) % 4
        else:
            if d == 0:
                if "#" in t[x][:y:1]:
                    y2 = last_index(t[x], "#", y - 1) + 1
                    for i in range(y, y2 - 1, -1):
                        opath.append((x, i, d))
                else:
                    for i in range(y, -1, -1):
                        opath.append((x, i, d))
                    break
            elif d == 1:
                if "#" in grid[y][:x:-1]:
                    x2 = grid[y].index("#", x + 1) - 1
                    for i in range(x, x2 + 1, 1):
                        opath.append((i, y, d))
                else:
                    for i in range(x, w, 1):
                        opath.append((i, y, d))
                    break
            elif d == 2:
                if "#" in t[x][:y:-1]:
                    y2 = t[x].index("#", y + 1) - 1
                    for i in range(y, y2 + 1, 1):
                        opath.append((x, i, d))
                else:
                    for i in range(y, h, 1):
                        opath.append((x, i, d))
                    break
            elif d == 3:
                if "#" in grid[y][:x:1]:
                    x2 = last_index(grid[y], "#", x - 1) + 1
                    for i in range(x, x2 - 1, -1):
                        opath.append((i, y, d))
                else:
                    for i in range(x, -1, -1):
                        opath.append((i, y, d))
                    break
            x = x2
            y = y2
        c = (x, y, d)
        opath.append(c)

    oset = set([(x, y) for x, y, _ in opath])
    for x, y in oset:
        grid[y][x] = "X"
    for row in grid:
        sprint("".join(row))
    print(len(oset))

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