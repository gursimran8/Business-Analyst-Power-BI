print("MATURITY STATUS CHECKER")
n=input("Enter you name: ")
a=int(input("Enter your age: "))
if(a>0 and a<=18):
    print("You are a Child")
elif(a>18 and a<=40):
    print("You are Young")
elif(a>40 and a<=60):
    print("You and Mature")
else:
    print("You and Old")



print('''


VOTER AGE ELIGIBILITY CHECKER''')
n=input("Enter you name: ")
a=int(input("Enter you age: "))
if(a<18):
    print("Not Eligible")
else:
    print("Eligible")

