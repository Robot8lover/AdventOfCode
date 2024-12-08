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
    ox = x
    oy = y
    result = 0
    d = 0
    opath = []
    opath.append((x, y, d))
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
            opath.append((x, y, d))

    print(len(set([(x, y) for x, y, _ in opath])))

    opath.append((ox, oy, 0))

    done = set()
    for ind, (j, i, _) in enumerate(opath[:-1]):
        if grid[i][j] != "." or (j, i) in done:
            continue
        done.add((j, i))
        grid[i][j] = "#"
        x, y, d = opath[ind - 1]
        pos = set(opath[:ind])
        stuck = False
        while True:
            x2 = x + dirs[d][0]
            y2 = y + dirs[d][1]
            if x2 < 0 or x2 >= w or y2 < 0 or y2 >= h:
                break
            elif grid[y2][x2] == "#":
                d = (d + 1) & 3
            else:
                x = x2
                y = y2
                c = (x, y, d)
                if c in pos:
                    stuck = True
                    break
                pos.add(c)
        if stuck:
            result += 1
        grid[i][j] = "."
    print(result)

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