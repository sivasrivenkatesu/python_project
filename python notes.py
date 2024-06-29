"""#PYTHON DATATYPES AND VARIABLE AND OPERATIONS
'''a=5
b=5.0
c=1+5j
d=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

list=[10,20,30]
list.append(40)
list.remove(30)
print(list[1:2])
print(list)"""
"""
s=20
i=30
v=40
print(s+i+v)
print(s-i-v)
print(s*i*v)
print(s/v)
i=100
sum=sum+i
for i in range(1,10):
    print(sum)
        """
"""
geeks=1
Geeks=2
ge_ek_s=3
_geeks=4
geeks_=5
_GEEKS_=6
print(geeks,Geeks,ge_ek_s)"""
"""
age=45
name="siva"
salary=1456.6
print(age)
print(name)
print(salary)"""


'''
a=40
b=12
print("the sum is :",a+b)
print ("the sub is :",a-b)
print("the multipication is :",a*b)
print("the division is:",a/b)
print("the quotient is :",a//b)
print("the exponentiation is :",a**b)
print("The remainder is :",a%b)'''
'''
a=10
b=30
c=a>b
d=a<b
e=a>-b
f=a!=b
g=a and b
print(a,b,c,d,e,f,g)'''
'''
a=10+3*4
print(a)
a=10+3*4
a=10+3*4
print(a)
a=10+3*4
print(a)
a=10+3*5555
print(a)'''
'''
p1=5.50*2
p2=8.75*3
p3=12.40*1
p4=p1+p2+p3
print("total cost of the items before x:",p4)
p5=p4*8/100
p6=p4+p5
print("Total cost of the items after x:",p6)'''


#left and right shift operators
#print(8>>2)'''(00001000>>2)=(00000010)=ans=2'''
#print(8<<2)'''(00001000<<2)=(00100000)=ans=32'''    



#if else ladder example
'''
a=int (input())
b=int (input())
c=int (input ())
if(a>=b and a>=c):
    print(a)
elif (b>=c and b>=a):#and operator
    print(b)
else:
    print(c)
'''
#short hand if
'''if 10>3 :print ("greater")'''

#short hand if else
'''
print("A")if (10>3)else print("b")'''

#one line if-nested else with three condition
'''
a=int (input())
b=int (input())
print(a)if a>b  else print(b)if b>a else print ("a=b")'''

#simple hello world
'''
a=int (input())
b=int (input())
if(a>b):print("hello World")'''

#simple odd or even
'''a=int (input())
print("Even") if (a%2==0) else print("odd")'''

#simple age program
'''age=int (input("age"))
print("Adult") if (age>=18) else print("child")'''

#simple celcius to fahrenheit
'''
c=float(input("celcius:"))
f=((9/5)*c)+32
print("The fah is : ",f)'''

#simple vowel or consonant
'''
let=input("Enter the char:")
print ("vowel") if let in "aeiouAEIOU" else print("consonant")'''

#LOOPS IN PYTHON - WHILE
#SYNTAX:WHILE EXPRESSION STATEMENTS
'''
i=0
n=int(input())
while i<n:
    i=i+1;
    print("ssiva")
'''

#using while loop with else statement
'''i=0
n=int(input())
while i<n:
    i=i+1;
    print("ssiva")
else:
    print("Sri venkatesu")'''

#infinite while loop in the python
'''while(1):
    print("siva")
'''

#for loop in python
'''
n=int(input())
for i in range(1,n+1):
    print(i,".siva sri venkatesu")
    print("\n")
'''    
#for loop in list
'''
#for loop in list
a=["siva","sri","venkatesu"]
for n in a:
    print(a)'''

#for loop in tuple
'''
a=("siva","sri","venkatesu")
for n in a:
    print(n)
'''


#for loop in string
'''
a="siva"
for n in a:
    print(n)
'''

#for loop in set
'''
a={"siva","sri","venkatesu"}
for n in a:
    print(n)
'''
#simple swapping program

