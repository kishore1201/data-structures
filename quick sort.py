import random   # because of worst case of time complexity
def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=random.choice(arr)
    left=[]
    for i in arr:
        if i<pivot:
            left.append(i)
    right=[]
    for i in arr:
        if i>pivot:
            right.append(i)

    middle=[]
    for i in arr:
        if i==pivot:
            middle.append(i)
    return quicksort(left)+middle+quicksort(right)



arr=[3,2,5,7,9,1,6]
print(quicksort(arr))
