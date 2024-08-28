x="hari"
print(list(x))

li=["harish",14,2.45]

li.append("deepak")
li.insert(2,"guru")
li.remove(2.45)   #delete by values
print(li)

li.pop(2)  #delete by index

print(li)

print(li.index("deepak"))

li[0]="hari"

print(li)

num=[1,2,3]

li.extend(num)

print(li)

del li[4]

print(li)

del li[2:4]

li.reverse()
print(li)

val=[5,2,3,9]
val.sort()
print(val)
print(sum(val))
