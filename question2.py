#Question 2
def addUpTo(i):
    sum = 0
    for j in range(i):
        sum = sum + j
    print('the sum of the numbers from 1 to', i ,'is', sum)
'''
on addUpTo(i): 
    it is close but not quite. 
    in python, range is [), which means upper bound is exclusive.  
'''
    
    
#Challenge Number 1
def Fibonacci(n): 
    if n<2: 
        return n - 1
    else: 
        return Fibonacci(n - 1)+Fibonacci(n - 2)

'''
Fibonacci is: 0,1,1,2,3,5,8,13
the one you built is a very good approach, although the answer is wrong.

if use recursive: 

---------------------------------
def Fibonacci(n): 
    if n<2:
        return 0
    elif n==2: 
        return 1 
    else: 
        return Fibonacci(n - 1)+Fibonacci(n - 2)
---------------------------------

if use dp: 
---------------------------------
def Fibonacci_dp(n):
    fib=[0 for i in range(n+1)]
    for i in range(1, n+1):
        if i==1:
            fib[i]=0
        elif i==2:
            fib[2]=1
        else:
            fib[i]=fib[i-1]+fib[i-2]

    return fib[n]
--------------------------------- 
''' 
    
    

def fiboSum(n):
    print('the sum of the first', n ,'fibonacci numbers is', Fibonacci(n+2) - 1)
'''
    smart solution. although it is not correct. since your implementation Fib is incorrect
'''  
    

#Challenge Number 2
def triSum(n) :
    print('the sum of the first', n ,'triangle ners is', int(n*(n+1)*(n+2)/6))
        
addUpTo(50)
fiboSum(3)
triSum(3)