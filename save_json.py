#!/usr/bin/env python3

import os
from typing import Union
import json

def save_json(fpath:Union[str, os.PathLike],
              jobj:dict) -> None:
    with open(fpath, mode='w', encoding='UTF-8') as jfile:
        json.dump(fp=jfile, obj=jobj)
    jfile.close()

def main():
    save_json(fpath, jobj)
 
if __name__ == "__main__":
    main()
