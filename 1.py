def add(a,b):
    return str(a+b)

def sub(a,b):
    return str(a-b)

def mul(a,b):
    return str(a*b)

def div(a,b):
    return str(a/b)

print("selectt operation")
print("1.Add")
print("2.subtraction")
print("3.multiply")
print("4.div")

choice=input("enter the choice(1 or 2 or 3 or 4)=")

a=int(input("enter the fst numb="))
b=int(input("enter the second numb="))

if choice=="1":
    print(a,'+',b,'=',add(a,b))
elif choice=="2":
    print(a,'-',b,'=',sub(a,b))
elif choice == "3":
    print(a,'*',b,'=',mul(a,b))
elif choice=="4":
    print(a,'/',b,'=',div(a,b))



