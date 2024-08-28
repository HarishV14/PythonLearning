num=(1,2,3.4)

val=tuple((3,4,5,4,2,3))

print(num[2],"---",val[2])

for n in num:
    print(n)

print(3 in val)

print(val.count(3))  # count the number of element in tup

print(val.index(3)) # it finds the first index
print(val.index(3,1)) #it finds the after first index where it occurs in the list

