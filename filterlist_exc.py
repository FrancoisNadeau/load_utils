#!usr/bin/env/python3

from typing import Sequence
from typing import Union

def filterlist_exc(
    exclude: Sequence,
    str_lst: Union[list, tuple]
) -> list:
    """
    Returns a tuple of elements excluding all items
    matching patterns in 'exclude'
    ------------------------------
    Parameters
    ----------
    exclude: patterns susceptible to return a match among items in 'str_lst'
    str_lst: list of items to be filtered
    """
    return [itm for itm in str_lst if all(sub not in itm for sub in exclude)]

def main():
    if __name__ == __main__:
        filterlist_exc(exclude, str_lst)

