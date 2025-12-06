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

    in_ranges = True
    # fresh_set = set()
    fresh_ranges = []
    count = 0
    for line in lines:
        if in_ranges:
            if not line:
                in_ranges = False
            else:
                start, end = lmap(int, line.split("-"))
                # fresh_set |= set(range(start, end+1))
                fresh_ranges.append(range(start, end+1))
        else:
            ingredient_id = int(line)
            for r in fresh_ranges:
                if ingredient_id in r:
                    count += 1
                    break
            # if ingredient_id in fresh_set:
                # count += 1
    print(count)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
3-5
10-14
16-20
12-18

1
5
8
11
17
32
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