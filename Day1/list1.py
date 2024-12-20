thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print(len(thislist))
print(type(thislist))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

newlist = [x for x in thislist if x != "apple"] 
print(newlist)