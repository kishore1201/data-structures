#four operation
#access
from array import *
arr=array('i',[1,2,3,4,5])
print(arr[4])
#insert
arr.insert(0,6)
print(arr)
#delete
arr.pop(0)
arr.pop() # the last index value willl be delete
print(arr)
#search
ar=array('i',[1,2,3,4,5])
a=2
for i in range(0,len(ar)):
    if ar[i]==2:
        print("true")
        break
