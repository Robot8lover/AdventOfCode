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

def do_case(inp: str, sample=False):
    # READ THE PROBLEM FROM TOP TO BOTTOM OK
    def sprint(*a, **k): sample and print(*a, **k)
    lines = inp.splitlines()

    tiles = []
    for line in lines:
        tiles.append([int(v) for v in line.split(",")])
    area = 0
    for i, pos in enumerate(tiles):
        for pos2 in tiles[:i]:
            temp_area = (abs(pos[0] - pos2[0]) + 1) * (abs(pos[1] - pos2[1]) + 1)
            if temp_area > area:
                area = temp_area
    print(area)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
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