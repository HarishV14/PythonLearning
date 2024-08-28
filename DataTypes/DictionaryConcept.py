names={1:'harish',
       2:'guru',
       3:'deepak'}

print(names[1],names.get(1))

val={(1,2):"one two",3:"three"}

print(val[(1,2)],val.get((1,2)))

val[4]="four" # adding the value with new key and new value
val[(1,2)]="two one" # changing the value to that old key

print(val)

del val[(1,2)]

print(val)

for v in val:
    print("keys",v)
    print("value",val[v])
val.pop(3)
print(val)

val.update(names)

print(val)

print(6 in val)
print(2 in val)

print(val.keys())
print(val.values())