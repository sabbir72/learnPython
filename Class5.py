#tuple


a=(1,2,3,4,5)
Datatype=type(a)
print(Datatype)


Vegitables=('onion', 'potato', 'ginger', 'cucumber', 45, 32, 22,67,88.54,65)


print(Vegitables)


print(type(Vegitables[0]))

print(type(Vegitables[4]))

print(type(Vegitables[8]))


AddNew=Vegitables + ('tomato', 'carrot', 'cabbage','ginger')
print(AddNew)


Length=len(AddNew)
print(Length)

Count=AddNew.count('ginger')
print(Count)