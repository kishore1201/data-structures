target=7
nums=[2,3,1,2,4,3]

####

left=0
right=0
minimum = float('inf')  # Use infinity for comparison
#minimum=[]
subSum=0
while right<len(nums):
    subSum+=nums[right]
    
    while subSum>=target:
       # minimum.append(right-left+1)
        minimum=min(minimum,right-left+1)
        subSum-=nums[left]
        left+=1
    right+=1

result = minimum if minimum != float('inf') else 0
print(result)
#if len(minimum)==0:
#    print(0)
#else:
   # print(min(minimum))