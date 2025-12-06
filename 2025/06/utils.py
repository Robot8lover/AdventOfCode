# region Imports
import collections
import copy
import functools
import itertools
import math
import operator
import re
import sys
import typing
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from pprint import pprint

# endregion

sys.setrecursionlimit(100000)


# Copy a function if you need to modify it.

# region numbers
def bool2sign(boolean):
    return 1 if boolean else -1

# endregion

# region Strings, lists, dicts
def lmap(func, *iterables):
    return list(map(func, *iterables))

def min_max(l):
    return min(l), max(l)

def max_minus_min(l):
    return max(l) - min(l)

# endregion

# region Algorithms
def bisect(f, lo=0, hi=None, eps=1e-9):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Assert that f(lo) != f(hi).
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo + offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    while hi - lo > eps:
        mid = (hi + lo) / 2
        if f(mid) == lo_bool:
            lo = mid
        else:
            hi = mid
    if lo_bool:
        return lo
    else:
        return hi


def binary_search(f, lo=0, hi=None):
    """
    Returns a value x such that f(x) is true.
    Based on the values of f at lo and hi.
    Assert that f(lo) != f(hi).
    """
    lo_bool = f(lo)
    if hi is None:
        offset = 1
        while f(lo + offset) == lo_bool:
            offset *= 2
        hi = lo + offset
    else:
        assert f(hi) != lo_bool
    best_so_far = lo if lo_bool else hi
    while lo <= hi:
        mid = (hi + lo) // 2
        result = f(mid)
        if result:
            best_so_far = mid
        if result == lo_bool:
            lo = mid + 1
        else:
            hi = mid - 1
    return best_so_far


# Distances
BLANK = object()

# endregion

# region Data Structures
T = typing.TypeVar("T")

# endregion

# region List/Vector operations
# endregion

# region Matrices

# endregion

# region Previous problems

# endregion


# region Running
def parse_samples(l):
    samples = lmap(str.strip, l)
    while samples and not samples[-1]: samples.pop()
    return samples

def get_actual(day=None, year=None):
    try:
        actual_input = open("input.txt").read()
        return actual_input
    except FileNotFoundError:
        pass
    from pathlib import Path
    # let's try grabbing it
    search_path = Path("").resolve()
    try:
        if day is None:
            day = int(search_path.name.lstrip("0"))
        if year is None:
            year = int(search_path.parent.name)
    except ValueError:
        print("Can't get day and year.")
        print("Backup: save 'input.txt' into the same folder as this script.")
        return ""

    print("{} day {} input not found.".format(year, day))

    # is it time?
    from datetime import datetime, timezone, timedelta
    est = timezone(timedelta(hours=-5))
    unlock_time = datetime(year, 12, day, tzinfo=est)
    cur_time = datetime.now(tz=est)
    delta = unlock_time - cur_time
    if delta.days >= 0:
        print("Remaining time until unlock: {}".format(delta))
        return ""

    while (not list(search_path.glob("*/token.txt"))) and search_path.parent != search_path:
        search_path = search_path.parent

    token_files = list(search_path.glob("*/token.txt"))
    if not token_files:
        assert search_path.parent == search_path
        print("Can't find token.txt in a parent directory.")
        print("Backup: save 'input.txt' into the same folder as this script.")
        return ""

    with token_files[0].open() as f:
        token = f.read().strip()

    # importing requests takes a long time...
    # let's do it without requests.
    import urllib.request
    import urllib.error
    import shutil
    opener = urllib.request.build_opener()
    opener.addheaders = [("Cookie", "session={}".format(token)), ("User-Agent", "python-requests/2.19.1")]
    print("Sending request...")
    url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
    try:
        with opener.open(url) as r:
            with open("input.txt", "wb") as f:
                shutil.copyfileobj(r, f)
            print("Input saved!")
            return open("input.txt").read()
    except urllib.error.HTTPError as e:
        status_code = e.getcode()
        if status_code == 400:
            print("Auth failed!")
        elif status_code == 404:
            print("Day is not out yet????")
        else:
            print("Request failed with code {}??".format(status_code))
        return ""


def run_samples_and_actual(part1, part2, do_case, day=None, year=None):
    p1 = parse_samples(part1)
    p2 = parse_samples(part2)
    for sample in p2 or p1:
        print("running {}:".format(repr(sample)[:100]))
        print("-" * 10)
        do_case(sample, True)
        print("-" * 10)
        print("#" * 10)

    actual_input = get_actual(day, year).strip()

    if actual_input:
        print("!! running actual: !!")
        print("-" * 10)
        do_case(actual_input, False)
        print("-" * 10)
# endregion
