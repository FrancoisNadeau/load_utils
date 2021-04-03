#!usr/bin/env/python3

from typing import Sequence
from typing import Union

def filterlist_inc(
    include: Sequence,
    str_lst: Union[list, tuple]
) -> list:
    """
    Returns a tuple of elements including only
    items matching patterns in 'include'
    Parameters
    ----------
    include: patterns susceptible to return a match among items in 'str_lst'
    str_lst: list of items to be filtered
    """
    outlst = [itm for itm in str_lst if any(sub in itm for sub in include)]
    return [sorted(outlst) if sort else outlst][0]

def main():
    if __name__ == __main__:
        filterlist_inc(exclude, str_lst)

