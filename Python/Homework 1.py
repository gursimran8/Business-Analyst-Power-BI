'''print ("Hello User")
n=input("Please enter your name: ")
a=int(input("Please enter your age: "))
if(a>=18):
      print("Eligible to vote")
elif(a<18):
    print("Not eligible to vote")
    

print("Hello User")
n=input("Please enter your name: ")
a=int(input("Please enter your age: "))
if(a<16):
    print("Child")
elif(a>=16 and a<55):
    print("Young")
else:
    print("Old")'''

#WHILE Loop
'''i=0
while(i<=25):
    print(i)
    i=i+5'''
#For Loop

'''for i in range(10,0,-1):
    print(i)'''

#Practice
'''i=1
while(i<=10):
    print(i)
    i=i+1'''

'''a=2
b=1
while(b<=10):
    print(a,"*",b,"=",a*b)
    b=b+1'''

'''a=2
b=1
for b in range(1,11,1):
    print(a,"*",b,"=",a*b)'''

'''a=10
b=2
while(a>=1):
    print(b,"*",a,"=",b*a,)
    a=a-1
print("------")

a=10
b=2
for a in range(10,0,-1):
    print(b,"*",a,"=",a*b)
print("------")

a=int(input("Enter value to find table:"))
b=int(input("Enter table length:"))
i=1
while(i<=b):
    print(a,"*",i,"=",a*i)
    i=i+1
print("------")
a=int(input("Enter value to find table:"))
b=int(input("Enter table length:"))
i=1
for i in range(1,b+1,1):
    print(a,"*",i,"=",a*i)
print("------")'''
'''#Non Parameterized
def Happy():
    print("Hello")
    print("Bye")
Happy()
print("-----------")
#Parameterized
def Joy(a,b):
    print(a*b)
x=int(input("1st Value:"))
y=int(input("2nd Value:"))
Joy(x,y)'''


#Home Work 13/8/24 
#Take 10 numbers input from the user and calculate sum of all the numbers
#User inputs all numbers



'''#User only inputs 1st number and pattern

def x(a,b,c,d):
    print(a+b+c+d)
e=int(input("Start Number:"))
f=int(input("Last Number:"))
g=int(input("Jump:"))
for i in range(e,f+1,g):
    print()
x(a,b,c,d)
print('''


''')'''

'''#Take 5 numbers input from the user and print the table of all the numbers

a=1
b=int(input("1st Number:"))
g=1
c=int(input("2nd Number:"))
h=1
d=int(input("3rd Number:"))
i=1
e=int(input("4th Number:"))
j=1
f=int(input("5th Number:"))
while(a<=10):
    print(b,"*",a,"=",b*a)
    a=a+1
print()
while(g<=10):
    print(c,"*",g,"=",c*g)
    g=g+1
print()
while(h<=10):
    print(d,"*",h,"=",d*h)
    h=h+1
print()
while(i<=10):
    print(e,"*",i,"=",i*e)
    i=i+1
print()
while(j<=10):
    print(f,"*",j,"=",f*j)
    j=j+1
print('''


''')


#Take a name input from the user and print the name in reverse order

n=input("Enter your name:")
r_n=n[::-1]
print(r_n)'''

#Home Work 13/8/24 
#Take 10 numbers input from the user and calculate sum of all the numbers
#User inputs all numbers
'''
b=0
for i in range(1,11):
    a=int(input("Enter number: "))
    b=b+1
print("Sum of numbers entered is",b)
'''
#Take 5 numbers input from the user and print the table of all the numbers

'''for i in range(1,6):
    a=int(input("Enter number: "))
    for i in range(1,10):
        print(a,"*",i,"=",a*i)'''

#Take a name input from the user and print the name in reverse order

'''a=input("Enter name:")
print(a[::-1])'''

'''a=[1,2,3,4,5]
print(a[1])
print(a[1:3])'''# Indexing start from 0 ... higher/last value to be 1 higher


#Take 10 no's input from the user and add the numbers into the list using both loops 
#For loop
'''def a():
    b=[]
    for i in range(1,11):
        c=int(input("Enter number: "))
        b.append(c)
    print(b)
a()'''
#while loop
'''def a():
    i=1
    b=[]
    while (i<=10):
        c=int(input("Enter number: "))
        b.append(c)
        i=i+1
    print(b)
a()'''    
#Take 10 no's input from the user and add the numbers into the list and
#calculate the sum of all the numbers using any loop 
'''def a():
    d=[]
    b=0
    for i in range(1,11):
        c=int(input("Enter number: "))
        b=b+c
        d.append(c)
    print ("Sum = ",b)
    print("List of all numbers: ",d)
a()'''



#Take 10 no's input from the user
#and if the number is odd then only add the numbers into the list using both loops
'''def while():
    a=[]
    b=1
    while(b<=10):
        c=int(input("Enter number: "))
        if(c%2==0):
            pass
        else:
            a.append(c)
        b=b+1
    print (a)
while()'''

'''def for()
    b=[]
    for i in range(1,11):
        a=int(input("Enter number: "))
        if(a%2==0):
            pass
        else:
            b.append(a)
    print(b)
for()'''


#1. Take a string input from the user and print in reverse order without using reverse inbuilt method . 
#2. Take 10 no. Input from the user add the no.s into the list and print the list in the manner so that the odd numbers will be displayed first and  the even after that .
#3. Take a string input from the user and print in vowels only present in the string

#Take 10 no's input from the user and add the numbers into the list ,
#display the list in reverse order using any loop
b=[]
c=[]
'''for i in range(1,11):
    a=int(input("Enter number: "))
    b.append(a)
for j in range(len(b)-1,-1,-1):
    c.append(b[j])
print(c)'''

#1. Take a string input from the user and print in reverse order without using reverse inbuilt method .

'''a=input("Enter string: ")
c=""
for i in range(len(a)-1,-1,-1):
    c=c+a[i]
print(c)'''


#2. Take 10 no. Input from the user add the no.s into the list
#and print the list in the manner so that the odd numbers will be displayed first and  the even after that .

'''b=[]
c=[]
i=1
while(i<=10):
    a=int(input("Enter number: "))
    if (a%2==0):
        b.append(a)
    elif (a%2==1):
        c.append(a)
    i=i+1
for j in range(len(c)):
    b.append(c[j])
print(b)'''

#3. Take a string input from the user and print in vowels only present in the string

b=input("Enter string: ")
c=""
i=1
for i in range(len(b)):
    if (b[i]=="a" or b[i]=="e"or b[i]=="o"or b[i]=="i"or b[i]=="u"):
        c=c+b[i]
        j=b[i]
        print(j)
print(c)


'''a=input("Enter string: ")
b=[]
c=("aeiou")
for i in range(0,len(a)):
    if(a[i] in c):
        print(a[i])
        b.append(a[i])
print(b)'''

    