'''
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
print("before swapping")
print("The value of a is ",a)
print("The value of b is ",b)
b=a+b
a=b-a
b=b-a
print("after swapping")
print("The value of a is ",a)
print("The value of b is ",b)

'''

#simple quadratic equation program
'''import math

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b * b) - (4 * a * c)
e = math.sqrt(d)

if d < 0:
   print("The roots are imaginary roots")
elif d == 0:
    r = -b / (2 * a)
    print("The root is:", r)
else:
    r1 = (-b + e) / (2 * a)
    r2 = (-b - e) / (2 * a)
    print("The roots are:", r1, "and", r2)
'''

#simple palindrome program
'''
num=int(input("Enter the number to check:"))
dup=num
#rev=0
if(num<=0):
   print("the inputted value is invalid")
else:
   while(num!=0):
      rev=rev*10+num%10
      num//=10
  if(num==num[::-1]):
      print(dup," is a palindromic number")
  else:
      print(dup,"is a non palindromic number")
'''
#simple fibonacci program
'''
n1=0
n2=1
n=int(input("Enter no of terms: "))
print(n1)
print(n2)
for i in range (3,n+1):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
'''
#fruitful functions
'''
def add(a,b):
   return a+b
def mul(a,b):
   return a*b
def div(a,b):
   return a//b
a=int (input("Enter the value of a"))
b=int (input("Enter the value of b"))
print(add(a,b))
print(mul(a,b))
print(div(a,b))k
'''

#lambda
'''
#It is a anonymous function
x=lambda a:a+10
print (x(5))
'''
#lambda using functions
'''
def add(a):
   x=lambda a:a*22
   return x(a)
a=int (input("Enter the value of a"))
c=add(a)
print(c)
'''
# unit 2
#list
#ordered(we cannot change the order),changeable(mutable),allow duplicate value,datatype
#friendly we can include any datatype elements in the same list 
#it contains index value range from 0
'''
mylist=["HI","HOW","Are","you"]
print(mylist)
print(len(mylist))
'''

#constructor in list
'''
a=list(("apple","banana","mango"))//to ease the compliation process constructor is used
print(a)
print(type(a))
'''

#arrays
#collection of similar datatype element

#append -adding an element in the end
'''
mylist=["HI","how","Are","you"]
print(mylist)
print(len(mylist))

mylist.append("siva")
print(mylist)
for i in range(1,9):
    mylist.append(i)
print(mylist)
for i in mylist:
    print(i)
mylist.pop(3)#data in the particullar index can be deleted 
print(mylist)
a=["a","b","c","d"]
mylist.extend(a)
print(mylist)
#insert(it can add new values at any place of the list)
mylist.insert(3,5)
mylist.insert(4,5)
#3 represents index and 5 represents the value
print(mylist)
mylist.remove("siva")#it can delete the value in the list at any position
print(mylist)
#slicing
print(mylist[:4])#beginning to end of  the index ie.,0 to 4
print(mylist[2:])#from the given index to end of the list ie.,2 to end of the list
print(mylist[2:4])#prints from 2 to 4 th of the list

#reverse
mylist.reverse()
print(mylist[::-1])
print(mylist)

#min And max element
a=list((1,2,3,4,5,6,7,8,9))
print(min(a))
print(max(a))

#count operation
b=list((1,2,3,2,2,6,7,8,9))
print(b.count(2))#counts the number of occurences of a given value

#concatenation
print(a+b)#it joins both the list

#getting index
print(mylist.index("how"))#prints the index of the given value

#sorting
c=[1,1,2,5,6,5,5,9]
c.sort()#asscending arrangement
print(c)

#clear
c.clear()#prints empty list
print(c)
c.clear()

#copying
d=a.copy()
print("copied list",d)
for i in mylist:
    print(i)
my=[12,1,2,2,12,1,21,2,1]
my1=[element*element for element in my]
print(my1)

#map function
def square(num):
    return num*num
y2=map(square,my)
print(y2)#prints address

#filter function
def even(num):
    return num%2==0
y3=filter(even,my)
print(y3)
'''

