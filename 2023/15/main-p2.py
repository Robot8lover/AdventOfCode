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
    lines = inp.split(",")

    boxes = [([],[]) for _ in range(256)]
    for line in lines:
        ind = max(line.find("="), line.find("-"))
        label = line[:ind]
        h = 0
        for c in label:
            h += ord(c)
            h *= 17
            h %= 256
        op = line[ind]
        if op == "-":
            if label in boxes[h][0]:
                i = boxes[h][0].index(label)
                boxes[h][0].pop(i)
                boxes[h][1].pop(i)
        else:
            fl = int(line[ind+1:])
            if label in boxes[h][0]:
                i = boxes[h][0].index(label)
                boxes[h][1][i] = fl
            else:
                boxes[h][0].append(label)
                boxes[h][1].append(fl)
        # sprint(boxes[0])
        # sprint(boxes[1])
        # sprint(boxes[3])
        # sprint()

    total = 0
    for bn, box in enumerate(boxes):
        for ln, fl in enumerate(box[1]):
            total += (bn + 1) * (ln + 1) * fl
    print(total)


    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
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


# 18 minutes