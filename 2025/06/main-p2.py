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

    grid = []
    for line in lines:
        grid.append(line)
    max_len = max(len(row) for row in grid)
    grid = [row.ljust(max_len) for row in grid]
    grid_t = lmap(list, zip(*grid)) # transpose
    sprint(grid)
    sprint(grid_t)
    ops = [v[-1] for v in grid_t if v[-1] != " "]
    grid_t = [v[:-1] for v in grid_t]
    nums = ["".join([c for c in row if c != " "]) for row in grid_t]
    nums_list = [list(g) for is_delim, g in itertools.groupby(nums, lambda v: v == "") if not is_delim]
    total = 0
    for i, prob_nums in enumerate(nums_list):
        if len(prob_nums) > 1:
            total += reduce(lambda acc, val: eval(str(acc) + ops[i] + val), prob_nums)
        else:
            total += int(prob_nums[0])
    print(total)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
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