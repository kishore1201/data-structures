# DYNAMIC PROGRAMMING
"""
FIBONACCI Series
1 2 3 4 5 6 7 8 9 -position  
1 1 2 3 5 8 13 21 34
"""
#"bottom up approach using tabulation "
def Fibo(position):
    if position <=2:
        print(1)
        return
    dp=[0]*(position)
    dp[0]=1
    dp[1]=1
    for i in range(2,position):
        dp[i]=dp[i-1]+dp[i-2]
    print(f"fibo of {position} : {dp[-1]}")
Fibo(9)

# top down
def Fibo_(position,memory):
    if position in memory:
        return memory[position]
    if position<=2:
        return 1
    memory[position]=Fibo_(position-1,memory)+Fibo_(position-2,memory)
    return memory[position]
 
print(Fibo_(4,{}))