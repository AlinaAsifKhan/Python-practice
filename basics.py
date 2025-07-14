#printing
print('Hello, World.')

#variable
s= 'leena'
print(s)
print('Hello, '+s)

#input
#inp=input('Input your name:')
#print('Hello, '+ inp)

#printing type of a variable
y=3
z='lin'
print(type(y))
print(type(z))

#Multiple Variables
x, y, z= "apple","banana","mango"
print(x,y,z)

x=y=z=3;
print(x,y,z)

#unpacking a list into variables
fruits= ["mango","apple", "banana"]
a,b,c=fruits
print(a,b,c) #with space
print(a+b+c) #without space

#global and local vars
m="ballerina"
def myfunc():
    n="Cappucina"
    global m
    m= "ballerinas"
    print(m,n)

myfunc()

#2
x = "awesome"

def myfunc():
  x = "fantastic"
  global q
  q ="mimimi"
  print("Python is " + x)

myfunc()

print("Python is " + x + q)

#string
a = "Hello, World!"
print(a[1])

string and loop
for x in 'banana':
    print(x)

#length of a string
a="Helooo, My name is leena"
print("The length of string is:", len(a))

#Check string
txt="I gotta do smth"
if("gotta do" in txt):
    print("yes")
else:
    print("no")

#slicing
print(txt[2:7])
print(txt[:8])
b = "Hello, World!"
print(b[-5:-2])

txt1=" Currenly, doing a Python Internship"
print(txt1.upper())
print(txt1.lower())
print(txt1.strip())
print(txt1.replace("r","e"))
print(txt1.split(","))

#fstrings
age=20
print(f"My age is :{age}")
    #OR
txt=f"My age is {age}"
print(txt)
     #OR with modifier
txt= f"My age is: {age:.2f}"
print(txt)
     #OR(with operations)
txt= f"Soon, i'm gonna be: {age+1}"
print(txt)

#escape character
print("Want to eat smth \"sweet\"")
print(txt.center(30))