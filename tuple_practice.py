emp1=(input("enter emp1 name: "))
emp2=(input("enter emp2 name : "))
emp3=(input("enter emp3 name : "))
emp4=(input("enter emp4 name : "))
emp5=(input("enter emp5 name : "))

tuple=(emp1,emp2,emp3,emp4,emp5)
print(tuple)
print(len(tuple))
s=int(input("enter the first index position : "))
e=int(input("enter the ending index position : "))
print(tuple[s:e])
