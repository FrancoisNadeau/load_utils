#!/usr/bin/env python3

def read_json(fpath:Union[str, os.PathLike]) -> dict:
    with open(fpath, mode='r', encoding='UTF-8') as jfile:
        jdict = json.load(jfile)
    jfile.close()
    return jdict

def main():
    return read_json(fpath)
 
if __name__ == "__main__":
    main()
