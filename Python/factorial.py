def factorial(num):
    if num<=1:
        return 1
    else:
        return factorial(num-1)*num
n=int(input())
print(factorial(n))      
