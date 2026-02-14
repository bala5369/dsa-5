'''Recursion
it is used in divide and conquer
types:
1)direct
2)indirect
3)head
4)tail
5)linear
6)tree
7)nested'''

#code to print n numbers in descending order using direct function->tailrecursion
'''def direct(n):
    if n==0:#breaking number
        return
    print(n)
    direct(n-1)
n=int(input("enter a value:"))
direct(n)'''

#code to check whether the given number is even or not using indirect function
'''def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1) 
n=int(input("enter a number:"))
print("even",is_even(n))'''




'''dry run:
n=4
is_even(4):
if 4==0:->F
is_odd

is_odd(3):
if 3==0:->F
is_even(2)

is_even(2):
if 2==0:->F
is_odd(1)

is_odd(1):
if 1==0:->F
is_even(0)

is_even(0):
if 0==0:->T
return True'''


#code to print n values using head recursion-> pratical joke
'''def head(n):
    if n==0:
        return
    head(n-1)
    print(n)
n=int(input("enter a number:"))
head(n)'''



#code to print the sum of n natural numbers using linear recursion
'''def linear(n):
    if n==0:
        return 0
    else:
        return n+linear(n-1)
n=int(input("enter n:"))
print("sum is:",linear(n))'''

'''dry run:
n=5
linear(5)
5==0->F
5+linear(4)
linear(4)
4==0->F
5+4+loinear(3)
linear(3)
3==0->F
5+4+3+linear(2)
linear(2)
2==0->F
5+4+3+2+linear(1)
linear(1)
1==0->F
5+4+3+2+1+linear(0)
linear(0)
0==0->T
return 0'''


#code to print a number in fibonnaci series using its index by tree recursion
'''def tree(n):
    if n<=1:
        return n
    return tree(n-1)+tree(n-2)
n=int(input("enter index:"))
print("fibinnoaci number:",tree(n))#considers series from 0'''

'''dry run
                          tree(4)
                        /       \
                    tree(3)      tree(2)
                    /   \          /   \
                tree(2)  tree(1) tree(1) tree(0)
                /   \       |       |       |
            tree(1) tree(0) 1       1       0
             |          |
            1           0                               
'''

#code to convert a number to zero using nested recursion
'''def timmer(n):
    if n<=0:
        return 0
    return timmer(timmer(n-1))
n=int(input("enter a number:"))
print(timmer(n))'''

'''dry run
n=5
5<=0->F
timmer(5)=timmer(timmer(4))
timmer(4)=timmer(timmer(3))
timmer(3)=timmer(timmer(2))
timmer(2)=timmer(timmer(1))
timmer(1)=timmer(timmer(0))
timmer(0)=return 0
'''
