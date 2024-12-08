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

    choice = True # probably better but hard to tell
    if choice:
        g = to_bitboard(grid)
        t = to_bitboard(trans(grid))
        while True:
            x2 = x + dirs[d][0]
            y2 = y + dirs[d][1]
            if g[y2] & (1 << x2):
                d = (d + 1) & 3
            else:
                if d == 0:
                    y2 = msb(lmask(t[x], y)) + 1
                    if y2 == 0:
                        for i in range(y, -1, -1):
                            opath.append((x, i, d))
                        break
                    for i in range(y, y2 - 1, -1):
                        opath.append((x, i, d))
                elif d == 1:
                    x2 = lsb(rmask(g[y], w - x - 1, w)) - 1
                    if x2 == -2:
                        for i in range(x, w, 1):
                            opath.append((i, y, d))
                        break
                    for i in range(x, x2 + 1, 1):
                        opath.append((i, y, d))
                elif d == 2:
                    y2 = lsb(rmask(t[x], h - y - 1, h)) - 1
                    if y2 == -2:
                        for i in range(y, h, 1):
                            opath.append((x, i, d))
                        break
                    for i in range(y, y2 + 1, 1):
                        opath.append((x, i, d))
                elif d == 3:
                    x2 = msb(lmask(g[y], x)) + 1
                    if x2 == 0:
                        for i in range(x, -1, -1):
                            opath.append((i, y, d))
                        break
                    for i in range(x, x2 - 1, -1):
                        opath.append((i, y, d))
                x = x2
                y = y2
    else:
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

    g = to_bitboard(grid)
    t = to_bitboard(trans(grid))

    done = set()
    for ind, (j, i, _) in enumerate(opath[:-1]):
        if grid[i][j] != "." or (j, i) in done:
            continue
        done.add((j, i))
        g[i] ^= (1 << j)
        t[j] ^= (1 << i)
        x, y, d = opath[ind - 1]
        pos = set(opath[:ind])
        stuck = False
        while True:
            x2 = x + dirs[d][0]
            y2 = y + dirs[d][1]
            if g[y2] & (1 << x2):
                d = (d + 1) & 3
            else:
                # match here had one really fast run but otherwise seems slower?
                # match should generally be better but who knows and background
                # since things were taking 10 times as long with certain processes running
                if d == 0:
                    y2 = msb(lmask(t[x], y)) + 1
                    if y2 == 0:
                        break
                elif d == 1:
                    x2 = lsb(rmask(g[y], w - x - 1, w)) - 1
                    if x2 == -2:
                        break
                elif d == 2:
                    y2 = lsb(rmask(t[x], h - y - 1, h)) - 1
                    if y2 == -2:
                        break
                elif d == 3:
                    x2 = msb(lmask(g[y], x)) + 1
                    if x2 == 0:
                        break
                x = x2
                y = y2
            c = (x, y, d)
            if c in pos:
                stuck = True
                break
            pos.add(c)
        if stuck:
            result += 1
        g[i] ^= (1 << j)
        t[j] ^= (1 << i)
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