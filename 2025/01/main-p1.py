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

    dial = 50
    count = 0
    for line in lines:
        direction = line[0] == "R" # True if R, False if L
        amount = int(line[1:])
        dir_sign = bool2sign(direction)

        dial = (dial + dir_sign * amount) % 100 # python, so sign matches that of modulus (positive)
        if dial == 0:
            count += 1
    print(count)

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
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