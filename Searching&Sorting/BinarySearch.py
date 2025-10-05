def BinarySearch(L, v):
#Binary Search only works on sorted lists
    if L == []:
        return False
    
    m = len(L)//2
    if v == L[m]:
        return True;

    if v < L[m]:
        return BinarySearch(L[:m], v)
    else:
        return BinarySearch(L[m+1:], v)