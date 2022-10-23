def ls(lis,n,key):
    for i in range(0, n):
        if(lis[i]==key): return i
    return -1
lis=[5,6,8,9,7]
key=8
n=len(lis)
res=ls(lis,n,key)
if (res==-1): print("element not found")
else: print("element found at the index", res)
