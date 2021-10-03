#!/usr/bin/env python3

import os
from typing import Union
import json

def read_json(fpath:Union[str, os.PathLike],
              encoding='UTF-8') -> dict:
    with open(fpath, mode='r', encoding=encoding) as jfile:
        jdict = json.load(jfile)
    jfile.close()
    return jdict

def main():
    return read_json(fpath, encoding)
 
if __name__ == "__main__":
    main()
