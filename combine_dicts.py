#!usr/bin/python3

import sys
from typing import Sequence
from loadutils.flatten import flatten

def combine_dicts(dictlist:Sequence)->dict:
    """ Combine dicts without duplicating or overwriting. 
    
    Iterates over list of dicts to find all keys, then
    removes the duplicates. After, looks for existing
    key:value pairs in all dicts from dictlist.
    Combines the result in a dict and returns it.
    
    Args:
        dictlist: Sequence of dictionaries
    
    Returns:
        Result of the key:value lookup iterations in a dict.
    """
    
    allkeys = flatten(tuple(tuple(adict.keys())
                               for adict in dictlist))
    ukeys = list(dict.fromkeys(allkeys))
    return dict((akey,[adict[akey] for adict in
             dictlist if akey in tuple(adict.keys())])
                for akey in ukeys)

def main():
    combine_dicts(sys.argv[1])

if __name__ == '__main__':
    main()

