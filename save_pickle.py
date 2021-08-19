#!/usr/bin/env python3

import os
from typing import Union
import pickle

def save_pickle(fpath:Union[str,os.PathLike]
                your_obj:object) -> None:
    import pickle
    with open(fpath, 'wb') as afile:
        pickle.dump(obj=your_obj, file=afile)
    afile.close()

def main():
    save_pickle(fpath, obj)
 
if __name__ == "__main__":
    main()
