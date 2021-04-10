#!usr/bin/env/python3

import os
from typing import Union
import pandas as pd
from os.path import basename as bname
from os.path import dirname as dname

def loadfiles(pathlist: Union[list, tuple]) -> object:
    """ Returns a pd.DataFrame with columns
        -----------------------------------
        'filename': name of file without extension,
        'ext': file extension,
        'parent': parent directory name,
        'fpaths': path to file """
    return pd.DataFrame(((bname(sheet).split(".", 1)[0],
                          os.path.splitext(sheet)[1],
                          bname(dname(sheet)), sheet,)
                         for sheet in pathlist),
                        dtype = object,
                        columns=["filename", "ext",
                                 "parent", "fpaths"]).sort_values(
        "filename").reset_index(drop=True)

def main():
    if __name__ == __main__:
        loadfiles(pathlist)
