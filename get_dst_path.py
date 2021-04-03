#!usr/bin/env/python3

import os
from typing import Union

def get_dst_path(
    src_path: Union[os.PathLike, str],
    dst_path: Union[str, os.PathLike] = None
) -> os.PathLike:
    return [dst_path if dst_path
            else os.path.join(
                os.getcwd(),
                os.path.splitext(bname(src_path))[1])][0]

def main():
    if __name__ == __main__:
        get_dst_path(src_path, dst_path)


