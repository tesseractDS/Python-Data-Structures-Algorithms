#defining Merge
def Merge(A,B):
    m,n = len(A), len(B)
    C,i,j = [],0,0

    #Base_case:When both lists A and B have elements for comparing
    while i < m and j < n:
        if A[i] <= B[i]:
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j+=1
    
    #Case1:When B is over
    while i < m:     
        C.append(A[i])
        i+=1
    
    #Case2:When A is over
    while j < n:
        C.append(B[j])
        j+=1
    
    return C


#defining MergeSort
def MergeSort(L):
    n = len(L)
    
    #if list has onlt one or no element
    if n<=1:
        return L
    #recursively sort left half of the list
    left = MergeSort(L[:n//2])

    #recurdsively sort right half of the list
    right = MergeSort(L[n//2:])

    #merge both left and right half of the list
    SortedList = Merge(left,right)
    return SortedList