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

class UnionFind:
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]
        self.size = [1] * N
    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            # self.size[j] <= self.size[i]
            self.id[j] = i
            self.size[i] += self.size[j]
        self.count -= 1
    def find(self, p):
        while (p != self.id[p]):
            p = self.id[p]
        return p
    def connected(self, p, q):
        return self.find(p) == self.find(q)

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    boxes = []
    for line in lines:
        x, y, z = [int(v) for v in line.split(",")]
        boxes.append((x, y, z))
    dists = []
    for i, box in enumerate(boxes):
        for j, box2 in enumerate(boxes[:i]):
            dists.append((math.dist(box, box2),(i,j)))
    dists.sort(key=lambda v: v[0])
    N = len(boxes)
    uf = UnionFind(N)
    connections = 10 if sample else 1000
    for i in range(connections):
        uf.union(*dists[i][1])
    root_sizes = []
    for i in range(N):
        if uf.id[i] == i:
            root_sizes.append(uf.size[i])
    assert len(root_sizes) == uf.count
    root_sizes.sort(reverse=True)
    print(root_sizes[0] * root_sizes[1] * root_sizes[2])

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
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