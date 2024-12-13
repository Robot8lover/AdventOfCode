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

import numpy as np

def solve(ax, ay, bx, by, px, py):
    # a * ax + b * bx = px
    # a * ay + b * by = py

    # by * a * ax + by * b * bx = by * px
    # bx * a * ay + bx * b * by = bx * py

    # (by * ax - bx * ay) * a = by * px - bx * py
    num_a = by * px - bx * py
    den_a = by * ax - bx * ay
    if num_a % den_a:
        return None
    else:
        a = num_a // den_a
        num_b = px - a * ax
        den_b = bx
        if num_b % den_b:
            return None
        else:
            b = num_b // den_b
            return a, b

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()
    lines.append([])

    # 3 for A, 1 for B

    result = 0
    for i in range(len(lines) // 4):
        ax, ay = ints(lines[4 * i])
        bx, by = ints(lines[4 * i + 1])
        px, py = ints(lines[4 * i + 2])

        """
        a * ax + b * bx = px
        a * ay + b * by = py
        """

        s = solve(ax, ay, bx, by, px, py)
        if s is not None:
            a, b = s
            if a > 100 or b > 100:
                # never comes up
                print(a, b)
                pass
            else:
                result += 3 * a + b
    print(result)


    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
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