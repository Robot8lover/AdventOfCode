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

class UnionPlots:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [1] * n
        self.count = n
        self.perimeters = [0] * n

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p != self.parents[p]:
            p = self.parents[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        if self.ranks[i] < self.ranks[j]:
            self.parents[i] = j
            self.ranks[j] += self.ranks[i]
            self.perimeters[j] += self.perimeters[i]
        else:
            self.parents[j] = i
            self.ranks[i] += self.ranks[j]
            self.perimeters[i] += self.perimeters[j]
        self.count -= 1

    def update_perimeter(self, p, perimeter):
        self.perimeters[self.find(p)] += perimeter

def conv2sing(x, y, width, height):
    return y * width + x

def conv2pair(n, width, height):
    return divmod(n, width)[::-1]

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    g = []
    for line in lines:
        g.append([c for c in line])
    height = len(g)
    width = len(g[0])

    g_old = g
    g = ([["." for _ in range(width + 2)]]
         + [(["."] + row + ["."]) for row in g_old]
         + [["." for _ in range(height + 2)]])

    # adj = (-width, 1, width, -1)
    adj = (
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    )
    up = UnionPlots(width * height)
    fences = [[] for _ in range(width * height)]
    for y, row in enumerate(g):
        for x, c in enumerate(row):
            if c == ".":
                continue
            c2s = conv2sing(x - 1, y - 1, width, height)
            perimeter = 0
            for adj_ind, (dx, dy) in enumerate(adj):
                x2 = x + dx
                y2 = y + dy
                if g[y2][x2] == c:
                    # no need for bound check due to padding
                    up.union(c2s, conv2sing(x2 - 1, y2 - 1, width, height))
                else:
                    match adj_ind:
                        case 0:
                            # up
                            fences[c2s].append(0)
                            if not(g[y][x - 1] == c and 0 in fences[conv2sing(x - 2, y - 1, width, height)]):
                                # sprint((x - 1, y - 1), (x2 - 1, y2 - 1), adj_ind)
                                perimeter += 1
                        case 1:
                            # right
                            fences[c2s].append(1)
                            if not (g[y - 1][x] == c and 1 in fences[conv2sing(x - 1, y - 2, width, height)]):
                                # sprint((x - 1, y - 1), (x2 - 1, y2 - 1), adj_ind)
                                perimeter += 1
                        case 2:
                            # down
                            fences[c2s].append(2)
                            if not(g[y][x - 1] == c and 2 in fences[conv2sing(x - 2, y - 1, width, height)]):
                                # sprint((x - 1, y - 1), (x2 - 1, y2 - 1), adj_ind)
                                perimeter += 1
                        case 3:
                            # left
                            fences[c2s].append(3)
                            if not (g[y - 1][x] == c and 3 in fences[conv2sing(x - 1, y - 2, width, height)]):
                                # sprint((x - 1, y - 1), (x2 - 1, y2 - 1), adj_ind)
                                perimeter += 1
            up.update_perimeter(c2s, perimeter)

    # sprint(fences)

    result = 0
    for i in range(width * height):
        if up.parents[i] == i:
            # sprint(conv2pair(i, width, height), up.ranks[i], up.perimeters[i])
            result += up.ranks[i] * up.perimeters[i]

    print(result)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
AAAA
BBCD
BBCC
EEEC
""",r"""
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
""",r"""
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
""",r"""
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
""",r"""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
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

"""], do_case) # day and year can be added as arguments if not doing toda