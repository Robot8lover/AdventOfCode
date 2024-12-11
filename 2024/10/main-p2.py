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

def rating(x, y, g, weight):
    if g[y][x] != weight:
        return 0
    elif weight == 9:
        return 1
    result = 0
    if x > 0:
        result += rating(x - 1, y, g, weight + 1)
    if y > 0:
        result += rating(x, y - 1, g, weight + 1)
    if x < len(g[0]) - 1:
        result += rating(x + 1, y, g, weight + 1)
    if y < len(g) - 1:
        result += rating(x, y + 1, g, weight + 1)
    return result

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    g = []
    for line in lines:
        g.append([])
        for c in line:
            g[-1].append(int(c))

    heads = []
    for i, row in enumerate(g):
        for j, val in enumerate(row):
            if val == 0:
                heads.append((j, i))

    result = 0
    for x, y in heads:
        s = rating(x, y, g, 0)
        result += s
    print(result)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
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