languages = ['Swift', 'Python', 'Go']

# access elements of the list one by one
for lang in languages:
    print(lang)


language = 'Python'

# iterate over each character in language
for x in language:
    print(x)

# iterate from i = 0 to i = 3
for i in range(4):
    print(i)


#with else clause
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


#without acessing item
languages = ['Swift', 'Python', 'Go']

# using _ for placeholder variable
for _ in languages:
    print('Hi')


#nested for loop
# outer loop 
for i in range(2):
    # inner loop
    for j in range(2): 
        print(f"i = {i}, j = {j}")


#range inbuilt function

val=range(-3,10)  #start,stop
val1=range(2,20,4) #start,stop,step

print(list(val))
print(list(val1))