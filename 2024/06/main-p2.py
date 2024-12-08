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
        grid.append(line)
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
    def conv(a, b):
        return a * w + b
    for i in range(h):
        for j in range(w):
            if grid[i][j] == "#" or grid[i][j] == "^":
                continue
            assert(grid[i][j] == ".")
            grid[i] = grid[i][:j] + "#" + grid[i][j+1:]
            x = ox
            y = oy
            d = 0
            pos = {}
            pos[conv(x, y)] = [d]
            stuck = False
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
                    c = conv(x, y)
                    if c not in pos:
                        pos[c] = []
                    elif d in pos[c]:
                        stuck = True
                        break
                    pos[c].append(d)
            if stuck:
                result += 1
            grid[i] = grid[i][:j] + "." + grid[i][j+1:]
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