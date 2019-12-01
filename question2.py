#Question 2
def addUpTo(i):
    sum = 0
    for j in range(i):
        sum = sum + j
    print('the sum of the numbers from 1 to', i ,'is', sum)

#Challenge Number 1
def Fibonacci(n): 
    if n<2: 
        return n - 1
    else: 
        return Fibonacci(n - 1)+Fibonacci(n - 2)

def fiboSum(n):
    print('the sum of the first', n ,'fibonacci numbers is', Fibonacci(n+2) - 1)

#Challenge Number 2
def triSum(n) :
    print('the sum of the first', n ,'triangle ners is', int(n*(n+1)*(n+2)/6))
        
addUpTo(50)
fiboSum(3)
triSum(3)