#!/usr/bin/env python3

def lst_intersection(lst1:list, lst2:list):
    '''
    Source: https://www.geeksforgeeks.org/python-intersection-two-lists/
    '''
    return [value for value in lst1 if value in set(lst2)]
    
def main():
    return lst_intersection(lst1, lst2)
 
if __name__ == "__main__":
    main()

