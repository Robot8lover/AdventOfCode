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

    V = len(lines) + 1
    adj = [[] for _ in range(V)]
    key_to_index = {}
    key_to_index["out"] = V - 1
    for i, line in enumerate(lines):
        key_to_index[line[:line.index(":")]] = i
    for line in lines:
        index = key_to_index[line[:line.index(":")]]
        adj[index] = [key_to_index[v] for v in line[line.index(":")+2:].split()]
    
    rev_adj = [[] for _ in range(V)]
    for i, l in enumerate(adj):
        for j in l:
            rev_adj[j].append(i)

    # Now we want to do a dfs and count things yk

    @functools.cache
    def count_paths(start, end, exclude=[]):
        if start == end:
            return 1
        return sum(count_paths(start, next_vertex) for next_vertex in rev_adj[end] if next_vertex not in exclude)

    svr_dac_fft_out_paths = (count_paths(key_to_index["svr"], key_to_index["dac"], (key_to_index["fft"],))
                              * count_paths(key_to_index["dac"], key_to_index["fft"], (key_to_index["dac"],))
                              * count_paths(key_to_index["fft"], key_to_index["out"], (key_to_index["dac"],)))
    svr_fft_dac_out_paths = (count_paths(key_to_index["svr"], key_to_index["fft"], (key_to_index["dac"],))
                              * count_paths(key_to_index["fft"], key_to_index["dac"], (key_to_index["fft"],))
                              * count_paths(key_to_index["dac"], key_to_index["out"], (key_to_index["fft"],)))
    print(svr_dac_fft_out_paths + svr_fft_dac_out_paths)

    # you actually don't need the exclusions, and one is guaranteed 0 since acyclic

    return # DOES NOTHING, PRINT INSTEAD

run_samples_and_actual([
# Part 1
r"""
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case) # day and year can be added as arguments if not doing today