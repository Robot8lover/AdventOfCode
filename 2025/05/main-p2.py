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

    # fresh_set = set()
    fresh_ranges = []
    for line in lines:
        if not line:
            break
        else:
            start, end = lmap(int, line.split("-"))
            # fresh_set |= set(range(start, end+1))
            fresh_ranges.append([start, end])
    # fresh_ranges.sort(key=lambda v: v[1])
    fresh_ranges.sort(key=lambda v: v[0])
    sprint(fresh_ranges)
    final_ranges = []
    i = 0
    l, r = fresh_ranges[0]
    for nl, nr in fresh_ranges[1:]:
        if nl <= r:
            # overlap
            # sorting means that l < nl
            r = max(r, nr)
        elif nl > r:
            # past right side
            final_ranges.append((l, r))
            l, r = nl, nr
    final_ranges.append((l, r))
    sprint(final_ranges)
    print(sum(r - l + 1 for l, r in final_ranges))

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