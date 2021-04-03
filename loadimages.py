#!usr/bin/python3

import os
from typing import Union

def loadimages(indir: Union[os.PathLike, str]) -> list:
    """ Lists the full relative path of all '.jpeg' files in a directory.
        Only lists files, not directories.
        ----------------------------------
        Parameters
        ----------
        imdir: type = str
            Name of the directory containing the images.

        Return
        ------
        imlist: type = list
        1D list containing all '.jpeg' files' full relative paths """
    imlist = []
    for allimages in os.walk(indir):
        for image in allimages[2]:
            indir = os.path.join(allimages[0], image)
            if os.path.isfile(indir):
                imlist.append(indir)
    return imlist

def main():
    if __name__ == __main__:
        loadimages(indir)
