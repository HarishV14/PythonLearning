import itertools

perm=itertools.permutations([1,2,3],2)
print(next(perm))
print(next(perm))
print(next(perm))

#for remaining permutation
for i in perm:
    print(i,end=" ")

perm1=itertools.permutations("abc",3)

for i in perm1:
    print(i)

print(list(itertools.permutations("abc",3)))


print("-----------------------------------------------------------")


#Cartesion product of 2 string

print(list(itertools.product('12','ABS')))

print(list(itertools.combinations('ABC',2)))

print("-----------------------------------------------------------")

#groupby method

name=['Dora', 'Ethan', 'Wesley', 'John', 'Anne',
'Mike', 'Chris', 'Sarah', 'Alex', 'Lizzie']

groups=itertools.groupby(name,len)
print(next(groups))

for length,names in groups:
    print('Name in {0:d} length'.format(length))
    for n in names:
        print(n)

print("-----------------------------------------------------------")

#chain method in iterator

#it iterates the first iterator and second iterator next
print(list(itertools.chain(range(0,3),range(10,14))))

#it combines the two iterator one by one anything alone will not display but in the iterator tool as zip_longest to will combine with null for remaing element
print(list(zip(range(0,3),range(10,14))))
print(list(itertools.zip_longest(range(0,3),range(10,14))))

print("-----------------------------------------------------------")
#it translate using the dict by the translate method
translation_table = {ord('A'): ord('O')} 
print(translation_table)

#it changes the value A to O by the ascii value
print("MARSKA".translate(translation_table))


print("-----------------------------------------------------------")
#translations 
characters = tuple(ord(c) for c in 'SMEDONRY')
guess = tuple(ord(c) for c in '91570682') 
#We have both ascii value

#converting to the dict
translation_table = dict(zip(characters, guess))

print(characters,"-----------character")
print(guess,"----------------guesss")
print(translation_table,"-------translation table")
print('SEND + MORE == MONEY'.translate(translation_table))

print("-----------------------------------------------------------")
#eval

print(eval('1+1==2'))
print(eval('1+1==3'))
print(eval('"A" + "B"'))
print(eval('"MARK".translate({65:69})'))
print(eval('"AAAAA".count("A")'))
x=5
print(eval("x * 5"))
print(eval("pow(x, 2)"))

import subprocess
print(eval("subprocess.getoutput('ls ~')"))