'''class and object orient-2 main aspects of oop
class is a building block.it creates a new type of object as an instance.Blue print of object creation
syntax:class --------(classname):
ex:class employee-features->stmt1
                            stmt2
                            ....
'''

#creating a object
'''class abcd:
    var=100
obj=abcd()
print(obj.var)'''

#constructor
'''special method which gives access to our class
syntax: class employee:
            def __init__(self,arguments):'''
#__init__ method
'''class icici:
    def __init__(self,cash):
        self.cash=cash
        print("cash deposited is:",cash)
#d="1,00,000/-"
obj=icici(100000)#obj=icici(d)'''

'''Special Methods:
    __repr__->stringevaluations
    __cmp__->any two py objects
    __len__->object's length
    __call___->class can be called as afunction
    __hash__()->decides where to place elements in the memory based on ascii values
    __iter__()
    __getitem__()
    __setitem__()
#methods used to compare two objects
    __lt__()
    __le__()
    __eq__()
    __ne__()
    __gt__()
    __ge__()'''
#code to demonstrate the use of class attributes 
''''class har:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("a:",self.a)
        print("b:",self.b)
        print("sum:",self.a+self.b)
obj=har(10,12.34)
obj.display()
print("object.__dict__:",obj.__dict__)
print("object.__doc__:",obj.__doc__)
print("class.__name__:",obj.__class__.__name__)
print("class.__module__:",obj.__class__.__module__)
print("class.__bases__:",obj.__class__.__bases__)'''


#code to segegrate the array into even and odd numbers using a class modifying mutable type attribute
'''class number:
    e=[]
    o=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.e.append(num)
        else:
            number.o.append(num)
#n=number(11,22)#error due to positional orguments
#print("even:",n.e)
#print("odd:",n.o)
n1=number(11)
n2=number(22)
n3=number(33)
n4=number(44)
n5=number(55)
#print("even:",number.e)
#print("odd:",number.o)
print("even:",n1.e)
print("odd:",n1.o)'''

#math evaluation
#write a  code to calculate area and circumference of a circle using a class circle with radius float value(7.5)
'''from math import pi
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return pi*self.radius*self.radius#pow(pi,2)
    def circumference(self):
        return 2*pi*self.radius
r=float(input("enter radius of the circle:"))
c=circle(r)
print("Area of the circle is:",c.area())
print("circumference of the circle is:",c.circumference())'''


#code to display and insert data in a hash table using hashTable
class hashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
    def hash_function(self,key):
        return key%self.size
    def insert(self,key):
        index=self.hash_function(key)
        self.table[index].append(key)
    def display(self):
        for i in range(self.size):
            print(f"index {i}:{self.table[i]}")
size=int(input("enter the size of the hash table:"))
ht=hashTable(size)
n=int(input("enter the numbers of elements to insert:"))
for i in range(n):
    key=int(input("enter the key to insert:"))
    ht.insert(key)
ht.display()