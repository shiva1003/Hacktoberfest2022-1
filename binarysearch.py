#binery search
def bs(arr,key,low,high):
    while low<=high:
        mid=(low+high)//2    # mid = low + (high - low)//2
        if(arr[mid]==key): return mid
        elif(arr[mid]<key):  low=mid+1
        else:  high=mid-1
    return -1
arr=[5,6,8,9,7]
key=8
res=bs(arr,key,0,len(arr)-1)
if(res!=-1):
    print("element found at index:", res)
else:
    print("element not found")
