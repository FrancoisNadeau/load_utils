#!usr/bin/env/python3

import pandas as pd
from functools import reduce

def megamerge(dflist: list, howto: str = "outer", onto: str = None) -> object:
    """ Returns a pd.DataFrame made from merging the frames in 'dflist' """
    return reduce(lambda x, y: pd.merge(
        x, y, on=onto, how=howto).astype("object"), dflist)

def main():
    if __name__ == __main__:
        megamerge(dflist, howto, onto)

