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

    sub = ""
    off = False
    total = 0
    for v in inp:
        if "don't()".find(sub + v) == 0:
            sub = sub + v
            if sub == "don't()":
                off = True
                sub = ""
        elif "do()".find(sub + v) == 0:
            sub = sub + v
            if sub == "do()":
                off = False
                sub = ""
        elif "mul(".find(sub + v) == 0 or re.match(r"^mul\(\d+,?(\d+)?$", sub + v):
            sub = sub + v
        elif re.match(r"^mul\(\d+,\d+\)$", sub + v):
            sub = sub + v
            if not off:
                x, y = ints(sub)
                total += x * y
            sub = ""
        else:
            sub = ""

    print(total)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case) # day and year can be added as arguments if not doing today