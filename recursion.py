#recursion
# factorial 5
number=5
def factorial(num):
    if num==1:
        return 1 # it s the base condition
    return num* factorial(num-1)   
print(factorial(number))
