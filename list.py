names=["harii","harish","gy","gopi"]
names[0]="Harii"
print(names)
print(names[0])

names=["harii","harish","gy","gopi"]
print(names[-1]) # -1 represents the last letter

names=["harii","harish","gy","gopi"]
print(names[0:4])

# list basic program

numbers=[0,1,2,3,4,5]
numbers.append(6)
numbers.insert(0,-1)
#numbers.remove(0)
#numbers.clear()
print(numbers)
print(len(numbers))
print(-1 in numbers)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)