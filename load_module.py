#!usr/bin/env/python3

import os
import shutil
from typing import Union

def load_module(modulepath: Union[str, os.PathLike]) -> None:
    os.makedirs(os.path.join(os.getcwd(), os.path.basename(modulepath)),
                exist_ok=True)

    commands = sorted(item for item in
                      [(shutil.copy(os.path.join(modulepath, item),
                                    os.path.join(os.getcwd(),
                                                 os.path.basename(modulepath), item)),
                        (''.join('from ' + os.path.basename(modulepath) + '.' \
                                 + os.path.splitext(item)[0] \
                                 +' ' + 'import ' + \
                         os.path.splitext(os.path.basename(item))[0])))[1]
                       for item in os.listdir(os.path.join(
                           os.path.dirname(os.getcwd()), os.path.basename(modulepath)))
                       if item.endswith('.py') and 'setup' not in item])[1:]
    [print(item + '\r') for item in commands]
    
def main():
    if __name__ == __main__:
        load_module(modulepath)
