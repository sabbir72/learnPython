A = {'orange', 'banana', 'pear', 'apple'}

Datatype =type(A)
print(Datatype)

# B=set('banana', 'pear', 'apple')

# Datatype=type(B)
# print(Datatype) 

C=set('abracadabra')
print(C)

Datatype=type(C)
print(Datatype)


D= {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print("Print set line D", D)

D.add('kiwi')
print("Print set line D after adding kiwi", D)

D.update({'mango', 'grapes', 'papaya'})
print("Print set line D after adding mango, grapes, papaya", D)

# D.remove('sabbir')
D.discard('sabbir')
print("Print set line D after removing sabbir", D)
D.pop()

print("\n Print set line D after pop", D)

D.clear()
print("\n Print set line D after clear", D)



Price={ 5,6,7,8,9,10,11,12,13,14,15}

Age={ 1,2,3,4,5,6,7,8,9,10}

CheckUnion=Price.union(Age)
print("\n Print set line CheckUnion", CheckUnion)

CheckIntersection=Price.intersection(Age)
print("\n Print set line CheckIntersection", CheckIntersection)