import sys;
from platform import machine

sys.dont_write_bytecode = True; from utils import *
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

def push_box(g, x, y, d, c):
    if d == "<":
        match g[y][x - 1]:
            case "#":
                return False
            case "[":
                if push_box(g, x - 1, y, d, "["):
                    g[y][x - 1] = c
                    g[y][x] = "."
                    return True
                else:
                    return False
            case ".":
                g[y][x - 1] = c
                g[y][x] = "."
                return True
    elif d == "v":
        match g[y + 1][x]:
            case "#":
                return False
            case "O":
                if push_box(g, x, y + 1, d, "O"):
                    g[y + 1][x] = c
                    g[y][x] = "."
                    return True
                else:
                    return False
            case ".":
                g[y + 1][x] = c
                g[y][x] = "."
                return True
    elif d == ">":
        match g[y][x + 1]:
            case "#":
                return False
            case "O":
                if push_box(g, x + 1, y, d, "O"):
                    g[y][x + 1] = c
                    g[y][x] = "."
                    return True
                else:
                    return False
            case ".":
                g[y][x + 1] = c
                g[y][x] = "."
                return True
    elif d == "^":
        match g[y - 1][x]:
            case "#":
                return False
            case "O":
                if push_box(g, x, y - 1, d, "O"):
                    g[y - 1][x] = c
                    g[y][x] = "."
                    return True
                else:
                    return False
            case ".":
                g[y - 1][x] = c
                g[y][x] = "."
                return True

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    g = []
    x = -1
    y = -1
    moves = ""
    for i, line in enumerate(lines):
        if line:
            g.append([c for c in line.replace("#", "##").replace("O", "[]").replace(".", "..".replace("@", "@."))])
        else:
            moves = "".join(lines[i+1:])
            break

    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == "@":
                x = j
                y = i
                break
        if x != -1:
            break

    move_change = {
        "<": (-1, 0),
        "v": (0, 1),
        ">": (1, 0),
        "^": (0, -1),
    }

    for m in moves:
        if push_box(g, x, y, m, "@"):
            x += move_change[m][0]
            y += move_change[m][1]

    result = 0
    for i, row in enumerate(g):
        j = -1
        while "O" in row[j + 1:]:
            j = row.index("O", j + 1)
            result += 100 * i + j

    print(result)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
""",r"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
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