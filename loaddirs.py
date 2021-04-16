#!usr/bin/env/python3

import os
from typing import Union

def loaddirs(
  src_path: Union[os.PathLike, str]
) -> list:
    """ Recursively lists the full relative path of all
        directories in a directory.
        Only lists files, not directories.
        ----------------------------------
        Parameters
        ----------
        src_path: Path of directory to be scanned
        -----------------------------------------
        Returns:
        --------
        dirlist: 1D list full relative paths
    """
    dirlist = []
    for allfiles in os.walk(src_path):
        for adir in allfiles[1]:
            output = os.path.join(allfiles[0], adir)
            if os.path.isdir(output):
                dirlist.append(output)
    return dirlist

def main():
    loaddirs(src_path = '')

if __name__ == '__main__':
    main()