#sum of all even numbers upto n
'''
n=int(input("Enter the number:"))
sum=0
for i in range(0,n+1):
    sum+=i
print(sum*2)
'''

#palindrome of a number
'''
text=input()
if(text==text[::-1]):
   print(text,"is a palindrome")
else:
    print("Not a Palindrome")
'''

#swapping without temporary variable
'''
a=int(input())
b=int(input())
b=a+b
a=b-a
b=b-a
print(a)
print(b)
'''

#check whether the given data is a vowel or consonants
'''ch=(input())
if ch in "aeiouAEIOU":
    print("VOWEL")
else:
    print("CONSONANTS")
'''

#FACTORIAL OF A GIVEN NUMBER
'''
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
'''

#list position swapping
'''
list=[1,2,3,4,5,6,7]
temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)
'''


#coffee shop
'''
#task1
coffee_price=int(input("enter the price of the coffee"))
pastry_price=int(input("enter the price of the pastry"))
coff_num=int(input("Enter the number of coffees ordered"))
pastry_num=int(input("Enter the number of pastries ordered"))
cof_discount_threshold=int(input("Enter the minimum number of coffee to be ordered to attain discount"))
cof_discount_percentage=int (input("Enter the discount for coffee"))
pastry_minimum_threshold=int(input("Enter the minimum number of pastry to be ordered to attain discount"))
pastry_discount_percentage=int(input("Enter the discount for pastry"))
#task2
coffee_total=coffee_price*coff_num
#task3
pastry_total=pastry_price*pastry_num
#task4
if(coff_num>=cof_discount_threshold):
    coffee_total=coffee_total-(coffee_total*(cof_discount_percentage/100))
#task5
if(pastry_num>=pastry_minimum_threshold):
    pastry_total=pastry_total-(pastry_total*(pastry_discount_percentage/100))
#task6
total_amount=coffee_total+pastry_total
print("The total bill amount",total_amount) 
'''

#simple calculator program
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def floor(a,b):
    return a//b
a=int(input("Enter the value of a"))
b=int (input("Enter the value of b"))

print("choice 1:add")
print("choice 2:sub")
print("choice 3:mul")
print("choice 4:div")
print("Choice 5:mod")
print("choice 6:floor")
choice=int(input("Enter the choice of operation to be performed"))
print("the output of the given operation is ")

  if(choice==1):
    print(add(a,b))
  elif(choice==2):
    print(sub(a,b))
  elif(choice==3):
    print(mul(a,b))
  elif(choice==4):
    print(div(a,b))
  elif(choice==5):
    print(mod(a,b))
  elif(choice==6):
    print(floor(a,b))
  else:
    print("enter the valid choice")
    break
'''

#sandwich vowel program
'''
def sv(string):
  vowel="aeiou"
  newstring=""
  for i in range (len(string)):
    if string[i] in vowel:
        if i==0 or i==len(string)-1:
            newstring+=string[i]
        elif string[i-1] not in vowel and string[i+1] not in vowel:
            continue
    else:
       newstring+=string[i]
  return newstring    
string=input()
newstring=sv(string)
print(newstring)
'''

#list delete and insert
'''
my_list = []

def insert(value):
    my_list.append(value)
def delete():
    if my_list:
        my_list.pop()
    else:
        print("List is empty. Cannot delete.")
def display():
    print("List contents:", my_list)

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        value = input("Enter value to push: ")
        insert(value)
    elif choice == 2:
        delete()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
'''

#prime number program
'''
def isprime(num):
    c=0
    if num==1 :
        print("neither prime nor composite:")
        exit
    for i in range(1,num+1):
        c=c+1 if num%i==0 else c
    return c
