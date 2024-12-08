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
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    g = []
    for line in lines:
        g.append([])
        for c in line:
            g[-1].append(c)
    t = trans(g)

    w = len(g)
    h = len(t)

    chars = {}
    for y, row in enumerate(g):
        for x, c in enumerate(row):
            if c == ".": continue
            if c not in chars:
                chars[c] = []
            chars[c].append((x, y))

    points = set()
    for c, ps in chars.items():
        l = len(ps)
        for i in range(l):
            for j in range(i + 1, l):
                x1, y1 = ps[i]
                x2, y2 = ps[j]
                dx = x1 - x2
                dy = y1 - y2
                p1x = x1 + dx
                p1y = y1 + dy
                p2x = x2 - dx
                p2y = y2 - dy
                if 0 <= p1x < w and 0 <= p1y < h:
                    points.add((p1x, p1y))
                if 0 <= p2x < w and 0 <= p2y < h:
                    points.add((p2x, p2y))

    print(len(points))

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
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