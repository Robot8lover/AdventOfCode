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

    grid = []

    for i, line in enumerate(lines):
        grid.append([])
        for c in line:
            grid[i].append(c)

    count = 0
    # for row in grid:
    #     word = ""
    #     for c in row:
    #         if "XMAS".find(word + c) == 0:
    #             word += c
    #             if word == "XMAS":
    #                 count += 1
    #         else:
    #             word = ""

    height = len(grid)
    width = len(grid[0])
    # for i in range(width):
    #     word = ""
    #     for j in range(height):
    #         c = grid[j][i]
    #         if "XMAS".find(word + c) == 0:
    #             word += c
    #             if word == "XMAS":
    #                 word = "S"
    #                 count += 1
    #         elif "SAMX".find(word + c) == 0:
    #             word += c
    #             if word == "SAMX":
    #                 word = "X"
    #                 count += 1
    #         else:
    #             word = ""

    for x in range(width):
        for y in range(0, height):
            if x < width - 3:
                word = ""
                for i in range(4):
                    word += grid[y][x + i]
                if word == "XMAS" or word == "SAMX":
                    count += 1
            if y < height - 3:
                word = ""
                for i in range(4):
                    word += grid[y + i][x]
                if word == "XMAS" or word == "SAMX":
                    count += 1
                word = ""
                if x < width - 3:
                    for i in range(4):
                        word += grid[y + i][x + i]
                    if word == "XMAS" or word == "SAMX":
                        count += 1
            if y >= 3 and x < width - 3:
                word = ""
                for i in range(4):
                    word += grid[y - i][x + i]
                if word == "XMAS" or word == "SAMX":
                    count += 1
    print(count)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""",r"""
..X...
.SAMX.
.A..A.
XMAS.S
.X....
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