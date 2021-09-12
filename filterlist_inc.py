#!usr/bin/env/python3
from typing import Sequence
def filterlist_inc(
    include: Sequence,
    lst: Sequence
) -> list:
    """
    Returns a tuple of elements including only
    items matching patterns in 'include'
    Parameters
    ----------
    include: patterns susceptible to return a match among items in 'lst'
    lst: list of items to be filtered
    """
    return [itm for itm in lst if any(sub in itm for sub in include)]

def main():
    if __name__ == __main__:
        filterlist_inc(exclude, lst)
