import glob,os
numbers = [1, 2, 3, 4]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

print("--------------------------------------------")

# filtering even numbers from a list
even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]

print(even_numbers)

# Output: [2, 4, 6, 8]

print("--------------------------------------------")
numbers = [1, 2, 3, 4, 5, 6]

# find even and odd numbers
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]

print(even_odd_list)

print("--------------------------------------------")
multiplication = [[i * j for j in range(1, 6)] for i in range(2, 5)]

print(multiplication)

print("--------------------------------------------")
#prime numeber using list compereshensions

# primeNo=[[if i%n==0 for j in range(i,n)]print(i) if True  for i in range (2,n)]

#it stores the key as filename in the directory and value metadata value in the value

#//-------Dictornary comprehensions-----------//
metadata_dict = {f:os.stat(f) for f in glob.glob('DataTypes/*.py')} 
print(metadata_dict)

print("-----------------------------------------------")
# print("---------------------------/--------------------")
print(metadata_dict.keys())

print("-----------------------------------------------")
keys=['a','b','c','d']
values=[10,11,20,33]

dict={k:v for (k,v) in zip(keys,values)}
print(dict)

a_dict = {'a': 1, 'b': 2, 'c': 3}
b_dict={value:key for key, value in a_dict.items()}

print(b_dict)


#///---------set compershension===---///
print("----------------------------------------------------------")
a_set=set(range(10))

print(a_set)

b_set={i**2 for i in a_set}
c_set={i for i in a_set if i%2==0}

print(b_set)
print(c_set)