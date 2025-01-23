# binary search and using two pointers algorithm
num=[0,1,2,3,4,5,6,7,8,9]
t=9
left=0
right=len(num)-1
while (left<=right):
    middle = left+right //2
    if t==num[middle]:
        print(middle)
        break
    elif t>num[middle]:
        left=middle+1
    else: # t<num[middle]:
        right=middle-1
if left>right:
    print("element not found")
