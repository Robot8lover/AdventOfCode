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

    result = 0
    for line in lines:
        disk = []
        files = 0
        for i, c in enumerate(line):
            n = int(c)
            if i & 1:
                # empty
                disk.extend([None] * n)
            else:
                # file
                disk.extend([i // 2] * n)
                files += n

        disk.append(None)

        i = len(disk) - 1
        j = 0
        while disk.index(None) < files:
            while disk[i] is None:
                i -= 1
            while disk[j] is not None:
                j += 1
            disk[j] = disk[i]
            disk[i] = None
        sprint(disk)

        for i, id_num in enumerate(disk):
            if id_num is None:
                break
            else:
                result += i * id_num

    print(result)


    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
2333133121414131402
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