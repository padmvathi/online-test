a=int(input("enter the numb="))
new=1

if a % 2 == 0:
    a -= 1
for i in range(1, a + a):
    if i % 2 != 0:
        print(new, end=" ")
        new += 2
    else:
        print(',', end=" ")

