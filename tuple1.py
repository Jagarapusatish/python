tel=int(input("enter tel marks : "))
hin=int(input("enter hin marks : "))
eng=int(input("enter eng marks : "))
maths=int(input("enter maths marks : "))
sci=int(input("enter sci marks : "))
soc=int(input("enter soc marks : "))

tuple=(tel,hin,eng,maths,sci,soc)
print(tuple)
print(len(tuple))
r=int(input("enter the index position from where you want to display output : "))
print(tuple[r:])
