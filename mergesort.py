def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)    # creating temp arrays
    R = [0] * (n2)
    for i in range(0, n1):  # Copying the data to temp arrays L[]
        L[i] = arr[l + i]
    for j in range(0, n2):     # Copying the data to temp arrays R[]
        R[j] = arr[m + 1 + j]
    i = 0     #  index of first subarray
    j = 0     #  index of second subarray
    k = l     #  index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:    # Copy the rest elements of L[]
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:   # Copy the rest elements of R[]
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2   
        mergeSort(arr, l, m)   # Sorting first and second halves
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
arr = [22, 10, 13, 5, 6, 7]
n = len(arr)
for i in range(n):
    print("%d" % arr[i],end=" ")
 
mergeSort(arr, 0, n-1)
print("\nSorted array is given below")
for i in range(n):
    print("%d" % arr[i],end=" ")
 
