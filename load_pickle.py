#!/usr/bin/env python3

def load_pickle(fpath:Union[str,os.PathLike]):
    import pickle
    with open(fpath, 'rb') as afile:
        obj = pickle.load(afile)
    afile.close()
    return obj

def main():
    return load_pickle(fpath)
 
if __name__ == "__main__":
    main()
