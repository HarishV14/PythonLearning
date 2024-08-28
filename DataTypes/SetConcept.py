wel={1,2,3}
hel={4,3,6}


wel.update(hel)
print(wel)

hel.add(5)
hel.add(2)
print(hel)

hel.discard(5)
print(hel)

print(sum(hel))
print(max(hel))

a={1,3,5}
b={1,2,3}

print(a.union(b),a|b) #all element
print(a.intersection(b),a&b) #common element
print(a.difference(b),a-b) #return a element and not present b
print(a.symmetric_difference(b),a^b) #all element witout common element

a.symmetric_difference_update(b) #it will update the symmetric value in the a
print(a)

c={1,2,3,5,6}
print(c.issuperset(b)) #check b subset of c
print(c.issubset(b)) #it check c is subset of b

a.pop() #removes the first element but inside raise the key error
print(a)