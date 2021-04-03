from collections.abc import Iterable
from typing import Sequence
from typing import Union

def flatten(
    nested_seq: Union[Iterable, Sequence]
) -> list:
    """Returns unidimensional list from nested list using list comprehension.
    ----------
    Parameters
    ----------
        nestedlst: list containing other lists etc.
    ---------
    Variables
    ---------
        bottomElem: type = str
        sublist: type = list
    ------
    Return
    ------
    flatlst: unidimensional list"""
    return [
        bottomElem
        for sublist in nested_seq
        for bottomElem in (
            flatten(sublist)
            if (isinstance(sublist, Sequence) and \
                not isinstance(sublist, str))
            else [sublist]
        )
    ]

def main():
    if __name__ == __main__:
        flatten(nested_seq)
