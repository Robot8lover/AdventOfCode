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

def perim_right(plot, y, y_lim):
    result = y_lim - y
    right = last_index(plot[y], True)
    for j in range(y + 1, y_lim):
        next_right = last_index(plot[j], True)
        result += abs(next_right - right)
        right = next_right
    return result

def top_bot(plot, y, y_lim):
    return ((last_index(plot[y], True) - plot[y].index(True) + 1)
            + (last_index(plot[y_lim - 1], True) - plot[y_lim - 1].index(True)) + 1)

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    g = []
    for line in lines:
        g.append([c for c in line])
    height = len(g)
    width = len(g[0])
    blank = [[False] * width for _ in range(height)]

    result = 0
    for y in range(height):
        for x in range(width):
            c = g[y][x]
            if c == ".":
                continue
            plot = copy.deepcopy(blank)
            r = y
            first = x
            while True:
                right = width - 1
                for i in range(first, width):
                    if g[r][i] == c:
                        plot[r][i] = True
                        g[r][i] = "."
                    else:
                        right = i - 1
                        break
                if r + 1 == height:
                    r += 1
                    break
                first = -1
                for i in range(right, x - 1, -1):
                    if g[r + 1][i] == c:
                        first = i
                    elif first != -1:
                        break
                r = r + 1
                if first == -1:
                    break
                else:
                    for i in range(first, -1, -1):
                        if g[r][i] == c:
                            first = i
                        else:
                            break
            y_lim = r
            area = sum(sum(row) for row in plot)
            sprint(plot)
            sprint(y, y_lim)
            sprint(plot[::-1])
            perimeter = perim_right(plot, y, y_lim) + perim_right(plot[::-1], height - y_lim, height - y) + top_bot(plot, y, y_lim)
            sprint(perimeter)
            result += area * perimeter

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

"""], do_case) # day and year can be added as arguments if not doing today