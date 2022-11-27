# find the biggest of three number

u1=int(input("please enter 1st number : "))
u2=int(input("please enter 2nd number : "))
u3=int(input("please enter 3rd number : "))

if u1>u2 and u1>u3:
    print(u1,"is greater")
elif u2>u3 and u2>u1:
    print(u2,"is greater")
elif u3>u2 and u3>u1:
    print(u3,"is greater")


