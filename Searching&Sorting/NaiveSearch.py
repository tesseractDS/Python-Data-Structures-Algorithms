def NaiveSearch(L, v):
    for i in range(len(L)):
        if L[i] == v:
            return i
        
    return -1