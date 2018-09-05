################################LIST COMPREHENSION & GENERATOR EXPRESSION##########################
#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
lst=[1,2,3,4,5]
lst=[i**3 for i in lst]
print(lst)
#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
lst=[i for i in range(2,20)  for j in range(2,i) if(i%j==0)  ]
a=[i for i in range(2,20) if(i not in lst )]
print(a)
#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''
ANS:-In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.
The generator yields one item at a time — thus it is more memory efficient than a list.'''


##############################LAMBDA & MAP#############################

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2 ,36.5, 37.3, 37.8]
f=list(map(lambda x: 1.8*x+32,Celsius))
print(f)

#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
lst=[1,2,3]
def squ(n):
    return n*n
s=list(map(lambda n:squ(n),lst))
print(s)
###############################FILTER & REDUCE#########################
#Q.1- Filter out all the primes from a list.
lst=[1,2,3,4,5,6,7,8,9]
def isprime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
        
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n
    
p=list(filter(lambda n: isprime(n),lst))
print(p)
#Q.2- Write a python program to multiply all the elements of a list using reduce.
lst=[1,2,3,4,5,5]
from  functools import *
m=reduce(lambda x,y:x*y,lst)
print(m)
