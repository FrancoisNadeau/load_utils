#!usr/bin/env/python3

from typing import Sequence

def filterlist_exc(
    exclude: Sequence,
    lst: Sequence
) -> list:
    """
    Returns a tuple of elements excluding all items
    matching patterns in 'exclude'
    ------------------------------
    Parameters
    ----------
    exclude: patterns susceptible to return a match among items in 'lst'
    lst: list of items to be filtered
    """
    return [itm for itm in lst if all(sub not in itm for sub in exclude)]

def main():
    if __name__ == __main__:
        filterlist_exc(exclude, lst)