num=int(input())
print("prime") if isprime(num)==2 else print ("non prime")
'''
#pattern printing program
'''
for i in range(5,0,-1):
    for j in range(0,5-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
'''
#least common value at list
'''
def lisum(list1, list2):
    index_sum = float('inf')
    common_elements = []
    index_dict = {element: index for index, element in enumerate(list2)}
    for i, element in enumerate(list1):
        if element in index_dict:
            current_index_sum = i + index_dict[element]
            if current_index_sum < index_sum:
                index_sum = current_index_sum
                common_elements = [element]
            elif current_index_sum == index_sum:
                common_elements.append(element)

    return common_elements
list1 = ["Shakespeare", "Hemingway", "Tolkien", "Fitzgerald"]
list2 = ["Rowling", "Hemingway", "Tolkien", "Austen"]
result = lisum(list1, list2)
print(result)
'''
'''
#unit 2(dictionary)
#used to store data in (key,value) pairs,not allow dupicates,mutable,ordered

#syntax-key:value
dict={
    "key":"value","year":2005,"data":31,"month":"july","month":"august","month":"july"#modiifcation
    }
print(dict)
dict["key"]="siva"#(dict[key]=value-modifying)
print(dict["key"])
print(dict)
print(dict["year"])
print(dict["data"])

#operations
#definition operation -()
#mutable operation - {}-addition of the key value pairs,del,update
#immutable-len,key,values,setdefault,in,get,items

dict={
    "key":"value","year":2005,"data":31,"month":"july","month":"august","month":"july"#modiifcation
    }
print(dict)
dict["key"]="siva"#(dict[key]=value-modifying)
print(dict["key"])
print(dict)
print(dict["year"])
print(dict["data"])

del dict["key"]
print(dict)
dict.update({"key":"Siva"})
print(dict)


#format operator
#-formats given string

c=42
print('%d' % c)

#command line arguments
'''
'''
input=string
another way of accept other than normal input functions
i/p is passed as the arguments
processing of these input is based on the sys module
all input passed cmd will form list

sys.argv -> to access the cmd prompt
argv accessed through the index st from the 0

sys.argv[0] starts from the file name

py filename py arg1 arg2 arg3
'''
'''
'''

#errors and exceptions in py
'''
types of error
-syntax error
-runtime error
-logical error

error handling

-try
-except
-finally
'''

#write a
'''
a = int(input())
b = int(input())

try:
    result = a / b
    print(result)
    if b == 0:
        raise ZeroDivisionError("it is not divisible")
    else:
        print("No error")
except ZeroDivisionError as e:
    print(e)
finally:
    print("program ends")
'''
'''
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''

#what is oops in python?
#-is a programming paradium that uses objects and classes in programming
#-aims to implement a real world entities
#-to bind the data and the functions that work together as a single unit
#-concepts--class,object,polymorphism,encapsulation,inheritance ,data abstraction

#python class
'''
class is collection of object
contains the blueprint by which the object being created
classes re created by keyword class attributes are the variables that belongs to the class
attributes are always public, can be accesed using the dot(.)
'''

#syntax for class:
'''
class name:
    #statements
    .
    .
    .
    #statements n
'''
#python constructor
'''
class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
'''

#constructor init method
'''
class sample:
    def __init__(self):
        print("this is a init constructor")
obj=sample()
'''

#inheritance
#single inheritance
'''
class dad():
    def phone(self):
        print("Iam dad")
class son(dad):#single inheritance
    def lap(self):
        print("iam son")
ram=son()
ram.lap()
ram.phone()
'''
#multiple inheritance
'''
class dad():
    def phone(self):
        print("Iam dad")
class mom():
    def cook(self):
        print("iam mom")
class son(dad,mom):
    def lap(self):
        print("iam son")
ram=son()
ram.phone()
ram.cook()
ram.lap()
'''
#multilevel inheritance
'''
class grandpa():
    def money(self):
        print("iam grandpa")
class dad(grandpa):
    def phone(self):
        print("Iam dad")
class mom(dad):
    def cook(self):
        print("iam mom")
class son(mom):
    def lap(self):
        print("iam son")
ram=son()
ram.phone()
ram.cook()
ram.money()
ram.lap()
'''
